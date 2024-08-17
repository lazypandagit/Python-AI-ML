import pandas as pd


# dictionary for data frame
dict_project: dict[str, list[str]] = {
    "Name": ["Rekha", "Divya", "Geet", "Jeet"],
    "Class": ["XII", "XII", "XII", "XII"],
    "Section": ["B", "C", "H", "B"],
    "Project Name": [
        "Data Analysis",
        "Graphical Analysis",
        "Machine Learning",
        "App Development",
    ],
}

project: pd.DataFrame = pd.DataFrame(dict_project,index=[i for i in range(101,105)])
print(f"Initial DataFrame:-\n{project}")

# inserting 2 new records
newRecords: dict[str, list[str]] = {
    "Name": ["Aniket", "Sayan"],
    "Class": ["XII", "XII"],
    "Section": ["E", "D"],
    "Project Name": ["Artificial Intelligence", "Internet of Things"],
}
project = pd.concat([project, pd.DataFrame(newRecords, index=[105,106])])
print(f"\nNew DataFrame:-\n{project}")

# insert a grade column
project.insert(
    loc=len(project.columns), column="Grade", value=[7,8,9,7,9,8]
)

print(f"\nDataFrame after adding column:-\n{project}")

#displaying names and sections
print(f"\nNames and Section:\n{project.loc[:,["Name", "Section"]]}")

#display records 101 and 102
print(f"\nRecords for 101 and 102:-\n{project.loc[[101,102]]}")

#inserting "school name" column after name
project.insert(
    loc= 1, column="School Name", value=['Kendriya Vidyalaya', "Army Public School", "Ramakrishna Mission", "Kalyani Public School", "Central School","Lady Braboun"]
)
print(f"\nDataFrame after adding column:-\n{project}")

#displaying 2nd and 3rd Record
print(f"\n2nd and 3rd Records:-\n{project.iloc[1:3]}")

#Replacing class and section of jeet
project.at[104, "Class"] = "XI"
project.at[104, "Section"] = "A"
print(f"\nAfter modification of Jeet's record:-\n{project}")

#Removing multiple columns
project = project.drop(["Project Name", "Section"], axis=1)
print(f"\nAfter Deleting columns from DataFrame:-\n{project}")
