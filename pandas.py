import pandas as pd

df = pd.DataFrame()

# getting rows by their index
df.take([0,1,2,3])

# getting rows by their column value
## if column value is in this list
df[df['col1'].isin(mylist)]
## if column value -is not- in this list
df[~df['col1'].isin(mylist)]
## ranges (the point is to use & | operators instead of "and" , "or")
df[(df['col'] < 10) & (df['col'] > 1)]
df[(df['col'] > 10) | (df['col'] < 1)]


# sort values by column
df.sort_values(by=['col1'])

# adding a row to end of dataframe
df.loc[len(df)] = [value1,value2,value3]
