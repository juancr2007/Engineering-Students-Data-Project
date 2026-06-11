from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import csv

project = Path(__file__).resolve().parent.parent
data_folder = project / "data"
output_folder = project / "output"
features_folder = project/ "features"

input_csv = output_folder / "engineering_data.csv"

eng_df = pd.read_csv(input_csv)

Final_CGPA_df = eng_df["Final_CGPA"].values
attendance_df = eng_df["Attendance_Pct"].values
# ---------------------------------------------------------------
# Students and their final cgpa
# plt.hist(Final_CGPA_df, bins=5, linewidth=0.5, color="red", edgecolor="black")
# plt.title("Final CGPA and Class Attendance")
# plt.xlabel("Final CGPA")
# plt.ylabel("Number of Students")
# plt.tight_layout()
# plt.savefig(features_folder / "Final_CGPA_bar.png", dpi=500)
# plt.show()

# plt.hist(attendance_df, bins=5, linewidth=0.5, color="green", edgecolor="black")
# plt.title("Attendance Percentage for Engineering Students")
# plt.xlabel("Attendance %")
# plt.ylabel("Number of Students")
# plt.savefig(features_folder / "att_hist.png", dpi=500)


# plt.scatter(eng_df["Attendance_Pct"], eng_df["Final_CGPA"], s=1)
# plt.title("Attendance Percentage vs Final CGPA")
# plt.xlabel("Attendance %")
# plt.ylabel("CGPA")
# plt.tight_layout()
# plt.savefig(features_folder / "scatter_att_vs_gpa.png")

# plt.scatter(eng_df["Study_Hours_Per_Day"], eng_df["Final_CGPA"], s=1)
# plt.title("Attendance Percentage vs Final CGPA")
# plt.xlabel("Hours of Studying")
# plt.ylabel("CGPA")
# plt.tight_layout()
# plt.savefig(features_folder / "scatter_studying_vs_gpa.png")


# age_att = eng_df.groupby("Attendance_Pct")["Age"].mean()
# age_att.plot(kind="hist")
# plt.title("Age vs Attendnace Percentage")
# plt.xlabel("Age")
# plt.ylabel("Attendance Percentage")
# plt.tight_layout()
# plt.savefig(features_folder / "hist_age_vs_att.png")


# p_gpa = eng_df["Previous_CGPA"].mean()
# f_gpa = eng_df["Final_CGPA"].mean()
# stu = eng_df.head()
# x = p_gpa
# y = f_gpa
# plt.bar(["Previous_CGPA", "Final_CGPA"], [p_gpa, f_gpa], color=["orange", "blue"])
# plt.title("Previous GPA vs Final GPA")
# plt.xlabel("Previous GPA")
# plt.ylabel("Final GPA")
# plt.savefig(features_folder / "p_vs_f.png")
# plt.show()

eng_df.boxplot(column="Social_Hours_Week", by="Gender")
plt.title("Box Plot for Hours Spent Socially per Week Organized by Gender")
plt.xlabel("Gender")
plt.ylabel("Social Hours Per Week")
plt.grid(True, alpha=0.2)
plt.tight_layout()
plt.savefig(features_folder/"Social_hours_gender.png")