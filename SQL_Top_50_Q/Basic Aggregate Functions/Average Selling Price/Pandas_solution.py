# Pandas solution for Average Selling Price
import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    df = prices.merge(units_sold, how="left", on=["product_id"])
    df = df.loc[(df['purchase_date'] >= df['start_date']) & (df['purchase_date'] <= df['end_date']) | (df['purchase_date'].isna())]
    df["total"] = df['price'] * df["units"]
    return df.fillna(0).groupby('product_id').agg(
        {'total': 'sum',
        'units': 'sum'}
    ).apply(lambda x: round(x['total']/x['units'], 2) if x['units'] != 0 else 0, axis=1).reset_index(name="average_price")
