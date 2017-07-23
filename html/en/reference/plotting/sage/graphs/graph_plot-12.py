pos = {0:[0.0, 1.5], 1:[-0.8, 0.3], 2:[-0.6, -0.8],
    3:[0.6, -0.8], 4:[0.8, 0.3]}
g = Graph({0:[1], 1:[2], 2:[3], 3:[4], 4:[0]})
P = g.graphplot(pos=pos, layout='spring', iterations=0).plot()
sphinx_plot(P)