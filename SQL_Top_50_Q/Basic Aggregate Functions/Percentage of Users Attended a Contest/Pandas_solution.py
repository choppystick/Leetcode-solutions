# Pandas solution for Percentage of Users Attended a Contest

import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    total_users = users.user_id.count()
    group = register.groupby('contest_id').size().reset_index(name='percentage')
    group['percentage'] = (group['percentage']*100/total_users).round(2)
    return group.sort_values(by=['percentage', 'contest_id'], ascending=[False, True])
