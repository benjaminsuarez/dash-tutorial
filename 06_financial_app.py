import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

import pandas as pd
import plotly.graph_objs as go

app = dash.Dash("__name__")

app.layout = html.Div([
    html.H1("Financial Advice Application by Ben",),
    html.Div([
        html.P("Select yearly savings"),
        dcc.Input(
            id="savings_py",
            type='number',
            value= 0)
    ]),
    html.Div([
        html.P("Starting amount"),
        dcc.Input(
            name = "test name",
            id="savings_input",
            type='number',
            value = 20000)
    ]),
    html.Div([
        html.P("ROI"),
        dcc.Input(
            id='ROI',
            type='number',
            value= 5),
    ]),
    html.Div(html.P("" , id='output-1')),
    dcc.Graph(id='line-plot'),
    dcc.Slider(
        id='year-slider',
        min= 0,
        max= 31,
        value= 20,
        marks={str(year): str(year) for year in range(30)},
        step=None)

   ])

@app.callback(
    Output('output-1', 'children'),
    [Input('savings_input', 'value'),
     Input('ROI', 'value')])
def update_output(input1,input2):
    return 'Starting amount is "{}" with a return on investment (ROI) of {}%'.format(input1, input2)
@app.callback(
    Output('line-plot', 'figure'),
    [Input('savings_input', 'value'),
     Input('ROI', 'value'),
     Input('year-slider', 'value'),
     Input('savings_py', 'value')
    ])
def update_output(start,roi, years, save):
    a = [start]
    for x in range(years):
        passive = roi/100 * start + save
        start = start + passive
        a.append(start)
    
    return {
        'data': [go.Scatter(
            x= list(range(years)),
            y= a,
            text= "my text",
            mode= 'lines+markers'
        )],
        'layout': go.Layout(
            xaxis = {'title':'time'},
            yaxis = {'title':'euros'},
            title = 'Financial progress'
        )
    }


if __name__ == "__main__":
    app.run_server(debug = True)

# PYTHON Financial application.
# features:
# inputs: savings per year, financial freedom goal, ROI (yearly)
# outputs: scatter/line plot, years to financial freedom.
# qtabs!!

col_names = ['A', 'B', 'C']
df = pd.DataFrame(columns = col_names)
