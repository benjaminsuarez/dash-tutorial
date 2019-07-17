import dash
import dash_html_components as html


app = dash.Dash("__name__")

app.layout = html.Div(
    html.H1("Financial advice application",)
    )

if __name__ == "__main__":
    app.run_server(debug = True)

# PYTHON Financial application.
# features:
# inputs: savings per year, financial freedom goal, ROI (yearly)
# outputs: scatter/line plot, years to financial freedom.
# tabs!!
