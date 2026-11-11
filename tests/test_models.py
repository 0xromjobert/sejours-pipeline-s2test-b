from datetime import date

import pytest
from pydantic import ValidationError

from sejours_pipeline.models import Sejour, duree_jours


def test_duree_jours():
    assert duree_jours(date(2026, 3, 1), date(2026, 3, 4)) == 3


def test_sortie_avant_entree_leve_erreur():
    with pytest.raises(ValueError):
        duree_jours(date(2026, 3, 4), date(2026, 3, 1))


def test_sejour_valide():
    s = Sejour.model_validate(
        {
            "id": "S1",
            "service": "cardio",
            "entree": "2026-03-01",
            "sortie": "2026-03-04",
            "age": "71",
        }
    )
    assert s.age == 71
    assert s.entree == date(2026, 3, 1)


def test_sejour_sans_service_refuse():
    with pytest.raises(ValidationError):
        Sejour.model_validate(
            {
                "id": "S1",
                "service": "",
                "entree": "2026-03-01",
                "sortie": "2026-03-04",
                "age": "71",
            }
        )
