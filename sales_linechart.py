#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go\

# Subset sales
games = pd.read_csv("data/vgsales.csv")
games = games[['Year', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']]
Sales = games.groupby(['Year']).sum()
Sales = Sales.reset_index()
Sales = Sales[:-2]

# Vector for each line
year = Sales.Year.values
na_sales = Sales.NA_Sales.values
jp_sales = Sales.JP_Sales.values
eu_sales = Sales.EU_Sales.values
other_sales = Sales.Other_Sales.values
global_sales = Sales.Global_Sales.values

# Create and style the lines
trace_na = go.Scatter(
            x = year,
            y = na_sales,
            name="North America Sales",
            line=dict(
                color='blue',
                width=2
            )
)
          
trace_jp = go.Scatter(
            x = year,
            y = jp_sales,
            name="Japan Sales",
            line=dict(
                color='red',
                width=2
            )
)
         
trace_eu = go.Scatter(
            x = year,
            y = eu_sales,
            name="Europe Sales",
            line=dict(
                color='green',
                width=2
            )
)

trace_other = go.Scatter(
            x = year,
            y = other_sales,
            name="Other Sales",
            line=dict(
                color='purple',
                width=2
            )
)
  
trace_global = go.Scatter(
            x = year,
            y = global_sales,
            name="Global Sales",
            line=dict(
                color='Gold',
                width=2
            )
)

# Join the lines
data = [trace_na, trace_jp, trace_eu, trace_other, trace_global]

# Plot layout
layout = go.Layout(
            title='Video games units sold by release year',
            xaxis={'title':'Year', 'dtick':2},
            yaxis={'title':'Number of units sold (Million)'},
            autosize=False,
            width=1200,
            height=600
)


fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='games_sales_linechart')