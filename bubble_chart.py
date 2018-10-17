import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('data/mpg.csv')
#print (df[['mpg', 'name']].head())

data = [go.Scatter(x=df['horsepower'],
                   y=df['mpg'],
                   text=df['name'],
                   mode='markers',
                   marker=dict(size=2*df['cylinders'],
                               color=df['weight'],
                               showscale=True))]


layout = go.Layout(title='Bubble Chart', hovermode='closest')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
