T = list(graphs.trees(7))
t = T[3]
t.set_edge_label(0, 1, -7)
t.set_edge_label(0, 5, 3)
t.set_edge_label(0, 5, 99)
t.set_edge_label(1, 2, 1000)
t.set_edge_label(3, 2, 'spam')
t.set_edge_label(2, 6, 3/2)
t.set_edge_label(0, 4, 66)
sphinx_plot(t.graphplot(heights={0: [0], 1: [4, 5, 1],
                                 2: [2], 3: [3, 6]},
                        edge_labels=True))