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


fig = go.Figure()
xArr = []

for kw in range(1, 51):
    xArr.append("kw" +str(kw))


yArr = []
for veg in range(0, 40):
    yArr.append([])

for kw in range(1, 51):
    for veg in range(1, 40):
        kwArr = data.get(str(kw)).get("xl")
        if kwArr:
            val = kwArr[veg-1]
            if val == 0:
                val = None
            yArr[veg].append(val)


fig = go.Figure()


for veg in range(1, 39):
    hexadecimal = "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    fig.add_trace(go.Scatter(
        x=xArr,
        y=yArr[veg],
        name=veggies[veg],
        line=dict(color=hexadecimal)
    ))

# for veg in range(1,39):
#     hexadecimal = "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])
#     fig.add_trace(go.Scatter(
#         x=xArr,
#         y=yArr[veg],
#         name=veggies[veg],
#         mode="markers",
#         marker=dict(color=hexadecimal)
#     ))


# Edit the layout

fig.show()
