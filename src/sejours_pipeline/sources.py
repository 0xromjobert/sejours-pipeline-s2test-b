"""Les sources : d'où viennent les lignes."""

import csv


class CsvSource:
    """Lit les séjours dans un fichier CSV."""

    def __init__(self, chemin: str) -> None:
        self.chemin = chemin

    def extract(self) -> list[dict]:
        """Renvoie une liste de dicts : une ligne du CSV par dict."""
        with open(self.chemin, encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f))
