from pathlib import Path
import pandas as pd
import csv
import kagglehub


path = kagglehub.dataset_download("robiulhasanjisan/university-student-performance-and-habits-dataset")

print("Path to dataset files:", path)

project = Path("Final Project SJS")

data_folder = project / "data"
output_folder = project / "output"
code_folder = project / "code"
features_folder = project / "features"

data_folder.mkdir(parents=True, exist_ok=True)
output_folder.mkdir(parents=True, exist_ok=True)
code_folder.mkdir(parents=True, exist_ok=True)
features_folder.mkdir(parents=True, exist_ok=True)

# -------------------------------------------------------------------
input_csv = data_folder / "Student_data.csv"

student_data_df = pd.read_csv(input_csv)

# llllllllllllllllllllllllllllllllllllllllllllllllllllll


tuple_ = student_data_df.shape

row_count = student_data_df.shape[0]

column_count = student_data_df.shape[1]

column_names = student_data_df.columns

if "Attendance_Pct" in student_data_df.columns:
    Attendance_Pct_count = student_data_df["Attendance_Pct"].value_counts()

nas = student_data_df.isna().sum()

head_val = student_data_df.head() 

tail_val = student_data_df.tail() 

d_types_df = student_data_df.dtypes 

df_desc = student_data_df.describe()

age = student_data_df["Age"].median()

names = {
    "Study_Hours_Per_Day" : "Hours_For_Study",
    "Social_Hours_Week" : "Free_Time"
}
new_names = student_data_df.rename(columns=names)

engineering_students = student_data_df[student_data_df["Major"]=="Engineering"]

review_output = project / "output" / "total_inspection.txt"
with open(review_output, "a") as file:
    file.write(f"Shape of the dataframe: {tuple_}\n")
    file.write(f"\n# of rows: {row_count}\n")
    file.write(f"\n# of columns: {column_count}\n")

    file.write("column names:\n")
    for column in range(column_count):
        file.write(f"- {column_count}\n")

    file.write(f"\nAttendence percentage count for each category: \n{Attendance_Pct_count}\n")
    file.write(f"\ntop 5 rows:\n{head_val}\n")
    file.write(f"\nbottom 5 rows:\n{tail_val}")
    file.write(f"\ndatatypes of each column:\n{d_types_df}\n")
    file.write(f"\nNumeric values for all data:\n{df_desc}")


# ----------------------------------------------------------------------------------------------------------
                        #total_inspection.txt
# COMMENT OUT EVERYTHING ABOVE OR BELOW THIS LINE TO PUT THE DATA IN DIFFERENT FILES
                        # eng.inspection.txt
# -------------------------------------------------------------------------------------------------------------
# engineering_students = student_data_df[student_data_df["Major"]=="Engineering"]

# engineering_output = project / "data" / "engineering_data.csv"

# engineering_students.to_csv(engineering_output, index=False)

# new_csv = data_folder / "engineering_data.csv"

# eng_student_df = pd.read_csv(new_csv)
# # llllllllllllllllllllllllllllllllllllllllllllllll

# tuple_ = eng_student_df.shape

# row_count = eng_student_df.shape[0]

# column_count = eng_student_df.shape[1]

# column_names = eng_student_df.columns

# if "Attendance_Pct" in eng_student_df.columns:
#     Attendance_Pct_count = student_data_df["Attendance_Pct"].value_counts()

# nas = eng_student_df.isna().sum()

# head_val = eng_student_df.head() 

# tail_val = eng_student_df.tail() 

# d_types_df = eng_student_df.dtypes 

# df_desc = eng_student_df.describe()

# age = eng_student_df["Age"].median()

# names = {
#     "Study_Hours_Per_Day" : "Hours_For_Study",
#     "Social_Hours_Week" : "Free_Time"
# }
# new_names = eng_student_df.rename(columns=names)

# engineering_students = student_data_df[student_data_df["Major"]=="Engineering"]

# review_output = project / "output" / "eng_inspection.txt"
# with open(review_output, "a") as file:
#     file.write(f"Shape of the dataframe: {tuple_}\n")
#     file.write(f"\n# of rows: {row_count}\n")
#     file.write(f"\n# of columns: {column_count}\n")

#     file.write("column names:\n")
#     for column in range(column_count):
#         file.write(f"- {column_count}\n")

#     file.write(f"\nAttendence percentage count for each category: \n{Attendance_Pct_count}\n")
#     file.write(f"\ntop 5 rows:\n{head_val}\n")
#     file.write(f"\nbottom 5 rows:\n{tail_val}")
#     file.write(f"\ndatatypes of each column:\n{d_types_df}\n")
#     file.write(f"\nNumeric values for all data:\n{df_desc}")
