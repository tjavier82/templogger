
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
	x  = df['date'],
	y = df['External Temperature'],
	mode = 'lines',
	name = 'External Temperature'
)

trace2 = go.Scatter(
	x  = df['date'],
	y = df['Internal Temperature'],
	mode='lines',
	name='Internal Temperature'
)


data = [trace1, trace2]
py.plot(data, filename='Temp evolution')