import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json

app = dash.Dash()
df = pd.read_csv('data/wheels.csv')

wheels_figure = {
    'data': [go.Scatter(
        x=df['color'],
        y=df['wheels'],
        dy=1,
        mode='markers',
        marker={'size': 12, 'color': 'blue', 'line': {'width': 2}}
    )],
    'layout': go.Layout(
        title='Wheels',
        xaxis={'title': 'Color'},
        yaxis={'title': 'Wheels', 'nticks': 3},
        hovermode='closest'
    )
}

app.layout = html.Div([
    html.Div([
        dcc.Graph(
            id='wheels-plot',
            figure=wheels_figure
        )
    ], style={'width': '30%', 'display': 'inline-block'}),

    html.Div([
        html.Pre(id='selection', style={'paddingTop': 25})
    ], style={'width': '30%', 'display': 'inline-block', 'verticalAlign': 'top'})
])


@app.callback(
    Output('selection', 'children'),
    [Input('wheels-plot', 'selectedData')]
)
def callback_image(selectedData):
    return json.dumps(selectedData, indent=2)


if __name__ == '__main__':
    app.run_server()
