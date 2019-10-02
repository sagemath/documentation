E = EuclideanSpace(3)
x, y, z = E.default_chart()[:]
v = E.vector_field(-y, x, sin(x*y*z), name='v')
sphinx_plot(v.plot(max_range=1.5, scale=0.5))