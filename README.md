# sejours-pipeline

Lit des séjours hospitaliers dans un CSV, valide chaque ligne, charge les séjours valides dans DuckDB.
Données **fictives** uniquement.

```
uv sync
uv run pytest
cp .env.example .env
uv run --env-file .env sejours-pipeline
```
