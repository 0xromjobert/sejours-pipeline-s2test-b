"""La forme d'un séjour et les règles qu'il doit respecter."""

from datetime import date

from pydantic import BaseModel, Field, model_validator


class Sejour(BaseModel):
    """Un séjour hospitalier : une ligne de la table sejours."""

    id: str = Field(min_length=1)
    service: str = Field(min_length=1)
    entree: date
    sortie: date
    age: int = Field(ge=0)

    @model_validator(mode="after")
    def sortie_apres_entree(self) -> "Sejour":
        """Refuse un séjour dont la sortie est avant l'entrée."""
        if self.sortie < self.entree:
            raise ValueError(f"sortie {self.sortie} avant entrée {self.entree}")
        return self


def duree_jours(entree: date, sortie: date) -> int:
    """Nombre de jours entre l'entrée et la sortie."""
    if sortie < entree:
        raise ValueError(f"sortie {sortie} avant entrée {entree}")
    return (sortie - entree).days
