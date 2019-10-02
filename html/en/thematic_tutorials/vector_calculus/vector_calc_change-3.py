E = EuclideanSpace(3)
cartesian = E.cartesian_coordinates()
spherical = E.spherical_coordinates()
x, y, z = cartesian[:]
r, th, ph = spherical[:]
g = spherical.plot(cartesian, fixed_coords={ph: 0}, ambient_coords=(x,z),
                   color={r:'red', th:'green', ph:'orange'})
sphinx_plot(g)