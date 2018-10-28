import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='number-in', value=1, style={'fontSize': 24}),
    html.H1(id='number-out')
])


@app.callback(Output('number-out', 'children'),
              [Input('number-in', 'value')])
def duplicate(number):
    return number


if __name__ == '__main__':
    app.run_server()
