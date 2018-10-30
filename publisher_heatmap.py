#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

# Load data
games = pd.read_csv("data/vgsales.csv")

# If a game was made for several platforms, makes sure that it has only one entry
games = games[['Name', 'Publisher', 'Genre']]
games = games.drop_duplicates()

# Gets the list of publishers that made over 100 games
publisher = games.Publisher.value_counts()
publisher = publisher.reset_index(name='Publisher')
publisher = publisher[publisher['Publisher'] > 100]
publisher_filter = list(publisher['index'].values)

# Filters the table for the publisher in the filtered list
games = games[games['Publisher'].isin(publisher_filter)]

# Counts the number of game titles per Publisher and genre to get a sense
# of what kind of publisher focus on what kind of game genre. Since there are
# over 500 publishers, we focused on publishers that made over 100 games
Titles = games.groupby(['Publisher', 'Genre']).size().unstack(fill_value=0)

publisher = list(Titles.index.values)
genre = list(Titles.columns.values)

annotations = go.Annotations()
for i, row in enumerate(Titles.values):
    for j, val in enumerate(row):
        annotations.append(go.Annotation(text=str(Titles.values[i][j]),
                                         x=genre[j],
                                         y=publisher[i],
                                         xref='x1',
                                         yref='y1',
                                         showarrow=False,
                                         font={'size':11, 'color':'white'} if Titles.values[i][j] < 150 else {'size':11, 'color':'black'}
        ))
        
        
layout = go.Layout(
            title='Number of game titles made by publisher and genre',
            xaxis={'title':'Genre'},
            yaxis=go.layout.YAxis(
                title="Publisher",
                automargin=True
            ),
            annotations=annotations,
            autosize=False,
            width=1400,
            height=900
)

trace = go.Heatmap(z=Titles.values, x=genre, y=publisher, colorscale='Viridis')

# Uploads the figure
data=[trace]
fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='games_publisher_heatmap')