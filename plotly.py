import plotly.express as px

# histogram
fig = px.histogram(df, x='col1')
# histogram with different colored data
fig = px.histogram(df, x="total_bill", color="sex")

# violin plot
fig = go.Figure()
for n,l in zip(names,lists):
    fig.add_trace(go.Violin(y=df['total_bill'][df['day'] == day],name=n,box_visible=True,meanline_visible=True))

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

# using themes
fig.update_layout(template="simple_white") 
