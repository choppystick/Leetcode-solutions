# Pandas solution for Monthly Transactions I
import pandas as pd
import numpy as np

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions['month'] = transactions['trans_date'].dt.strftime("%Y-%m")
    transactions['state'] = np.where(transactions['state'] == 'approved', transactions['amount'], np.nan)
    return transactions.groupby(['month', 'country'], dropna=False).agg(
        trans_count=('id', 'count'),
        approved_count=('state', 'count'),
        trans_total_amount=('amount', 'sum'),
        approved_total_amount=('state', 'sum')
    ).reset_index()
