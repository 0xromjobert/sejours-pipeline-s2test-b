from sejours_pipeline.pipeline import run

LIGNES = [
    {
        "id": "S1",
        "service": "cardio",
        "entree": "2026-03-01",
        "sortie": "2026-03-04",
        "age": "71",
    },
    {
        "id": "S2",
        "service": "",
        "entree": "2026-03-02",
        "sortie": "2026-03-03",
        "age": "45",
    },
]


class FakeSource:
    """Une source écrite à la main : ni fichier, ni API."""

    def __init__(self, lignes: list[dict]) -> None:
        self.lignes = lignes

    def extract(self) -> list[dict]:
        return self.lignes


class MemoryLoader:
    """Une destination en mémoire : garde les séjours dans une liste."""

    def __init__(self) -> None:
        self.sejours = []

    def write(self, sejours) -> None:
        self.sejours = list(sejours)


def test_run_charge_les_valides_et_rejette_les_autres():
    loader = MemoryLoader()
    sejours, rejets = run(FakeSource(LIGNES), loader)
    assert [s.id for s in loader.sejours] == ["S1"]
    assert len(sejours) == 1
    assert rejets[0]["motif"] == "service"
