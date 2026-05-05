import pandas as pd 

data = {
    "Name": ["aditya", "uday", "omkar", "omraj","sumit","chinu"],
    "Subject":["EDS", "DV", "C", "SIC","SE","AIML"],
    "Batch" : [1,2,3,4,5,6]
}
print(data)                        # output in tuple form

import pandas as pd
df = pd.DataFrame(data)
print(df)                          # output is in tabular form

shape = df.shape                                 # return a tuple containing the shape of DataFrame - row and columns
print(shape)                       # (6, 3)     (row,column)

dt = df.dtypes
print(dt)

dt = df.columns                                 # list of column in a dataframe
print(dt)                         # Index(['Name', 'Subject', 'Batch'], dtype='str')


print(df.head(2))                               # Top Row

print(df.tail(2))                               # last row

print(df.rename(columns = {'Name':'Student_Name'}))             # but not parmanent

print(df)           # column name is not change 

print("For parmenent")

df.rename(columns = {'Name':'Student_Name'},inplace=True)
print(df)             

# ___________________or___________________

df1 = df.rename(columns = {'Name':'Student_Name'})

print(df1)



df.info()                 # info method print information about the  dataframe

print(df.describe())      # describe method generates descriptive statistics of DataFrame, only for nummerical-value columns   
# gives min,mean,std,etc.

df.info()
df['Batch'] = pd.to_timedelta(df['Batch'])                # we can change Dtype

df.info()
# print(df)





