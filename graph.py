# libraries
import matplotlib.pyplot as plt
import numpy as np
# https://python-graph-gallery.com/line-chart/

# create data
values = np.cumsum(np.random.randn(1000, 1))

# use the plot function
plt.plot(values)
plt.show()
