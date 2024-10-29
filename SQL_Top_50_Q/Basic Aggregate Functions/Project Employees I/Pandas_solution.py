# Pandas solution for Project Employees I

import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    return project.merge(employee, how="left", on="employee_id").groupby("project_id")['experience_years'].mean().round(2).reset_index(name='average_years')