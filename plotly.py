import plotly.express as px

# histogram
fig = px.histogram(df, x='col1')
fig.show()
