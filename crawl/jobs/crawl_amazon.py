# crawl/jobs/crawl_amazon.py
import sys
print(sys.path)

from crawl.core.fetcher import fetch
from crawl.core.storage import save_json
from crawl.sites.amazon import parse

def main():
    url = "https://www.amazon.sg/Razer-blackshark-platform-esports-headset/dp/B089SSFV85?ref_=Oct_d_obs_d_6385488051_0&pd_rd_w=DD8j3&content-id=amzn1.sym.f54adfb5-cb35-45d1-8cd0-1c9fc8020cc1&pf_rd_p=f54adfb5-cb35-45d1-8cd0-1c9fc8020cc1&pf_rd_r=S8X97V613H2J9W1N5QP6&pd_rd_wg=uf0NI&pd_rd_r=36c8251e-2da0-4a35-9f4a-06871f4f4f43&pd_rd_i=B089SSFV85&th=1"  # 示例：随机一个产品链接
    html = fetch(url)
    product = parse(html)
    print(product)

    # 保存结果
    save_json(product, "outputs/amazon_product.json")

if __name__ == "__main__":
    main()
