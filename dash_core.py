import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Label('Dropdown'),
    html.Br(),
    html.Br(),
    dcc.Dropdown(options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'San Francisco', 'value': 'SF'},
    ],
        value='SF'),

    html.Br(),
    html.Label('Slider'),
    html.Br(),
    html.Br(),

    dcc.Slider(min=-10, max=10, step=0.5, value=0,
               marks={i: i for i in range(-10, 10)}),

    html.Br(),
    html.P(html.Label('Radio Buttons')),

    dcc.RadioItems(options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'San Francisco', 'value': 'SF'},
        {'label': 'Los Angeles', 'value': 'LA'},
    ],
        value='SF',
        labelStyle={'display': 'inline-flex'}
    )

])

if __name__ == '__main__':
    app.run_server()
