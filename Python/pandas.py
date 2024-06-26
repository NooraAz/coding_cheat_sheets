import pandas as pd

# ---- Reading file -----

# From excel
df = pd.read_excel('path_to_file.xlsx')

# From excel with multiple sheets
xls = pd.ExcelFile('path_to_file.xlsx')
df1 = pd.read_excel(xls, 'Sheet1')
df2 = pd.read_excel(xls, 'Sheet2')

df = pd.DataFrame()
df = pd.DataFrame.from_dict(data) # each item is a column
df = pd.DataFrame.from_dict(data, orient='index') # each item is a row

# getting rows by their index
df.take([0,1,2,3])
df.iloc[[4]]

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

# correlation between two columns

# removing rows
df = df.drop([0, 1])
# removing columns
df = df.drop(['col1', 'col2'], axis=1)
# removing rows with Nan value in a specific column
df = df[df['col1'].notna()]

# reset indices after removing rows or changing order
df.reset_index(inplace=True)

# printing all rows neatly 
with pd.option_context('display.max_rows', None, 'display.max_columns', None,'display.precision', 3):
    print(df)

# exporting dataframe to CSV file
df.to_csv('path/to/saving', index=False)

# set a row as column names
df.columns = df.iloc[1]
df = df.drop(df.index[1]) #(ensure there are no repetitive indices)

# heatmap
df_res.apply(pd.to_numeric).style.background_gradient(cmap='Viridis')
df.style.background_gradient(cmap ='viridis').set_properties(**{'font-size': '20px'}) 

# aggregating multiple columns together
df['new column'] = df[list_of_columns].agg(''.join, axis=1)