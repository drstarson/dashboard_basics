import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

import plotly.offline as pyo
import plotly.graph_objs as go


# US Census Data
df0 = pd.read_csv('data/nst.csv')
# Grabbing New England States via DIVISION

df1 = df0[df0['DIVISION'] == '1']
# inplace = True modifies the DataFrame in place w/o creating a new object
df1.set_index('NAME', inplace=True)

list_of_pop_col = [col for col in df1.columns if col.startswith('POP')]
df1 = df1[list_of_pop_col]

traces = [go.Scatter(x=df1.columns,
                     y=df1.loc[name],
                     mode='lines+markers',
                     name=name) for name in df1.index]


data = traces

layout = go.Layout(
    title='Line Charts',
    xaxis=dict(
        autotick=True,
        autorange=True,
        showgrid=True,
        zeroline=True,
        showline=True,
        ticks='',
        showticklabels=True
    ),
    yaxis=dict(
        autotick=True,
        autorange=True,
        showgrid=True,
        zeroline=True,
        showline=True,
        ticks='outside',
        showticklabels=True
    )
)

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
