print("\n","#" * 70)
print("Task 1: NumPy Introduction & Arrays")
print("#" * 70,"\n")
#Task 1: NumPy Introduction & Arrays
import numpy as np
arr = np.array([1,0,3,4,5,6,7,8,9,11])
ar=np.array([[1,0,3,4,5],[6,7,8,9,11]])
print("One Dimensional Array: ",arr)
print("\nTwo Dimensional Array: ",ar)
print("\n Size of the array is:  ", arr.size)
print(" Shape of the array is:  ",arr.shape)
print(" Data type of the array is:  ",arr.dtype)
print("\n Size of the array is:  ", ar.size)
print(" Shape of the array is:  ",ar.shape)
print(" Data type of the array is:  ",ar.dtype)

print("\n","#" * 70)
print("Task 2: NumPy Indexing, Slicing & Reshaping")
print("#" * 70,"\n")
#Task 2: NumPy Indexing, Slicing & Reshaping
od = np.array([31,23,95,73,93,24,35,34,25,24])
print("\nElement at index [5 & -2]: ",od[5],od[-2])
print("\nSlice [2:6] (elements from index 2 to 5):", od[2:6])
print("Slice [::2] (every 2nd element):", od[::2])
print("\nOriginal One Dimensional Array: ",od)
print("\n Reshape of the array is:  \n",od.reshape(5,2))
td = np.array([[12,19,23,25],[100,200,500,900]])
print("\n Shape of the another array is:  ",td.shape)
print("\n Access specific rows and columns: \n Element at Row 0,1 & Coln 2:",td[:,2])
print("\n Access specific rows and columns: \n Sub-matrix (rows 0-1, columns 1-3",td[0:2, 1:3])
print("\nOriginal Two Dimensional Array: ",td)
print("\n Reshape of the array is:  \n",td.reshape(4,2))

print("\n","#" * 70)
print("Task 3:NumPy Mathematical & Statistical Operations")
print("#" * 70,"\n")
#Task 3: NumPy Mathematical & Statistical Operations
a = np.array([15, 22, 8, 34, 19, 27, 11, 45, 30, 5])
b = np.array([5, 10, 2, 4, 3, 9, 1, 5, 6, 5])
print("\n Dataset: ","a = ",a,",","b = ",b)
print("\n Mathematical Operations:\n","\nAddition: ",np.add(a,b))
print("\nSubtraction: ",np.subtract(a,b))
print("\nMultiplication: ",np.multiply(a,b))
print("\nDivision: ",np.divide(a,b))
print("\nSTATISTICAL FUNCTIONS: \n","\nMean: ",np.mean(a))
print("Median: ",np.median(a))
print("Minimum: ",np.min(a))
print("Maximum: ",np.max(a))
print("Standard Deviation: ",np.std(a))
print("Sum:",np.sum(a))

print("\n","#" * 70)
print("Task 4: Pandas Series & DataFrame")
print("#" * 70,"\n")
#Task 4: Pandas Series & DataFrame 
import pandas as pd
s = pd.Series([50,90,31,23,19,12,24,25,1])
print("\nPanda Series:\n", s)
df = pd.DataFrame({"Student Name" : ["Kalpana","Raj","Aish","Priya","Loke"],
        "Roll No" : ["20023","20024","20020","20021","20022"],
        "Dept" : ["CS","EEE","BA","BCA","ME"],
        "Studying year" : ["Final year","Final year","2nd year","1st year","Final year"]})
print("\nPandas Student DataFrame:\n",df)
print("\n DataFrame Column Names:\n",df.columns)
print("\n DataFrame Index:\n",df.index)
df["Marks"] = [85, 90, 78, 92, 88]
print("\nUpdated DataFrame:\n",df)

print("\n","#" * 70)
print("Task 5: Reading & Inspecting Data")
print("#" * 70,"\n")
#Task 5: Reading & Inspecting Data 
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")
print(df)
print("\nThe First Five Rows of the datasets: \n",df.head(5))
print("\nThe Last Five Rows of the datasets: \n",df.tail(5))
print("\nNumber of rows & columns of the datasets: \n",df.shape)
print("\nNumber of rows: \n", df.shape[0])
print("\nNumber of columns: \n", df.shape[1])
print("\nColumns of the datasets: \n",df.columns)
print("\nData types of the datasets: \n",df.dtypes)
print("\nInfo of the datasets: \n",df.info())
print("\nStatistical Summary of the datasets: \n",df.describe())

print("\n","#" * 70)
print("Task 6: Selecting, Filtering & Sorting Data ")
print("#" * 70,"\n")
#Task 6: Selecting, Filtering & Sorting Data 
df = pd.read_csv("Sample - Superstore.csv", encoding="latin1")
print("Original Products DataFrame:\n",df)
print("\nSelecting specific columns(Order Date) of the dataset:\n",df.iloc[:,2])
print("\nSelecting specific columns(Customer Name) of the dataset:\n",df["Customer Name"])
print("\nSelecting specific rows of the dataset:\n",df.iloc[5])
print("\nQuantity greater than 10:\n",df[df["Quantity"]>10])
print("\nCategory == 'Technology' & Sales greater than 10000:\n",df[(df["Category"]=="Technology") & (df["Sales"]>10000)])
print("\nSub-Category == 'Phones' OR State == 'New York':\n",df[(df["Sub-Category"]=="Phones") | (df["State"]=="New York")])
print("\nSort by Price Ascending:\n ", df.sort_values(by="Order Date",ascending=True))
print("\nSort by Price Descending: \n", df.sort_values(by="Order Date",ascending=False))

