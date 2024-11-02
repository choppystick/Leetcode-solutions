# Pandas solution for Queries Quality and Percentage

import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    queries['quality'] = queries.rating/queries.position + 1e-6
    queries['poor_query_percentage'] = (queries.rating < 3) * 100
    return queries.groupby('query_name')[["quality", 'poor_query_percentage']].mean().round(2).reset_index()
    
    
    