T = list(graphs.trees(7))
t = T[3]
sphinx_plot(t.graphplot(heights={0: [0], 1: [4, 5, 1],
                                 2: [2], 3: [3, 6]}))