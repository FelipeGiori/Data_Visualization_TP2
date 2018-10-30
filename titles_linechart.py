#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

# Returns the number of titles produced per year given a platform
def titles_per_year_platform(df, platform):
    Titles = df[df['Platform'] == platform]
    Titles = Titles[['Name', 'Year']]
    Titles = Titles.groupby(['Year']).size()
    Titles = Titles.reset_index()
    Titles.columns = ['Year', platform]
    return Titles

# Subset data
games = pd.read_csv("data/vgsales.csv")

# Temporal series of titles produced for platform
Titles_DS = titles_per_year_platform(games, 'DS')
Titles_PS2 = titles_per_year_platform(games, 'PS2')
Titles_PS3 = titles_per_year_platform(games, 'PS3')
Titles_Wii = titles_per_year_platform(games, 'Wii')
Titles_X360 = titles_per_year_platform(games, 'X360')
Titles_PSP = titles_per_year_platform(games, 'PSP')
Titles_PS = titles_per_year_platform(games, 'PS')
Titles_PC = titles_per_year_platform(games, 'PC')
Titles_XB = titles_per_year_platform(games, 'XB')
Titles_PS4 = titles_per_year_platform(games, 'PS4')
Titles_XOne = titles_per_year_platform(games, 'XOne')
Titles_SNES = titles_per_year_platform(games, 'SNES')

games = games[['Name', 'Year']]
games = games.drop_duplicates()

Titles = games.groupby(['Year']).size()
Titles = Titles.reset_index()
Titles = Titles[:-2]
Titles.columns = ['Year', 'Total']

Titles = Titles.join(Titles_DS.set_index('Year'), on='Year')
Titles = Titles.join(Titles_PS2.set_index('Year'), on='Year')
Titles = Titles.join(Titles_PS3.set_index('Year'), on='Year')
Titles = Titles.join(Titles_Wii.set_index('Year'), on='Year')
Titles = Titles.join(Titles_X360.set_index('Year'), on='Year')
Titles = Titles.join(Titles_PSP.set_index('Year'), on='Year')
Titles = Titles.join(Titles_PS.set_index('Year'), on='Year')
Titles = Titles.join(Titles_PC.set_index('Year'), on='Year')
Titles = Titles.join(Titles_XB.set_index('Year'), on='Year')
Titles = Titles.join(Titles_PS4.set_index('Year'), on='Year')
Titles = Titles.join(Titles_XOne.set_index('Year'), on='Year')
Titles = Titles.join(Titles_SNES.set_index('Year'), on='Year')

Titles = Titles.fillna(0)

year = Titles.Year.values
platforms = list(Titles.columns[1:])

traces = []
for platform in platforms:
    
    # Create and style traces
    traces.append(go.Scatter(
                    x = year,
                    y = Titles[platform].values,
                    name=platform,
                    line=dict(width=2)
                )
    )
            
data = traces

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