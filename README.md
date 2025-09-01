# 🛠️ E-Commerce Data Engineering Project

An end-to-end **data engineering pipeline** built on the [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).  
Covers the full workflow: **raw data → ingestion → transformation (dbt) → warehouse → analytics**.

---

## 📂 Project Structure

e-commerce-data-engineering/
├── data/
│ ├── raw/ # Full dataset (42MB, ignored by git)
│ ├── sample/ # 6 sampled CSV tables (committed)
│ ├── staging/ # Intermediate landing zone (ignored)
│ └── processed/ # Analytics-ready exports (ignored)
├── src/ # Python source (utils, io, ingestion, generation)
├── jobs/ # CLI entry scripts (generate, ingest, etc.)
├── airflow/ # Airflow DAGs
├── dbt_project/ # dbt models, tests, snapshots, seeds
├── notebooks/ # Exploratory analysis
├── tests/ # Unit tests
└── README.md

---

## 📊 Architecture

Sample Data (CSV)
→ Ingestion (Python + SQLAlchemy)
→ Postgres raw schema
→ Transformation (dbt staging + marts)
→ Analytics schema
→ Documentation & lineage (dbt docs)
→ Dashboard (Metabase / Superset)

---

## 🔧 Tech Stack

- **Python**: pandas, SQLAlchemy, psycopg2, Faker, dotenv
- **Airflow**: orchestration (DAGs in `airflow/dags/`)
- **dbt**: transformations, testing, lineage docs
- **Postgres**: warehouse (via Docker container)
- **Metabase / Superset**: dashboard & visualization

---

## 🚀 Quickstart

### 1. Start Postgres (via Docker)

```bash
docker run --name postgres-olist \
  -e POSTGRES_USER=calvin \
  -e POSTGRES_PASSWORD=calvin \
  -e POSTGRES_DB=olist \
  -p 5432:5432 \
  -d postgres:15
```

Create schemas:
CREATE SCHEMA raw;
CREATE SCHEMA staging;
CREATE SCHEMA analytics;

2. Install dependencies (uv)
   uv venv --seed --python 3.11 .venv
   uv sync

3. Ingest sample data into Postgres
   uv run python jobs/ingest_to_db.py

4. Run dbt
   uv run dbt --project-dir dbt_project deps
   uv run dbt --project-dir dbt_project debug
   uv run dbt --project-dir dbt_project build
   uv run dbt --project-dir dbt_project docs generate
   uv run dbt --project-dir dbt_project docs serve

⚠️ Data

Full dataset (42MB) → downloaded from Kaggle, stored in data/raw/, gitignored

Sample dataset (~6 CSVs) → included in data/sample/olist/, used for quick demo

Tables: orders, customers, products, order_items, order_payments, order_reviews

✅ Current Progress

✔️ Project skeleton established

✔️ Sample data ingested into Postgres (raw schema)

✔️ dbt connected and stg_orders built in staging schema

✔️ Basic tests (not_null, unique) passing

📈 Next Steps

Complete staging models for all 6 tables

Add marts (fact_orders, dim_customers, dim_products)

Add relationship tests (foreign key checks)

Generate dbt lineage docs and add screenshots to README

Build dashboard (Metabase / Superset)

📜 License

Data provided by Olist
.
Please review Kaggle’s license terms before reuse.

---

这样一份 README 能完整反映你现在的进度（已经 ingestion + dbt 跑通），同时也告诉别人怎么复现和接下来要做什么。

要不要我帮你再生成一张 **架构图（更新版，包含 raw → staging → marts → docs）**，你可以加到 README 里展示？
