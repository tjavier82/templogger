
# Simple test to learn plotly 

import plotly.plotly as py
import plotly.graph_objs as go


import numpy as np
import pandas as pd

df = pd.read_csv(
	'temp.csv', header=None, parse_dates=[1],
	 names=('date','Internal Humidity', 'Internal Temperature','External Humidity', 'External Temperature'),
	 delimiter=";")

#sample_data_table = FF.create_table(df)
#py.plot(sample_data_table, filename='sample-data-table')

# #trace1 = go.Scatter(
                    # x=df['date'], y=df['temp'], # Data
                    # mode='lines', name='temp' # Additional options
					# )
#layout = go.Layout(title='Simple Plot from csv data',
                  # plot_bgcolor='rgb(230, 230,230)')
				   
				 
#fig = go.Figure(data=[trace1], layout=layout)
#py.plot(fig, filename='temp_csv') 

data = [go.Scatter(
			x=df['date'],
			y1=df['Internal Temperature'],
			y2=df['External Temperature'],
			name = 'Temperature',
			mode = 'lines',
			hoverinfo = "x+y",
			connectgaps = True,
			line = dict (
				#color = ('rgb(205, 12, 24)'),
				#width = 4,
				#dash = 'dash',
				shape = 'spline')
				
		)]	

# Edit the layout
layout = dict(title = 'Temperature from Arduino sensor',
              xaxis = dict(title = 'Time'),
              yaxis = dict(title = 'Temperature (degrees C)'),
              )		

fig = dict(data=data, layout=layout)
py.plot(fig, filename='temp')