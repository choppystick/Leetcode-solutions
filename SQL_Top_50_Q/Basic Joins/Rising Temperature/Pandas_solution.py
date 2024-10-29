# Pandas solution for Rising Temperature

import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values(by="recordDate", inplace=True)
    return (weather.loc[(weather.diff()["temperature"] > 0) & (weather.recordDate.diff().dt.days == 1), ["id"]])