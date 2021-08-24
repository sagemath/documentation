g = Graph({0: [1, 2], 2: [3], 4: [0, 1]})
g.graphplot(save_pos=True, layout='circular')  # indirect doctest
T = list(graphs.trees(7))
t = T[3]
P = t.plot(heights={0: [0], 1: [4, 5, 1], 2: [2], 3: [3, 6]})
sphinx_plot(P)