E = EuclideanSpace(3)
cartesian = E.cartesian_coordinates()
spherical = E.spherical_coordinates()
r, th, ph = spherical[:]
g = spherical.plot(cartesian, color={r:'red', th:'green', ph:'orange'})
sphinx_plot(g)