import plotly.express as px

# histogram
fig = px.histogram(df, x='col1')
fig.show()

# adding horizontal and vertical lines
fig.add_hline(y=1)
fig.add_vline(x=1)

# setting range of axes
fig.update_xaxes(range=[0,1])
fig.update_yaxes(range=[0,1])

# treating x as catogorical data
fig.update_layout(xaxis_type='category')

# background color
fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)')

