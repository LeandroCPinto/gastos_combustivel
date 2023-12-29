# https://github.com/lolipopshock/notion-df
#!pip3 install notion-df
#!pip install --upgrade pip
#!pip install -U kaleido

import notion_df
import datetime
from datetime import timedelta
import numpy as np 
import pandas as pd 
import plotly.express as px
from kaleido.scopes.plotly import PlotlyScope
from dash import Dash, dcc, html, Input, Output

scope = PlotlyScope(
    plotlyjs="https://cdn.plot.ly/plotly-latest.min.js",
    # plotlyjs="/path/to/local/plotly.js",
)

server = app.server 

notion_database_url = "https://www.notion.so/leandroconp/6f555d9ed8224fba9fbf8755a453b47b?v=e282f57e9d394e59a2a2eaf9f7ec8b11"
api_key = "secret_vOnrTV4HJQCTuG9OadpiHeOT4tIVQFdx55kAcAZ8jXm"

df = notion_df.download(notion_database_url, api_key=api_key)
# Equivalent to: df = pd.read_notion(notion_database_url, api_key=api_key)
# df.head()
df.sort_values(by=['Data'], inplace=True)
print(df)

fig = px.bar(df, x='Nome', y='Consumo (km/L)',
            hover_data={"Data": "%d-%m"},
            title='Consumo de Combustível',text="Posto", color="Posto", color_discrete_sequence=px.colors.qualitative.Plotly)

fig.update_layout(
    barmode='stack',
    yaxis={'title': 'Consumo (km/L)'},
    xaxis={
        'tickformat': '%d-%m',
        'type': 'category',
        'title': 'Dia',
    },
)

fig.update_xaxes(ticks= "outside",
                 ticklabelmode= "period", 
                 tickcolor= "black", 
                 ticklen=10)
