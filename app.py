# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
import json

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

app = Dash(__name__)

f = open('./data/data.json')
veggies = json.load(open('./data/veggies.json')).get("veggies")
data = json.load(f)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

kw1xl = data.get("1").get("xl")
df = pd.DataFrame({
    "veggies": veggies,
    "kw1xl": kw1xl
})

fig = px.bar(df, x="veggies", y="kw1xl")

app.layout = html.Div(children=[
    html.H1(children='Hello Veggie!'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
