# Pandas solution for Immediate Food Delivery II
import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    first = delivery[delivery['order_date'] == delivery.groupby('customer_id')['order_date'].transform('min')]

    return pd.DataFrame({'immediate_percentage': [round((first['order_date'] == first['customer_pref_delivery_date']).mean() * 100, 2)]})