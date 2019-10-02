E = EuclideanSpace(3)
x, y, z = E.default_chart()[:]
v = E.vector_field(-y, x, sin(x*y*z), name='v')
g = v.plot(fixed_coords={y: 1}, ambient_coords=(x,z), max_range=1.5,
           scale=0.25)
sphinx_plot(g)