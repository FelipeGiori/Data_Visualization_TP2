#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

# Load data
games = pd.read_csv("data/vgsales.csv")

# Counts the number os titles per game genre and game platform and transforms
# it into a matrix for the heatmap
Titles = games.groupby(['Genre', 'Platform']).size().unstack(fill_value=0)

# Extracts the labels for the legend
genres = list(Titles.index.values)
platforms = list(Titles.columns.values)

trace = go.Heatmap(z=Titles.values, x=platforms, y=genres)

data=[trace]
py.iplot(data, filename='labelled-heatmap')