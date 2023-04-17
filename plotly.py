import plotly.express as px

# histogram
fig = px.histogram(df, x='col1')
fig.show()

# treating x as catogorical data
fig.update_layout(xaxis_type='category')

# background color
fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)')
