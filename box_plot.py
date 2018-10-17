import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

# Just random data
# y = np.random.randint(1, 10, 10)

# Snodgrss vs Twain 3 letter words
snodgrass = [.209, .205, .196, .210, .202, .207, .224, .223, .220, .201]
twain = [.225, .262, .217, .240, .230, .229, .235, .217]


trace1 = go.Box(y=snodgrass,
                name='Snodgrass')

trace2 = go.Box(y=twain,
                name='Twain')


data = [trace1, trace2]

layout = go.Layout(title='Bar Plot')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig)
