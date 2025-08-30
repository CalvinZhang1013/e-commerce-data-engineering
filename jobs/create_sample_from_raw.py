import pandas as pd
from pathlib import Path

RAW_DIR = Path("data/raw/olist")
SAMPLE_DIR = Path("data/sample/olist")

def create_sample(input_file: str, output_file: str, n : int = 1000):
    df = pd.read_csv(RAW_DIR / input_file)

    # 如果行数少于n, 就直接保存
    sample_df = df.sample(n=min(n, len(df)), random_state=42)
    SAMPLE_DIR.mkdir(parents=True, exist_ok=True)
    sample_df.to_csv(SAMPLE_DIR / output_file, index=False)
    print(f"{input_file} -> {output_file} ({len(sample_df)} rows)")

if __name__ == "__main__":
    SAMPLE_DIR.mkdir(parents=True, exist_ok=True)

    #抽样的文件
    files = [
        ("olist_orders_dataset.csv", "orders_sample.csv"),
        ("olist_customers_dataset.csv", "customers_sample.csv"),
        ("olist_products_dataset.csv", "products_sample.csv"),
        ("olist_order_items_dataset.csv", "order_items_sample.csv"),
        ("olist_order_payments_dataset.csv", "order_payments_sample.csv"),
        ("olist_order_reviews_dataset.csv", "order_reviews_sample.csv"),
    ]

    for infile, outfile in files:
        create_sample(infile, outfile, n=1000)