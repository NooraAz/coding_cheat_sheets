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

# sort by occurance of values in a column
df['Frequency'] = df.groupby('CompanyName')['CompanyName'].transform('count')
df.sort_values(['Frequency', 'CompanyName'], inplace=True, ascending=[False, True])

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

# group rows based on column name into average of those rows
df_mean = df.groupby('File name', as_index=False)['Energy'].mean()

# group into mean and std
df_result = df.groupby(['a'], as_index=False).agg({'c':['mean','std'],'b':'first', 'd':'first'})
df_result.columns = ['a','c-mean','c-std','b','d']
df_result.reindex(columns=sorted(df_result.columns))

# normalization
normalized_df=(df-df.min())/(df.max()-df.min()) #min-max
normalized_df=(df-df.mean())/df.std() #mean

# loc based on inclusion of a string
df.loc[df['A'].str.contains("PEP")]