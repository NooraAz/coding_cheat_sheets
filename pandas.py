import pandas as pd

df = pd.DataFrame()

# getting rows by their index
df.take([0,1,2,3])

# sort values by column
df.sort_values(by=['col1'])
