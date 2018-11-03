import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import numpy as np
import pandas as pd

app = dash.Dash()

np.random.seed(10)

x1 = np.linspace(0.1, 5, 50)
x2 = np.linspace(5.1, 10, 50)
y = np.random.randint(0, 50, 50)

df_1 = pd.DataFrame({'x': x1, 'y': y})
df_2 = pd.DataFrame({'x': x1, 'y': y})
df_3 = pd.DataFrame({'x': x2, 'y': y})


df = pd.concat([df_1, df_2, df_3])

data_1 = [go.Scatter(
    x=df['x'],
    y=df['y'],
    mode='markers'
)]

layout_1 = go.Layout(title='ScatterPlot', hovermode='closest')

figure_1 = {'data': data_1, 'layout': layout_1}

graph_obj_1 = dcc.Graph(id='plot', figure=figure_1)

app.layout = html.Div([
    html.Div([graph_obj_1], style={'width': '30%', 'display': 'inline-block'}),
    html.Div([html.H1(id='density', style={'paddingTop': 25})], style={
             'width': '30%', 'display': 'inline-block', 'verticalAlign': 'top'})
])


@app.callback(Output('density', 'children'),
              [Input('plot', 'selectedData')])
def find_density(selectedData):
    pts = len(selectedData['points'])
    rng_or_lp = list(selectedData.keys())
    rng_or_lp.remove('points')
    max_x = max(selectedData[rng_or_lp[0]]['x'])
    min_x = min(selectedData[rng_or_lp[0]]['x'])
    max_y = max(selectedData[rng_or_lp[0]]['y'])
    min_y = min(selectedData[rng_or_lp[0]]['y'])
    area = (max_x - min_x)*(max_y - min_y)
    d = pts/area
    return 'Density: {:.2f}'.format(d)


if __name__ == '__main__':
    app.run_server()
