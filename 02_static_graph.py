import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv("./data/irish_property_data.csv")
df["year"] = df[df.columns[0]].str.slice(6,10,1).astype("int64")
df["date"] = df["Date of Sale (dd/mm/yyyy)"]
df2010 = df[df.year==2010]

app = dash.Dash(__name__)
app.layout = html.Div(children = [
    html.H1("Ben's Dash App on the Irish Property Market", style = {"text-align":"center"}),
    html.P("This is data from the irish property register, from 2010"),
    dcc.Graph(id = "my id", figure = {
              'data': [go.Scatter(
            x=df2010[df2010['County'] == "Clare"]['date'],
            y=df2010[df2010['County'] == "Clare"]['Price'],
            text= "Clare",
            mode='markers',
            marker={
                'size': 8,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={
                'title': 'date',
            },
            yaxis={
                'title': 'price',
                'type': 'log',
            },
            margin={'l': 80, 'b': 100, 't': 10, 'r': 0},
            hovermode='closest'
        )}

    )
])

if __name__ == "__main__":
    app.run_server(debug = True)
