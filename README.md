# sejours-pipeline

Lit des séjours hospitaliers dans un CSV, valide chaque ligne, charge les séjours valides dans DuckDB.
Données **fictives** uniquement.

```
uv sync
uv run pytest
cp .env.example .env
uv run --env-file .env sejours-pipeline
```

## Données

Le pipeline lit `data/sejours.csv`, un export fictif des séjours fourni par l'équipe data.
Les données ne sont jamais dans Git : `data/`, `*.duckdb` et `.env` sont dans le `.gitignore`.
Même fictives, on prend l'habitude : les données de séjours se transmettent par un autre canal.
