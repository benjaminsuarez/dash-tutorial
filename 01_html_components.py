import dash
import dash_html_components as html


app = dash.Dash("__name__")

app.layout = html.Div([
    html.H1("Hello World !!!",
            style = {
                "backgroundColor" : "rgb(250, 250, 250)",
                "borderBottom" : "thin lightgrey solid",
                "textAlign" : "center",
#                "border" : "1px solid black",
            }),
    html.H3("You can tune the look and feel of your dash apps using html components.")
])

if __name__ == "__main__":
    app.run_server(debug = True)
