from sejours_pipeline.sources import CsvSource


def test_csv_source_lit_les_lignes(tmp_path):
    fichier = tmp_path / "sejours.csv"
    fichier.write_text(
        "id,service,entree,sortie,age\nS1,cardio,2026-03-01,2026-03-04,71\n",
        encoding="utf-8",
    )
    lignes = CsvSource(str(fichier)).extract()
    assert lignes == [
        {
            "id": "S1",
            "service": "cardio",
            "entree": "2026-03-01",
            "sortie": "2026-03-04",
            "age": "71",
        }
    ]
