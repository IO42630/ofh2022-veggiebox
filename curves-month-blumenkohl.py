import json
import random

import plotly.graph_objects as go
from dash import Dash

app = Dash(__name__)

veggies = json.load(open('./data/veggies.json')).get("veggies")
ernte = json.load(open('./data/veggies.json')).get("ernte")
data = json.load(open('./data/data.json'))

vegRange = range(2, 3)      # do not count Verpackung
kwRange = range(1, 51)

fig = go.Figure()

xArr = []
for kw in kwRange:
    xArr.append("kw" + str(kw))

yArr = []
for veg in range(0, 100):
    yArr.append([])

for kw in kwRange:
    for veg in vegRange:
        kwArr = data.get(str(kw)).get("xl")
        if kwArr:
            val = kwArr[veg-1]
            if val == 0:
                val = None
        else:
            val = None
        yArr[veg-1].append(val)


fig = go.Figure()




for veg in vegRange:
    hexadecimal = "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])
    fig.add_trace(go.Scatter(
        x=xArr,
        y=yArr[veg-1],
        name=veggies[veg-1],
        line=dict(color=hexadecimal)
    ))

    ernteArrMt = ernte[veg-1]
    ernteArrKw = []
    for er in ernteArrMt:
        for x in range(0, 4):
            if er != 0:
                ernteArrKw.append(er)
            else:
                ernteArrKw.append(None)


    ernteArrKw.append(None)
    ernteArrKw.append(None)




    hexadecimal = "#"+''.join([random.choice('ABCDEF0123456789') for i in range(6)])

    fig.add_trace(go.Scatter(
        x=xArr,
        y=ernteArrKw,
        name=veggies[veg-1] + "ernte",
        line=dict(color=hexadecimal)
    ))




fig.show()
