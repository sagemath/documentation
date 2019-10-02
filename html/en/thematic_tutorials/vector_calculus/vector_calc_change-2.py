E = EuclideanSpace(3)
cartesian = E.cartesian_coordinates()
spherical = E.spherical_coordinates()
x, y, z = cartesian[:]
r, th, ph = spherical[:]
g = spherical.plot(cartesian, fixed_coords={th: pi/2}, ambient_coords=(x,y),
                   color={r:'red', th:'green', ph:'orange'})
sphinx_plot(g)