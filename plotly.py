import plotly.express as px

# histogram
fig = px.histogram(df, x='col1')
# histogram with different colored data
fig = px.histogram(df, x="total_bill", color="sex")

# violin plot
fig = go.Figure()
for n,l in zip(names,lists):
    fig.add_trace(go.Violin(y=df['total_bill'][df['day'] == day],name=n,box_visible=True,meanline_visible=True))

# heatmap (matrix)
fig = px.imshow(arr)

# line plot
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')

# adding horizontal and vertical lines
fig.add_hline(y=1)
fig.add_vline(x=1)

# horizontal and vertical rectangle
fig.add_hrect(y0=0, y1=1, line_width=0, fillcolor="red", opacity=0.2)
fig.add_vrect(y0=0, y1=1, line_width=0, fillcolor="red", opacity=0.2)

# setting range of axes
fig.update_xaxes(range=[0,1])
fig.update_yaxes(range=[0,1])

# treating x as catogorical data
fig.update_layout(xaxis_type='category')

# background color
fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)')

# points (/traces) color
fig.update_traces(marker_color='rgba(255, 182, 193, .9)')

# using themes
fig.update_layout(template="simple_white") 


