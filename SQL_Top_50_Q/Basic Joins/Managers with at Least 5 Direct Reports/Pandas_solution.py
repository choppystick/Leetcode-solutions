# Pandas solution for Managers with at Least 5 Direct Reports

import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    manager_id = employee["managerId"].value_counts().reset_index(name="count")
    return employee.merge(manager_id[manager_id["count"] >= 5], how="inner", left_on="id", right_on="managerId")[["name"]]
