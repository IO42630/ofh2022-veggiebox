import json
import random
import util.arrUtil as arrUtil

import plotly.graph_objects as go
from dash import Dash

app = Dash(__name__)

veggies = json.load(open('./data/veggies.json')).get("veggies")
data = json.load(open('./data/data.json'))

vegRange = range(1, 39)      # do not count Verpackung
kwRange = range(1, 51)

fig = go.Figure()

xArr = []
for kw in kwRange:
    xArr.append("kw" + str(kw))

yArr = []
for veg in vegRange:
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


sums = []
for veg in vegRange:
    sums.append([])

for veg in vegRange:
    notNullArr = arrUtil.replace(yArr[veg-1], None, 0)
    sums[veg-1] = sum(notNullArr)

print(sums)



