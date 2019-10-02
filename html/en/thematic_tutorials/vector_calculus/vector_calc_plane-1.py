E = EuclideanSpace(2)
X = E.default_chart(); x, y = X[:]
v = E.vector_field(-y, x, name='v')
g = v.plot()
sphinx_plot(g)