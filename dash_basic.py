import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

colors = {'background': '#111111',
          'text': '#7FDBFF'}

style_1 = {'textAlign': 'center',
           'color': colors['text']}

data_dict_1 = {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'}
data_dict_2 = {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'NYC'}
layout_dict = {
    'title': 'Bar Plot',
    'plot_bgcolor': colors['background'],
    'paper_bgcolor': colors['background'],
    'font': {'color': colors['text']},
}

app.layout = html.Div(children=[
    html.H1('Hello Dash', style={
            'textAlign': 'center', 'color': colors['text']}),
    html.Div('Dash environmnent', style=style_1),
    dcc.Graph(id='example',
              figure={'data': [data_dict_1, data_dict_2],
                      'layout': layout_dict})
], style={'backgroundColor': colors['background']})

if __name__ == '__main__':
    app.run_server()
