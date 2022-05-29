# with open("file.txt") as file: 
#     data = file.read()

#pandas
#Pandas is a Python library used for working with data set
import pandas as pd
df = pd.read_csv('data.csv')
print(df)
'''
 rno     name  cgpa  dept
0    1      sri    76   cse
1    2     rama    91    ds
2    3  lakshmi    87   iot
'''
print("__________________")
print(df['name'])
'''
0        sri
1       rama
2    lakshmi

Name: name, dtype: object
'''
print("__________________")
print(df['name'].tolist())
'''
['sri', 'rama', 'lakshmi']
'''
print("__________________")
print(df.head(1))
'''
   rno name  cgpa dept
0    1  sri    76  cse
 
'''
print("__________________")
print(df.drop(0))
'''
   rno     name  cgpa dept
1    2     rama    91   ds
2    3  lakshmi    87  iot
 
'''
print("__________________")

mydataset = {'sub': ["python", "c", "maths"],'marks': [30, 17, 20]}
myvar = pd.DataFrame(mydataset)
print(myvar)
'''
      sub  marks
0  python     30
1       c     17
2   maths     20
'''
print("__________________")
dept = ['CS','DS','IoT']
df['dept'] = dept
'''
file beforerno,name,cgpa
1,sri,76
2,rama,91
3,lakshmi,87
file after
1,sri,76,'CS'
2,rama,91,'DS'
3,lakshmi,87,'IOT'
'''
print("\nNew DataFrame after inserting the 'dept' column")
print(df)
print("__________________")
#A Pandas Series is like a column in a table.
#It is a one-dimensional array holding data of any type.
a = [1, 7, 2]
s = pd.Series(a)
print(s)
'''
0    1
1    7
2    2
dtype: int64
'''
print("__________________")
#Create own labels
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
'''
x    1
y    7
z    2
dtype: int64
'''
print("__________________")
stu_det = {"s1": 42.0, "s2": 38.0, "s3": 39.0}
stu = pd.Series(stu_det)
print(stu)
'''
s1    42.0
s2    38.0
s3    39.0
dtype: float64
'''
print("__________________")
#Pandas use the loc attribute to return one or more specified row(s)

print(df.loc[0])
'''
rno       1
name    sri
cgpa     76
Name: 0, dtype: object
'''
print("__________________")
print(df.loc[[0, 1]])
'''
   rno  name  cgpa
0    1   sri    76
1    2  rama    91
'''
print("-----------------------")

data = [{'area': 'new-hills', 'rainfall': 100, 'temperature': 20},
		{'area': 'cape-town', 'rainfall': 70, 'temperature': 25},
		{'area': 'mumbai', 'rainfall': 200, 'temperature': 39 }]

df = pd.DataFrame.from_dict(data)
print(df)
'''
        area  rainfall  temperature
0  new-hills       100           20
1  cape-town        70           25
2     mumbai       200           39
'''

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
'''
   Duration  Pulse  Maxpulse  Calories
0        60    110       130     409.1
1        60    117       145     479.0
2        60    103       135     340.0
3        45    109       175     282.4
4        45    117       148     406.0
5        60    102       127     300.5
'''
print("__________________")
df = pd.read_json('data.json')
print(df.to_string()) 
'''
member #002 member #003 member #001
first name        John      Elijah        Jane
last name          Doe       Baley         Doe
age                 34          27          42
'''
#Print the first 5 rows of the DataFrame
print(df.head())
print("__________________")
#Print the last 5 rows of the DataFrame
print(df.tail())
print(df.info()) 
'''
<class 'pandas.core.frame.DataFrame'>
Index: 3 entries, first name to age
Data columns (total 3 columns):
 #   Column       Non-Null Count  Dtype 
---  ------       --------------  ----- 
 0   member #002  3 non-null      object
 1   member #003  3 non-null      object
 2   member #001  3 non-null      object
dtypes: object(3)
memory usage: 96.0+ bytes
'''
df = pd.read_csv('sample.csv')
print(df)

#remove rows that contain empty cells
#dropna() method returns a new DataFrame, and will not change the original.
new_df = df.dropna()
print(new_df.to_string())
'''
---------------
    BEFORE
---------------
    Duration  Pulse  Maxpulse  Calories
0         60    110       130     409.1
1         60    117       145     479.0
2         60    103       135     340.0
3         45    109       175     282.4
4         45    117       148     406.0
5         60    102       127     300.5
6         60    110       136     374.0
7         45    104       134     253.3
8         30    109       133     195.1
9         60     98       124     269.0
10        60    103       147     329.3
11        60    100       120     250.7
12        60    106       128     345.3
13        60    104       132     379.3
14        60     98       123     275.0
15        60     98       120     215.2
16        60    100       120     300.0
17        45     90       112       NaN
18        60    103       123     323.0
19        45     97       125     243.0
20        60    108       131     364.2
21        45    100       119     282.0
22        60    130       101     300.0
23        45    105       132     246.0
24        60    102       126     334.5
25        60    100       120     250.0
26        60     92       118     241.0
27        60    103       132       NaN
28        60    100       132     280.0
29        60    102       129     380.3
----------------
      AFTER
----------------
    Duration  Pulse  Maxpulse  Calories
0         60    110       130     409.1
1         60    117       145     479.0
2         60    103       135     340.0
3         45    109       175     282.4
4         45    117       148     406.0
5         60    102       127     300.5
6         60    110       136     374.0
7         45    104       134     253.3
8         30    109       133     195.1
9         60     98       124     269.0
10        60    103       147     329.3
11        60    100       120     250.7
12        60    106       128     345.3
13        60    104       132     379.3
14        60     98       123     275.0
15        60     98       120     215.2
16        60    100       120     300.0
18        60    103       123     323.0
19        45     97       125     243.0
20        60    108       131     364.2
21        45    100       119     282.0
22        60    130       101     300.0
23        45    105       132     246.0
24        60    102       126     334.5
25        60    100       120     250.0
26        60     92       118     241.0
28        60    100       132     280.0
29        60    102       129     380.3
30        60     92       115     243.0
31        45     90       112     180.1
-------------
'''
#saving the dataframe to csv file
df.to_csv('file1.csv')

#If we want to change the original DataFrame, use the inplace = True argument
df.dropna(inplace = True)
print(df.to_string())

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
