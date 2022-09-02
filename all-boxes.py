# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import json
import random

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, html, dcc

app = Dash(__name__)

f = open('./data/data.json')
veggies = json.load(open('./data/veggies.json')).get("veggies")
data = json.load(f)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

fig = go.Figure()
yArr = []

for kw in range(1,51):
    hexadecimal = "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    yVal = data.get(str(kw)).get("xl");
    yArr.append(yVal)
    fig.add_trace(go.Bar(
        x=veggies,
        y=yVal,
        name="kw" + str(kw) + "xl",
        marker_color= hexadecimal
    ))




fig.update_layout(barmode='group')
fig.update_yaxes()

app.layout = html.Div(children=[

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
