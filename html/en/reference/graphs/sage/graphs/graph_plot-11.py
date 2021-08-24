D = DiGraph({0:[0,1], 1:[2], 2:[3]}, loops=True)
P = D.plot(edge_colors={(0, 1, 0): [(0, 1, None), (1, 2, None)],
                        (0, 0, 0): [(2, 3, None)]})
sphinx_plot(P)