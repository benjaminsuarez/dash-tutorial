import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Dash Components"),
    html.P("Lets look at some 'Core components.'"),
    dcc.Dropdown(
        options=[
            {'label': 'Clare', 'value': 'CLR'},
            {'label': 'Cork', 'value': 'CRK'},
            {'label': 'Connemara', 'value': 'CN'},
            {'label': 'tinnahely', 'value': 'tn'}
        ],
        value='CLR'
    ),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: 'Level {}'.format(i) for i in range(10)},
        value=5),
    html.Div(dcc.RadioItems(
        options=[
            {'label': 'Lord of the Rings', 'value': 'LOTR'},
            {'label': 'Game of Thrones', 'value': 'GOT'},
            {'label': 'Peppa Pig', 'value': 'PP'}
        ],
        value='LOTR',
        labelStyle={'display': 'inline-block'}
    ), style = {"margin" : "50px 0px"})
    ])

if __name__ == '__main__':
    app.run_server(debug=True)
