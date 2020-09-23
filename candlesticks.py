# -*- coding: utf-8 -*-


#This program shows an interactive candlestick chart in Python

#Import libraies
import plotly.graph_objects as go
import pandas as pd

#store the data to a dataframe
df = pd.read_csv('AMZN.csv')

#Set the index
df = df.set_index(pd.DatetimeIndex(df['Date'].values))

#Show the data
df

#Create an interactive candlestick chart
figure = go.Figure(
    data = [
            go.Candlestick(
                x = df.index,
                low = df['Low'],
                high = df['High'],
                close = df['Close'],
                open = df['Open'],
                increasing_line_color = 'green',
                decreasing_line_color = 'red'
            )
    ]
)
#figure.update_layout(xaxis_rangeslider_visible = False)

figure.update_layout(
    title = 'Amazon Price',
    yaxis_title = 'Amazon Stock Price USD ($)',
    xaxis_title = 'TimeStamp'
)
figure.show()

