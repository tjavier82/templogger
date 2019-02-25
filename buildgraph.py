
# Simple test to learn plotly 

import plotly.plotly as py
import plotly.graph_objs as go


import numpy as np
import pandas as pd

df = pd.read_csv(
	'temp.csv', header=None, parse_dates=[1],
	 names=('date','Internal Humidity', 'Internal Temperature','External Humidity', 'External Temperature'),
	 delimiter=";")

trace = go.Scatter(
	x  = df['date']
	y1 = df['Internal Temperature']
	y2 = df['External Temperature']
)

data = [trace]
py.iplot(data, filename='Temp evolution')