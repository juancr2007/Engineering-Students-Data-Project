# Engineering-Students-Data-Project
This is the final project for SJS Program for Coding. The data was filtered to help narrow down the thousands of college students information down to those who are majoring in engineering.

## Dataset
The information takes the dataset from "University Student Performance &amp; Habits Dataset" by Robiul Hasan Jisan from Kaggle.

## Folder Structure
- code/
  - code.py -- This file contains the code that helped create all of the folders and files that are in this repository
  - data_new.py -- This file contains the code that helped create all the graphs in the features folder of this repository
- data/
  - Student_data.csv -- Table that includes the data of all 5000 students
- features/
  - Final_CGPA_bar.png -- Histogram showing how many students achieved each CGPA value
  - Social_hours_gender.png -- Boxplot showing how many hours students of each gender spend socially.
  - att_hist.png -- Histogram showing how many students attendance a certain percentage of their classes
  - hist_age_vs_att.png -- Average attendance percentage of classes for each student age
  - p_vs_f.png -- Comparing the average previous CGPA to the final CGPA of all students
  - scatter_att_vs_gpa.png -- Scatter plot that plots every students attendance percentage with their final CGPA
  - scatter_studying_vs_gpa.png -- Scatter plot that plots every students hours specnt studying with their final CGPA
- output/
  - eng_inspection.txt -- Presents data gathered from the enginerring_data.csv
  - engineering_data.csv -- Table that inludes the data for only Engineering students that were present in the dataset
  - total_inspection.txt -- Presents data gathered from the Student_data.csv
   
## Data Gathered
The data that was collected from the csv files is listed here in order:
- Shape of the dataframe
  - presented as a tuple
- Number of rows
- Number of columns
- Name of columns
- Attendance percentage for each category
  - How many people attended class per percentage
- Top 5 rows of the dataset
- Bottom 5 rows of the dataset
- Datatypes of each column
- Numeric values for all datatypes
