# Pandas solution for Product Sales Analysis I

import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    return sales.merge(product, on="product_id", how="left")[["product_name", "year", "price"]]
