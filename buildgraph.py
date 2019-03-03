# Simple test to learn plotly

import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np
import pandas as pd
import logging
import configparser

CONFIG_PATH = "config.ini"
DATA_FILE = ""


class BuildGrapgh:

    def __init__(self, data_file=None):
        # Fields
        # data_file , data , logger

        config = configparser.ConfigParser()
        try:
            config.read(CONFIG_PATH)
        except:
            exit()

        self.logger = logging.getLogger(config['Logging']['LoggerName'] + '.BuildGraph')
        self.data = None
        if data_file is None:
            self.data_file = config['Output']['FilePath']
            self.logger.debug('No data file name provided. Getting from config file: ' + self.data_file)
        else:
            self.data_file = data_file
            self.logger.debug('Data file provided: ' + self.data_file)

        # Open file
        try:
            self.data = pd.read_csv(self.data_file, header=None, parse_dates=[1], delimiter=";",
                                    names=('date', 'Internal Humidity', 'Internal Temperature', 'External Humidity',
                                           'External Temperature')
                                    )
        except:
            self.logger.exception('Error opening ' + self.data_file)

        return

    def temperature(self):
        self.logger.debug('Starting temperature graphic')
        trace1 = go.Scatter (
            x=self.data['date'],
            y=self.data['External Temperature'],
            hoverinfo = 'x+y',
            mode='lines',
            name='External Temperature',
            line=dict(shape='spline', simplify=True)
        )
        trace2 = go.Scatter(
            x=self.data['date'],
            y=self.data['Internal Temperature'],
            hoverinfo='x+y',
            mode='lines',
            name='Internal Temperature',
            line=dict(shape='spline', simplify=True)
        )

        data = [trace1, trace2]
        layout = go.Layout(
            title='Temperature inside and outside',
            yaxis=dict(
                title='Temperature'
             )
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='Temperature')
        return

    def humidity(self):
        self.logger.debug('Starting humidity graphic')
        trace1 = go.Scatter (
            x=self.data['date'],
            y=self.data['External Humidity'],
            hoverinfo = 'x+y',
            mode='lines',
            name='External Humidity',
            line=dict(shape='spline', simplify=True)
        )
        trace2 = go.Scatter(
            x=self.data['date'],
            y=self.data['Internal Humidity'],
            hoverinfo='x+y',
            mode='lines',
            name='Internal Humidity',
            line=dict(shape='spline', simplify=True)
        )

        data = [trace1, trace2]
        layout = go.Layout(
            title='Humidity inside and outside',
            yaxis=dict(
                title='Humidity'
             )
        )
        fig = go.Figure(data=data, layout=layout)
        py.plot(fig, filename='Humidity')
        return



    def all_together(self):
        self.logger.debug('Starting all_together graphic')
        trace1 = go.Scatter(
            x=self.data['date'],
            y=self.data['External Temperature'],
            mode='lines',
            name='External Temperature',
            line=dict(shape='spline', simplify=True)
        )

        trace2 = go.Scatter(
            x=self.data['date'],
            y=self.data['Internal Temperature'],
            mode='lines',
            name='Internal Temperature',
            line=dict(shape='spline', simplify=True)
        )

        trace3 = go.Scatter(
            x=self.data['date'],
            y=self.data['External Humidity'],
            mode='lines',
            name='External Humidity',
            yaxis='y2',
            line=dict(shape='spline', simplify=True)
        )

        trace4 = go.Scatter(
            x=self.data['date'],
            y=self.data['Internal Humidity'],
            mode='lines',
            name='Internal Humidity',
            yaxis='y2',
            line=dict(shape='spline', simplify=True)
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
        return

def main():
    bf = BuildGrapgh()
    bf.temperature()
    bf.humidity()
    bf.all_together()
    return

if __name__ == "__main__":
    main()