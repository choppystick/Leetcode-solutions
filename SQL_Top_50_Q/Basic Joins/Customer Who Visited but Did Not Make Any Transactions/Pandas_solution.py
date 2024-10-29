# Pandas solution for Customer Who Visited but Did Not Make Any Transactions

import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merge = visits.merge(transactions, on="visit_id", how="left")
    return merge[merge.transaction_id.isna()].groupby("customer_id").size().reset_index(name="count_no_trans")
