# Pandas solution for Confirmation Rate

import pandas as pd

def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    df = confirmations.groupby('user_id').agg(
        total=('action', 'count'),
        confirmed=('action', lambda x: (x == 'confirmed').sum())
    ).reset_index()
    
    df2 = signups[["user_id"]].merge(df, on="user_id", how="left").fillna(0)
    df2["confirmation_rate"] = round((df2["confirmed"]/df2["total"]).fillna(0), 2)
    return df2[["user_id", "confirmation_rate"]]
