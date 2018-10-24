import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/OldFaithful.csv')

# Create plotly data trace and data object

trace_1 = go.Scatter(x=df['X'],
                     y=df['Y'],
                     mode='markers')

data_1 = [trace_1]

# Create plotly layout

layout_1 = go.Layout(title='Old Faithful')


# Launch the app
app = dash.Dash()

# Create a Graph
graph_1 = dcc.Graph(id='old_faithful',
                    figure={'data': data_1,
                            'layout': layout_1})

# Create a Dash layout
app.layout = html.Div([graph_1])

if __name__ == '__main__':
    app.run_server()
