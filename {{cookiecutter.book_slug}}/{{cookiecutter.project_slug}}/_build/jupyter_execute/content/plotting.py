# Embedding Plots in Jupyter Book

In {doc}`notebook` we saw how to include images (e.g., `.png` files) in a Jupyter Book, however, we can also directly embed plots generated from code in a Jupyter notebook.

Plots may be static (e.g., [matplotlib](https://matplotlib.org/), [seaborn](https://seaborn.pydata.org/)) or interactive (e.g., [altair](https://altair-viz.github.io/index.html), [plotly](https://plotly.com/python/), [bokeh](https://bokeh.org/)). A few example plots are shown below - see the official [Jupyter Book](https://jupyterbook.org/intro.html) documentation for more informatin on including plots in a Jupyter book.

```{note}
The code generating the plots below has been hidden but you can view it by clicking the "Click to show" button. Read more about hiding cell input and output [here](https://jupyterbook.org/interactive/hiding.html#hide-code-cell-content).
```

## Examples

First we generate 25 random data points for plotting. The head of the data is shown below, consisting of two features (`X1` and `X2`), one discrete response (`y`) and a temporal component (`Time`).

import numpy as np
import pandas as pd

np.random.seed(1)
pd.options.plotting.backend = "plotly"

df = pd.DataFrame({"X1": np.random.randint(1, 10, 25),
                   "X2": np.random.randint(1, 10, 25),
                   "y": np.random.choice(["Class 1", "Class 2", "Class 3"], 25),
                   "Time": np.random.randint(0, 4, 25)}).sort_values(by=["y", "Time"])
df.head()

Below is a scatter plot of our data using the plotly plotting library (through the [Pandas plotting backend](https://plotly.com/python/pandas-backend/)).

```{tip}
The plot below supports hover labels (try hovering your mouse over a data point) and clickable legend entries to hide/show data.
```

import plotly.io as pio
pio.renderers.default = "notebook"
fig = df.plot.scatter(x="X1", y="X2", color="y")
fig.update_layout(width=500, height=500)
fig.update_traces(marker={"size": 14})
fig.show()

Below, we introduce interaction into our figure by generating snapshots of our data based on the `Time` column.

fig = df.plot.scatter(x="X1", y="X2", color="y", animation_frame="Time")
fig.update_layout(width=500, height=500)
fig.update_traces(marker={"size": 14})
fig