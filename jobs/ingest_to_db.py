import os
import pandas as pd
from sqlalchemy import create_engine, text
from pathlib import Path
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

PGUSER = os.getenv("PGUSER", "calvin")
PGPASSWORD = os.getenv("PGPASSWORD", "calvin")
PGHOST = os.getenv("PGHOST", "localhost")
PGPORT = os.getenv("PGPORT", "5432")
PGDATABASE = os.getenv("PGDATABASE", "olist")

# SQLAlchemy 连接字符串
engine = create_engine(f"postgresql+psycopg2://{PGUSER}:{PGPASSWORD}@{PGHOST}:{PGPORT}/{PGDATABASE}")

SAMPLE_DIR = Path("data/sample/olist")

# 要导入的表名和文件名对应
tables = {
    "customers": "customers_sample.csv",
    "orders": "orders_sample.csv",
    "products": "products_sample.csv",
    "order_items": "order_items_sample.csv",
    "order_payments": "order_payments_sample.csv",
    "order_reviews": "order_reviews_sample.csv",
}

def ingest_table(table_name, file_name):
    file_path = SAMPLE_DIR / file_name
    print(f"🚀 Loading {file_name} into raw.{table_name} ...")

    df = pd.read_csv(file_path)

    # 写入数据库
    df.to_sql(
        table_name,
        engine,
        schema="raw",
        if_exists="replace",   # 如果存在则覆盖，可以改为 'append'
        index=False,
        method="multi",        # 批量插入
        chunksize=1000
    )

    print(f"✅ {table_name}: {len(df)} rows inserted.")

if __name__ == "__main__":
    with engine.connect() as conn:
        conn.execute(text("SET search_path TO raw, public;"))

    for table, file in tables.items():
        ingest_table(table, file)

    print("🎉 All sample data ingested into Postgres (schema=raw).")
