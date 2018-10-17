import plotly.offline as pyo
import plotly.figure_factory as ff
import numpy as np

x1 = np.random.randn(200) - 2
x2 = np.random.randn(200) + 2

hist_data = [x1, x2]
group_labels = ['X1', 'X2']

fig = ff.create_distplot(hist_data, group_labels, bin_size=[0.1, 0.3])
pyo.plot(fig)
