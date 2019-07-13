import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv("./data/irish_property_data.csv")
df["year"] = df[df.columns[0]].str.slice(6,10,1).astype("int64")
df["date"] = df["Date of Sale (dd/mm/yyyy)"]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.H1('Irish Property Market Analysis'),
    html.Div([
        dcc.Dropdown(
            id='county_select',
            options=[{'label': i, 'value': i} for i in df.County.unique()],
            value='Clare'),
        dcc.RadioItems(
            id='axis_type',
            options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
            value='Log',
            labelStyle={'display': 'inline-block'})
    ],
        style={'width': '100%', 'display': 'inline-block', 'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)'
        }),
    html.Div(dcc.Graph(id='graph-with-slider')),
    html.Div(dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None),
             style = {'padding':'40px'})
])
                     
@app.callback(
    Output('graph-with-slider', 'figure'),
    [Input('year-slider', 'value'),
     Input('county_select', 'value'),
     Input('axis_type', 'value')])

def update_figure(selected_year, selected_county, axis):
    dff = df[df.year == selected_year]
    return {
        'data': [go.Scatter(
            x=dff[dff['County'] == selected_county]['date'],
            y=dff[dff['County'] == selected_county]['Price'],
            text= selected_county,
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
                'type': 'log' if axis == 'Log' else 'linear',
            },
            margin={'l': 80, 'b': 100, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }

if __name__ == '__main__':
    app.run_server(debug=True)
