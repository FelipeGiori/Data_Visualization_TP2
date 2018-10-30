#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

# Subset data
games = pd.read_csv("data/vgsales.csv")
games = games[['Name', 'Year']]
games = games.drop_duplicates()

Titles = games.groupby(['Year']).size()
Titles = Titles.reset_index()
Titles = Titles[:-2]
Titles.columns = ['Year', 'count']

year = Titles.Year.values
count = Titles['count'].values

# Create and style traces
trace = go.Scatter(
            x = year,
            y = count,
            name="# titles",
            line=dict(
                color='red',
                width=2
            )
)
            
data = [trace]

# Layout of the line chart
layout = go.Layout(
            title='Video game titles made by year',
            xaxis={'title':'Year', 'dtick':2},
            yaxis={'title':'Number of game titles'},
            autosize=False,
            width=1200,
            height=600
)

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='games_titles_linechart')