print("\n","#" * 70)
print("Task 7: Handling Missing Values ")
print("#" * 70,"\n")
#Task 7: Handling Missing Values 
em = pd.read_csv("employees_missing.csv")
print("\nOriginal Dataset: \n",em)
print("\nMisssing Values:\n",em.isnull().any())
print("\nCount of missing values per column:\n",em.isnull().sum(axis=0))
print("\nTotal missing values in dataset:\n",em.isnull().sum().sum())
print("\n",em.dropna(),"\nDataset AFTER removing rows with missing values (dropna):\n",em)
em["Age"] = em["Age"].fillna(em["Age"].median())
print("\n Age value filling with using median:\n",em["Age"])
em["Salary"] = em["Salary"].fillna(em["Salary"].mean())
print("\n Salary value filling with using median:\n",em["Salary"])
em["JoiningDate"] = em["JoiningDate"].fillna(0)
print("\n Dates value filling with 0:\n",em["JoiningDate"])
em["City"] = em["City"].fillna(em["City"].mode()[0])
print("\n City value filling with using mode:\n",em["City"])
em["Rating"] = em["Rating"].fillna(em.groupby("City")["Rating"].transform("mean"))
print("\n Rating value filling with 0:\n",em["Rating"])
print("\nDataset AFTER filling missing values:\n",em)

print("\n","#" * 70)
print("Task 8: Merge, Concatenate, GroupBy & Pivot Table ")
print("#" * 70,"\n")
#Task 8: Merge, Concatenate, GroupBy & Pivot Table 
employees = pd.DataFrame({
    "EmpID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Helen"],
    "DeptID": [1, 2, 2, 3, 1, 2, 3, 1],
    "Salary": [45000, 62000, 58000, 75000, 47000, 68000, 82000, 51000]})
departments = pd.DataFrame({
    "DeptID": [1, 2, 3, 4],
    "DeptName": ["HR", "IT", "Finance", "Marketing"],
    "Location": ["Delhi", "Bangalore", "Mumbai", "Chennai"]})
merged = pd.merge(employees, departments, on="DeptID", how="left")
print("Merging two DataFrames using a common column (DeptID):\n",merged)
new_employees = pd.DataFrame({
    "EmpID": [109, 110],
    "Name": ["Ian", "Julia"],
    "DeptID": [2, 4],
    "Salary": [71000, 55000]})
concatenated = pd.concat([employees, new_employees], ignore_index=True)
print("\nConcatenating two dataframe: Employees + New Employees:\n",concatenated)
grouped = merged.groupby("DeptName")
print("\nGROUPBY: Merged data grouped by 'Department':\n",grouped)
print("\nSum of Salary per Department:\n",grouped["Salary"].sum())
print("\nMean Salary per Department:\n",grouped["Salary"].mean())
print("\nCount of Employees per Department:\n",grouped["Name"].count())
print("\nMin and Max Salary per Department:\n",grouped["Salary"].agg(["min", "max"]))
print("\nMultiple aggregations at once:\n")
print(grouped["Salary"].agg(["sum", "mean", "count", "min", "max"]))
print("\nPIVOT TABLE: Average Salary by Department and Location")
pivot = pd.pivot_table(
    merged,
    values="Salary",
    index="DeptName",
    columns="Location",
    aggfunc="mean",
    fill_value=0)
print("\n",pivot)
print("\nPIVOT TABLE: Multiple aggregations (sum and count) Salary by Department")
pivot2 = pd.pivot_table(
    merged,
    values="Salary",
    index="DeptName",
    aggfunc=["sum", "mean", "count"])
print("\n",pivot2)

print("\n","#" * 70)
print("Task 9: Exporting Data")
print("#" * 70,"\n")
#Task 9: Exporting Data
em.to_csv("employees.csv", index=False)
print("\nSuccessfully Saved employees.csv",)
merged.to_csv("merged_employees_departments.csv", index=False)
print("\nmerged_employees_departments.csv")


print("\n","#" * 70)
print("Task 10: Mini Data Analysis Project")
print("#" * 70,"\n")
#Task 10: Mini Data Analysis Project
print("\n","#" * 70)
print("1. LOADING THE DATASET")
print("#" * 70,"\n")
# 1. LOADING THE DATASET
import pandas as pd
st = pd.read_csv("student_performance.csv")
print("\nStudent Performance Dataset:\n",st)

