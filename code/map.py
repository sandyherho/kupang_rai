'''
map.py

PyGMT Mapping script
Sandy H. S. Herho <herho@umd.edu>
2021/10/24
'''

import pygmt
grid = pygmt.datasets.load_earth_relief(resolution="03s", region=[122.5, 127.9, -11.5, -8])

x = 123.671
y = -10.1716

fig = pygmt.Figure()
fig.grdimage(grid=grid, projection="M15c", frame="a", cmap="geo")
fig.colorbar(frame=["a1000", "x+lElevation", "y+lm"])
fig.plot(x, y, style="i0.5c", color="red")
fig.savefig('../figs/fig1.png')
