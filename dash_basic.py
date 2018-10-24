import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

data_dict_1 = {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'}
data_dict_2 = {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'NYC'}
layout_dict = {'title': 'Bar Plot'}

app.layout = html.Div(children=[
    html.H1('Hello Dash', style={'text-align': 'center'}),
    html.Div('Dash environmnent', style={'text-align': 'center'}),
    dcc.Graph(id='example',
              figure={'data': [data_dict_1, data_dict_2],
                      'layout': layout_dict})
])

if __name__ == '__main__':
    app.run_server()
