"""Le pipeline : extraire, valider, charger."""

import logging
import os

from pydantic import ValidationError

from sejours_pipeline.loaders import DuckDBLoader
from sejours_pipeline.models import Sejour
from sejours_pipeline.sources import CsvSource

log = logging.getLogger(__name__)


def run(source, loader) -> tuple[list[Sejour], list[dict]]:
    """Valide chaque ligne de la source et charge les séjours valides."""
    sejours, rejets = [], []
    for ligne in source.extract():
        try:
            sejours.append(Sejour.model_validate(ligne))
        except ValidationError as erreur:
            motif = erreur.errors()[0]["loc"]
            rejets.append(
                {**ligne, "motif": ".".join(str(m) for m in motif) or "sejour"}
            )
    loader.write(sejours)
    log.info("%d séjours chargés, %d rejetés", len(sejours), len(rejets))
    return sejours, rejets


def main() -> None:
    logging.basicConfig(
        level=logging.INFO, format="%(levelname)s %(name)s : %(message)s"
    )
    source = CsvSource(os.environ["SEJOURS_CSV"])
    loader = DuckDBLoader(os.environ.get("SEJOURS_DB", "sejours.duckdb"))
    run(source, loader)


if __name__ == "__main__":
    main()
