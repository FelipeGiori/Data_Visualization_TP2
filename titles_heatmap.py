#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go

# Load data
games = pd.read_csv("data/vgsales.csv")

sales_df = games[['Genre', 'Platform', 'Global_Sales']]

# Counts the number os titles per game genre and game platform and transforms
# it into a matrix for the heatmap
Titles = games.groupby(['Genre', 'Platform']).size().unstack(fill_value=0)
Sales = sales_df.groupby(['Genre', 'Platform']).sum().unstack(fill_value=0)

# Extracts the labels for the legend
genres = list(Titles.index.values)
platforms = list(Titles.columns.values)

# Text of heatmap cells
annotations = go.Annotations()
for i, row in enumerate(Sales.values):
    for j, val in enumerate(row):
        annotations.append(go.Annotation(text=str(Sales.values[i][j]),
                                         x=platforms[j],
                                         y=genres[i],
                                         xref='x1',
                                         yref='y1',
                                         showarrow=False,
                                         font={'size':11, 'color':'white'} if Sales.values[i][j] < 250 else {'size':11, 'color':'black'}
        ))


# Hover text info. Numbers of titles produced
titles_info = Titles.values.astype(str)

for i, row in enumerate(Titles.values):
    for j, val in enumerate(row):
        titles_info[i][j] = "Number of titles: " + str(titles_info[i][j])

# Layout of the heatmap graph
layout = go.Layout(
            title='Millions of units of games sold per genre and platform',
            xaxis={'title':'Platform'},
            yaxis={'title':'Genre'},
            annotations=annotations,
            autosize=False,
            width=1400,
            height=900
)

# Creates the heapmap
trace = go.Heatmap(z=np.round(Sales.values, 2), x=platforms, y=genres, text=titles_info, colorscale='Viridis')

# Uploads the figure
data=[trace]
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='games_titles_heatmap')