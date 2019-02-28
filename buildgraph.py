
# Simple test to learn plotly 

import plotly.plotly as py
import plotly.graph_objs as go


import numpy as np
import pandas as pd

df = pd.read_csv(
	'temp.csv', header=None, parse_dates=[1],
	 names=('date','Internal Humidity', 'Internal Temperature','External Humidity', 'External Temperature'),
	 delimiter=";")

trace1 = go.Scatter(
	x=df['date'],
	y=df['External Temperature'],
	mode = 'lines',
	name = 'External Temperature',
	line = dict(shape='spline', simplify=True)
)

trace2 = go.Scatter(
	x  = df['date'],
	y = df['Internal Temperature'],
	mode='lines',
	name='Internal Temperature',
	line = dict(shape='spline', simplify=True)
)

trace3 = go.Scatter(
	x=df['date'],
	y=df['External Humidity'],
	mode = 'lines',
	name = 'External Humidity',
	yaxis='y2',
	line = dict(shape='spline', simplify=True)
)

trace4 = go.Scatter(
	x  = df['date'],
	y = df['Internal Humidity'],
	mode='lines',
	name='Internal Humidity',
	yaxis='y2',
	line = dict(shape='spline', simplify=True)
)


data = [trace1, trace2, trace3, trace4]

layout = go.Layout(
    title='Temperature and Humidity inside and outside',
    yaxis=dict(
        title='Temperature'
    ),
    yaxis2=dict(
        title='Humidity',
        titlefont=dict(
            color='rgb(148, 103, 189)'
        ),
        tickfont=dict(
            color='rgb(148, 103, 189)'
        ),
        overlaying='y',
        side='right'
    )
)

fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='Temperatura and Humidity')


