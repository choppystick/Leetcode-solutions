# Pandas solution for Department Top Three Salaries
import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee.merge(
        department,
        left_on='departmentId',
        right_on='id',
        suffixes=('_employee', '_department')
    )

    def get_top_3_unique_salaries(group):
        top_3_salaries = sorted(group['salary'].unique(), reverse=True)[:3]
        return group[group['salary'].isin(top_3_salaries)]
    
    result = (merged_df.groupby('name_department', as_index=False)
              .apply(get_top_3_unique_salaries)
              .reset_index(drop=True)
              .rename(columns={
                  'name_employee': 'Employee',
                  'name_department': 'Department',
                  'salary': 'Salary'
              })[['Department', 'Employee', 'Salary']]
             )
    
    return result