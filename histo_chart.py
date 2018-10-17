import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('data/mpg.csv')
print(df.head())

trace = go.Histogram(x=df['mpg'],
                     xbins=dict(start=0, end=50, size=2))

data = [trace]

layout = go.Layout(title='Histo')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
