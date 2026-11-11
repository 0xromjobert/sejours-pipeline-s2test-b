"""Les destinations : où vont les séjours validés."""

import duckdb

from sejours_pipeline.models import Sejour, duree_jours


class DuckDBLoader:
    """Écrit les séjours dans une table DuckDB."""

    def __init__(self, chemin: str) -> None:
        self.chemin = chemin

    def write(self, sejours: list[Sejour]) -> None:
        """Remplace la table sejours par les séjours donnés."""
        with duckdb.connect(self.chemin) as con:
            con.execute(
                "CREATE OR REPLACE TABLE sejours ("
                "id VARCHAR, service VARCHAR, entree DATE, sortie DATE, "
                "age INTEGER, duree INTEGER)"
            )
            con.executemany(
                "INSERT INTO sejours VALUES (?, ?, ?, ?, ?, ?)",
                [
                    (
                        s.id,
                        s.service,
                        s.entree,
                        s.sortie,
                        s.age,
                        duree_jours(s.entree, s.sortie),
                    )
                    for s in sejours
                ],
            )
