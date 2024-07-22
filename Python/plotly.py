import plotly.express as px
import plotly.graph_objects as go

# ------- histogram ----------
fig = px.histogram(df, x='col1')

# histogram with different colored data
fig = px.histogram(df, x="total_bill", color="sex")

# changing color of histogram bars
fig = px.histogram(df, x="total_bill", color="sex" ,color_discrete_sequence=['red','blue','indianred'])

# overlaying 
fig = px.histogram(df, x="total_bill", color="sex", barmode='overlay')

# set size of bins (not number of bins)
fig.update_traces(xbins_size=2)

# --------- violin plot ----------
fig = go.Figure()
for n,l in zip(names,lists):
    fig.add_trace(go.Violin(y=df['total_bill'][df['day'] == day],name=n,box_visible=True,meanline_visible=True))

# box plot
fig = px.box(df,y=df.columns)

# heatmap (matrix)
fig = px.imshow(arr)  # 0,0 on top left corner
fig = px.imshow(arr, origin='lower') # 0,0 on bottom left corner


# --------- Jitter plot ----------

fig = px.strip(df, x='day', y='tip')

#--------------- Scatter plot -------------
fig = px.scatter(df,x='age',y='performance')

# error bars
fig = px.scatter(df,x='age',y='performance',error_x="ex", error_y="ey")

# change marker size
fig.update_traces(marker=dict(size=4))


#--------------- Line plot -------------
'''
Note: Plotly line charts are implemented as connected scatterplots (see below), 
meaning that the points are plotted and connected with lines
in the order they are provided, with no automatic reordering.
'''
fig = px.line(df, x="year", y="lifeExp", title='Life expectancy in Canada')
# smoothen the line plot
fig = px.line(df, x="x", y="y",line_shape='spline' )
# showing points on line
fig = px.line(df, x="x", y="y",markers=True)


#--------------- Bar plot ---------
fig = px.bar(df, x='rmsd',y='score')

# not stacking (group barmode)
fig = px.bar(df, x="sex", y="total_bill",color='smoker', barmode='group')

# --------------

# sorting alphabetically
fig.update_xaxes(categoryorder='category ascending')

# Adding horizontal and vertical lines
fig.add_hline(y=1)
fig.add_vline(x=1)

# Adding diagonal line
fig.add_shape(type="line",x0=4, y0=0, x1=4, y1=10)

# horizontal and vertical rectangle
fig.add_hrect(y0=0, y1=1, line_width=0, fillcolor="red", opacity=0.2)
fig.add_vrect(y0=0, y1=1, line_width=0, fillcolor="red", opacity=0.2)

# adding rectangle 
# relative
fig.add_shape(type="rect",xref="x domain", yref="y domain",x0=0.6, x1=0.7, y0=0.8, y1=0.9,)
# absolute
fig.add_shape(type="rect",x0=0.6, x1=0.7, y0=0.8, y1=0.9,)

# setting range of axes
fig.update_xaxes(range=[0,1])
fig.update_yaxes(range=[0,1])

# UPDATE_LAYOUT
fig.update_layout(
    xaxis_type='category', #type of x-axis data ('linear' (numerical), 'category', 'date')

    log_x=True, #logarithmic axes
    log_y=True,
    
    title_text="this is a plot", #plot title
    title="Plot Title",
    xaxis_title="X Axis Title",
    yaxis_title="Y Axis Title",

    legend_title="Legend Title",
    showlegend=False,

    font=dict(family="Courier New, monospace",size=18,color="RebeccaPurple"),

    plot_bgcolor='rgba(0, 0, 0, 0)', #background color
    template="simple_white", # template ('ggplot2', 'seaborn', 'simple_white', 'plotly', 'plotly_white','plotly_dark', 'presentation', 'xgridoff', 'ygridoff', 'gridon', 'none')
    width=800, height=400 #plot size
)


# UPDATE_XAXIS
fig.update_xaxis(
    type='category' #type of x-axis data ('linear' (numerical), 'category', 'date')
)

#UPDATE_TRACES
fig.update_traces(
    marker_color='rgba(255, 182, 193, .9)' # points (/traces) color
)

 

# changing color of continuous bars
color_continuous_scale='Bluered_r'

# animating the plot
px.scatter(df, x="x", y="y", animation_frame="time", animation_group="group")

# overlapping plots on each other
fig1 = px.scatter()
fig2 = px.line()
fig3 = go.Figure(data=fig1.data + fig2.data)
fig3.show()

# saving the plot as an image
fig.write_image("figure.png")

#-------- Subplots -------------
#---seperate
from plotly.subplots import make_subplots

fig = make_subplots(rows=1, cols=2)
fig.add_trace(go.Scatter(x=X1, y=Y1,row=1, col=1))
fig.add_trace(go.Scatter(x=X2, y=Y2,row=1, col=2))
fig.show()

#---overlapped
fig = go.Figure()
   
fig.add_trace(go.Scatter(x=x, y=x,mode='markers')) #scatter plot
fig.add_trace(go.Scatter(x=x, y=y,mode='lines+markers')), #line with markers
fig.add_trace(go.Scatter(x=x, y=y,mode='lines',)) #line plot

fig.show()

#------------ go.Scatter -----------
#-- markers mode
go.Scatter(x=X,y=Y,
    mode='markers',
    marker=dict(
        size=sizemap,
        color=colormap # If you want to set the colors, you can input colors as elements of the color map
    )
          )
                         
#-- line mode
go.Scatter(x=X,y=Y,
    mode='line',
    line=dict(
        color="#ffe476"
    )
          )

                    
#-- trendline
## removind scatter dots after applying trendline
fig.update_traces(visible=False, selector=dict(mode="markers"))