print("\n","#" * 70)
print("2. DATA INSPECTION")
print("#" * 70,"\n")
# 2. DATA INSPECTION
print("\nHead of the first 5 rows:\n",st.head(5))
print("\nTail of the last 5 rows:\n",st.tail(5))
print("\nAll columns in the datasets:\n",st.columns.tolist())
print("\nStatistical info in the datasets:\n",st.describe(include="all"))
print("\nInformation about the datasets:\n",st.info())
print("\nNo.of.rows & columns in the datasets:\n",st.shape)
print("\nDatatypes of the column in the datasets:\n",st.dtypes)

print("\n","#" * 70)
print(" 3. IDENTIFYING AND HANDLING MISSING VALUES")
print("#" * 70,"\n")
# 3. IDENTIFYING AND HANDLING MISSING VALUES
print("\nNull values in the datasets:\n",st.isnull().sum())
print("\nNull values in rows of the datasets:\n",st.isnull().any(axis=1))
for subject in ["Math", "Science", "English"]:
  fill = st[subject].median()
  st[subject]=st[subject].fillna(fill)
  print(f"\nFilled missing '{subject}' values with median: {fill}")
print("\nMissing values per column (after cleaning):\n",st.isnull().sum())

print("\n","#" * 70)
print("4. SELECTING AND FILTERING DATA")
print("#" * 70,"\n")
# 4. SELECTING AND FILTERING DATA
print("\n3rd row:\n",st.loc[2])
print("\n1st column:\n",st.iloc[:,0])
High = st[st["Attendance"]>=90]
print("\nStudents who scored >= 90 in Attendance:\n",High[["Name","Class","Attendance"]])
Highest = st[(st["Science"]>=90) & (st["Math"]>=90)  & (st["English"]>=90)]
print("\nStudents who scored >= 90 in Science, Math, and English:\n",Highest[["Name","Class","Science","English","Math","Attendance"]])

print("\n","#" * 70)
print("5. SORTING DATA")
print("#" * 70,"\n")
# 5. SORTING DATA
so = st.sort_values(by="Attendance",ascending=False)
print(so[["Name","Attendance"]])

print("\n","#" * 70)
print("6. GROUPBY ANALYSIS")
print("#" * 70,"\n")
# 6. GROUPBY ANALYSIS
gf = st.groupby("Class")
print(gf)
print("\n",gf[["Math","Science","English"]].mean().round(0))
print("\n",gf["Name"].count())
print("\n",gf[["Math","Science","English"]].agg(["min","max"]))

print("\n","#" * 70)
print(" 7. PIVOT TABLE")
print("#" * 70,"\n")
# 7. PIVOT TABLE
pivot = pd.pivot_table(st,
    values=["Math","Science","English"],
    index="City",
    columns="Class",
    aggfunc="mean")
print("\nPivot Table: Average of all subjects by City & Class:\n",pivot)

print("\n","#" * 70)
print("8. INSIGHTS")
print("#" * 70,"\n")
# 8. INSIGHTS
st["Average"] = st[["Math","Science","English"]].mean(axis=1).round(0)
print("Average of all three Subject",st["Average"])
top_student = st.loc[st["Average"].idxmax()]
fir_fiv = st.nlargest(5, "Average").round(0)
las_fiv = st.nsmallest(5, "Average").round(0)
lowest_student = st.loc[st["Average"].idxmin()]
best_class = st.groupby("Class")["Average"].mean().idxmax()
best_gen_avg = st.groupby("Gender")["Average"].mean().idxmax()
most_com_city = st["City"].mode()
overall_avg = st["Average"].mean()
attendance_corr = st["Attendance"].corr(st["Average"])
print("\n 1.Topest Student of the Class:\n",top_student)
print("\n 1.First 5 Topest Student of the Class:\n",fir_fiv)
print("\n 2.Lowest Student of the Class:\n",lowest_student)
print("\n 1.Last 5 Student of the Class:\n",las_fiv)
print("\n 3.Best Performing Class:\n",best_class)
print("\n 4.Average Score by Gender:\n",best_gen_avg)
print("\n 5.Most Common Student City:\n",most_com_city)
print("\n 6.Overall Class Average:\n",overall_avg)
print("\n 7.Correlation between Attendance and Average score:", round(attendance_corr,2))
if attendance_corr > 0.5:
    print("\n   -> Strong positive relationship: higher attendance tends to mean higher scores.")
elif attendance_corr > 0.2:
    print(" \n  -> Moderate positive relationship between attendance and scores.")
else:
    print("\n   -> Weak/no clear relationship between attendance and scores.")

print("\n","#" * 70)
print("9. EXPORTING THE CLEANED / PROCESSED DATASET")
print("#" * 70)
# 9. EXPORTING THE CLEANED / PROCESSED DATASET
output_file = "student_performance_cleaned.csv"
st.to_csv(output_file, index=False)
print("\nCleaned dataset exported to" ,output_file)
verify_df = pd.read_csv(output_file)
print(f"Verification - exported file shape: {verify_df.shape}")
print(f"Verification - missing values remaining: {verify_df.isnull().sum().sum()}")
print("\nFinal cleaned dataset preview:")
print(verify_df.head())

