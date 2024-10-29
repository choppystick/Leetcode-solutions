# Pandas solution for Average Time of Process per Machine

import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by=["machine_id", "process_id", "activity_type"], ascending=[True, True, False], inplace=True)
    diff = activity.timestamp.diff()
    machine_id = activity[activity.activity_type=="end"]["machine_id"]
    return (pd.DataFrame({"machine_id": machine_id, "processing_time":diff}).groupby("machine_id").mean().round(3).reset_index())
    
    
