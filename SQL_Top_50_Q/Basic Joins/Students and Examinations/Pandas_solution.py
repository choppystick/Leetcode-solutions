# Pandas solution for Students and Examinations

import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:

    count = examinations.groupby(["student_id", "subject_name"]).size().reset_index(name="attended_exams")
    df = students.merge(subjects, how="cross").merge(count, how="left", on=["student_id", "subject_name"]).sort_values(by=["student_id", "subject_name"])
    df["attended_exams"] = df["attended_exams"].fillna(0)
    return df
    