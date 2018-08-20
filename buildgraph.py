
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF

import numpy as np
import pandas as pd

df = pd.read_csv('temp.csv', header=None, parse_dates=[1], names=('date','temp'), delimiter=";")

sample_data_table = FF.create_table(df)
#py.plot(sample_data_table, filename='sample-data-table')

trace1 = go.Scatter(
                    x=df['date'], y=df['temp'], # Data
                    mode='lines', name='temp' # Additional options
					)
layout = go.Layout(title='Simple Plot from csv data',
                   plot_bgcolor='rgb(230, 230,230)')
				   
fig = go.Figure(data=[trace1], layout=layout)
py.plot(fig, filename='temp_csv')