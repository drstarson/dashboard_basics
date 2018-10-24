import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

# Creating Data

np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)

data_1 = [go.Scatter(
    x=random_x,
    y=random_y,
    mode='markers',
    marker={
        'size': 12,
        'color': 'rgb(51,204,153)',
        'symbol': 'circle',
        'line': {'width': 2}
    }
)]

layout_1 = go.Layout(title='My Plot',
                     xaxis={'title': 'My X Axis'}
                     )

graph_1 = dcc.Graph(id='scatterplot',
                    figure={'data': data_1,
                            'layout': layout_1})

graph_2 = dcc.Graph(id='scatterplot_0',
                    figure={'data': data_1,
                            'layout': layout_1})


app.layout = html.Div([
    graph_1,
    graph_2
])


if __name__ == '__main__':
    app.run_server()
