# with open("file.txt") as file: 
#     data = file.read()

#pandas
#Pandas is a Python library used for working with data set
import pandas as pd
df = pd.read_csv('data.csv')
print(df)
print(df['name'])
print(df['name'].tolist())
print("__________________")
print(df.head(5))
print("__________________")
print(df.drop(0))
print("__________________")

mydataset = {'sub': ["python", "c", "maths"],'marks': [30, 17, 20]}
myvar = pd.DataFrame(mydataset)
print(myvar)
dept = ['CS','DS','IoT']
df['dept'] = dept
print("\nNew DataFrame after inserting the 'dept' column")
print(df)
print("__________________")
#A Pandas Series is like a column in a table.
#It is a one-dimensional array holding data of any type.
a = [1, 7, 2]
s = pd.Series(a)
print(s)
print("__________________")
#Create own labels
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
print("__________________")
stu_det = {"s1": 42.0, "s2": 38.0, "s3": 39.0}
stu = pd.Series(stu_det)
print(stu)
print("__________________")
#Pandas use the loc attribute to return one or more specified row(s)

print(df.loc[0])
print("__________________")
print(df.loc[[0, 1]])
print("-----------------------")

data = [{'area': 'new-hills', 'rainfall': 100, 'temperature': 20},
		{'area': 'cape-town', 'rainfall': 70, 'temperature': 25},
		{'area': 'mumbai', 'rainfall': 200, 'temperature': 39 }]

df = pd.DataFrame.from_dict(data)
print(df)

#Read JSON
import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409.1,
    "1":479.0,
    "2":340.0,
    "3":282.4,
    "4":406.0,
    "5":300.5
  }
}

df = pd.DataFrame(data)
print(df) 
print("__________________")
df = pd.read_json('data.json')
print(df.to_string()) 
#Print the first 5 rows of the DataFrame
print(df.head())

print("__________________")
#Print the last 5 rows of the DataFrame
print(df.tail())
print(df.info()) 


df = pd.read_csv('sample.csv')
print(df)

#remove rows that contain empty cells
#dropna() method returns a new DataFrame, and will not change the original.
new_df = df.dropna()
print(new_df.to_string())
#saving the dataframe to csv file
df.to_csv('file1.csv')

#If we want to change the original DataFrame, use the inplace = True argument
#df.dropna(inplace = True)
#print(df.to_string())

#Replace Empty Values
#fillna() method allows us to replace empty cells with a value
df.fillna(1000, inplace = True)

#Replace Only For Specified Columns
df["Calories"].fillna(130, inplace = True)

#Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column
df = pd.read_csv('sample.csv')
x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)

#Calculate the MEDIAN, and replace any empty values with it:
df = pd.read_csv('sample.csv')
x = df["Calories"].median()

df["Calories"].fillna(x, inplace = True)

#Replacing Values
df.loc[7, 'Duration'] = 45

#If the value is higher than 120, set it to 120:
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120

#Removing Rows
#Another way of handling wrong data is to remove the rows that contains wrong data.
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)

print("------------------------")

  
# create a dictionary with five fields each
data = {
    'A':['A1', 'A2', 'A3', 'A4', 'A5'], 
    'B':['B1', 'B2', 'B3', 'B4', 'B5'], 
    'C':['C1', 'C2', 'C3', 'C4', 'C5'], 
    'D':['D1', 'D2', 'D3', 'D4', 'D5'], 
    'E':['E1', 'E2', 'E3', 'E4', 'E5'] }
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
  
print(df)
df.drop(['A'], axis = 1, inplace = True)
print(df)

df.drop(['C', 'D'], axis = 1,inplace = True)
print(df)


data = {
    'A':['A1', 'A2', 'A3', 'A4', 'A5'], 
    'B':['B1', 'B2', 'B3', 'B4', 'B5'], 
    'C':['C1', 'C2', 'C3', 'C4', 'C5'], 
    'D':['D1', 'D2', 'D3', 'D4', 'D5'], 
    'E':['E1', 'E2', 'E3', 'E4', 'E5'] }
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
df.to_csv('data1.csv', sep=',', index=False,header=True)  
# Remove all columns between column index 1 to 3
df.drop(df.iloc[:, 1:3], inplace = True, axis = 1)
print(df)

data = {
    'A':['A1', 'A2', 'A3', 'A4', 'A5'], 
    'B':['B1', 'B2', 'B3', 'B4', 'B5'], 
    'C':['C1', 'C2', 'C3', 'C4', 'C5'], 
    'D':['D1', 'D2', 'D3', 'D4', 'D5'], 
    'E':['E1', 'E2', 'E3', 'E4', 'E5'] }
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data)
for col in df.columns:
    if 'A' in col:
        del df[col]
  
print(df)
import csv

with open('newsample.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["SN", "Name", "Sub"])
    writer.writerow( [1, "Sri", "C"])
    writer.writerow([2, "Rama", "Maths"])
    writer.writerow([3, "Devi", "Python Programming"])




#If you need to write the contents of the 2-dimensional list to a CSV file,
#writerows() function to write the content of the list to the CSV file.
row_list = [["SN", "Name", "Sub"],
             [1, "Sri", "C"],
             [2, "Rama", "Maths"],
             [3, "Devi", "Python Programming"]]
with open('filewriter.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(row_list)

a_file = open("sampledict.csv", "w")
a_dict = {"a": 1, "b": 2}

writer = csv.writer(a_file)
for key, value in a_dict.items():
    writer.writerow([key, value])

a_file.close()

#Dictionary to CSV using csv.DictWriter()
import csv
myheaders = ['Name','EID','DOMAIN']
myvalues = [
    {'EID': 8901, 'Name':'Akil', 'DOMAIN': 'SUP'},
    {'EID': 7812, 'DOMAIN': 'DB', 'Name':'John'},
    {'Name':'Zoya','EID': 8034, 'DOMAIN': 'SUP'},
    {'EID': 1233, 'Name':'Asha', 'DOMAIN': 'DEV'},
]
filename = 'employeedata1.csv'
with open(filename, 'w', newline='') as myfile:
    writer = csv.DictWriter(myfile, fieldnames=myheaders)
    writer.writeheader()
    writer.writerows(myvalues)


import json

dict = {"member #002":{"first name": "John", "last name": "Doe", "age": 34},
        "member #003":{"first name": "Elijah", "last name": "Baley", "age": 27},
        "member #001":{"first name": "Jane", "last name": "Doe", "age": 42}}

with open('datawriter.json', 'w') as fp:
    json.dump(dict, fp)
