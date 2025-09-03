## 📄 README.md

# 🛠️ E-Commerce Data Engineering Project

An end-to-end **data engineering pipeline** built on the [Olist Brazilian E-Commerce Dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).  
Covers the full workflow: **raw data → ingestion → transformation (dbt) → warehouse → analytics → lineage → dashboard**.

## 📊 Architecture

```

Sample Data (CSV)
→ Ingestion (Python + SQLAlchemy)
→ Postgres raw schema
→ dbt Staging (views)
→ dbt Marts (fact & dim tables)
→ Analytics schema
→ Documentation & lineage (dbt docs)
→ Dashboard (Metabase / Superset)

```

## 📂 Project Structure

```

e-commerce-data-engineering/
├── data/ # Datasets (raw, sample, staging, processed)
│ ├── raw/ # Full Olist dataset (42MB, ignored by Git)
│ ├── sample/ # Committed subset (~1k rows per table)
│ │ └── olist/ # orders, customers, products, items, etc.
│ ├── staging/ # Intermediate files (ignored)
│ └── processed/ # Analytics-ready exports (ignored)
│
├── src/ # Python source code
│ ├── ingestion/ # Scripts to load CSV → Postgres raw schema
│ ├── transformations/ # Data cleaning / enrichment helpers
│ └── utils/ # Common functions (logging, config, etc.)
│
├── jobs/ # CLI entry points
│ ├── create_sample_from_raw.py
│ └── ingest_to_db.py
│
├── airflow/ # Orchestration layer
│ └── dags/ # Airflow DAGs for ETL
│
├── dbt_project/ # dbt models & configs
│ ├── models/
│ │ ├── sources/ # Source definitions (raw tables)
│ │ ├── staging/ # Staging models (cleaned views)
│ │ └── marts/ # Fact & dimension tables
│ ├── macros/ # Custom macros (e.g., schema naming)
│ └── tests/ # Schema/data quality tests
│
├── notebooks/ # Jupyter notebooks for exploration
├── tests/ # Unit tests for Python code
├── .env.example # Example env vars for Postgres
├── .gitignore # Ignore rules (raw data, dbt logs, etc.)
├── pyproject.toml # Dependencies (uv/Poetry compatible)
└── README.md

```

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

```sql
CREATE SCHEMA raw;
CREATE SCHEMA staging;
CREATE SCHEMA analytics;
```

### 2. Install dependencies (uv)

```bash
uv venv --seed --python 3.11 .venv
uv sync
```

### 3. Ingest sample data into Postgres

```bash
uv run python jobs/ingest_to_db.py
```

### 4. Run dbt

```bash
uv run dbt deps --project-dir dbt_project
uv run dbt debug --project-dir dbt_project
uv run dbt build --project-dir dbt_project
uv run dbt docs generate --project-dir dbt_project
uv run dbt docs serve --project-dir dbt_project
```

## 📜 Data

| Table            | Rows (sample) | Description          |
| ---------------- | ------------- | -------------------- |
| `orders`         | \~1,000       | Customer orders      |
| `customers`      | \~1,000       | Customer details     |
| `products`       | \~1,000       | Product catalog      |
| `order_items`    | \~1,000       | Order line items     |
| `order_payments` | \~1,000       | Payment transactions |
| `order_reviews`  | \~1,000       | Customer reviews     |

> Note: The full dataset (42MB) is **not committed**. Only the sample dataset is included for demo purposes.

## 🔗 Data Lineage

Example Lineage graph (from `fact_orders`):

![Lineage graph](assets/lineage_fact_orders.png)

## ✅ Current Progress

- ✔️ Project skeleton established
- ✔️ Sample data ingested into Postgres (`raw` schema)
- ✔️ dbt configured & connected
- ✔️ Staging models built (`stg_orders`, `stg_customers`, `stg_products`)
- ✔️ Additional staging models added (`stg_order_items`, `stg_order_payments`, `stg_order_reviews`)
- ✔️ Marts models created (`dim_customers`, `dim_products`, `fact_orders`)
- ✔️ Custom macros fixed → clean `staging` / `analytics` schemas
- ✔️ dbt lineage docs generated

## 📈 Next Steps

- [ ] Add more relationship tests (`fact_orders` → `dim_customers`, `dim_products`)
- [ ] Extend marts (e.g., `fact_payments`, `dim_sellers`)
- [ ] Connect BI tool (Metabase / Superset)
- [ ] Build dashboards (daily sales, top products, payment methods)
- [ ] Optimize pipelines & orchestrate with Airflow

## 📜 License

Data provided by [Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce).
Please review Kaggle’s license terms before reuse.
