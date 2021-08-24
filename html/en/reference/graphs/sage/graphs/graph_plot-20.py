g = Graph({}, loops=True, multiedges=True, sparse=True)
g.add_edges([(0, 0, 'a'), (0, 0, 'b'), (0, 1, 'c'),
             (0, 1, 'd'), (0, 1, 'e'), (0, 1, 'f'),
             (0, 1, 'f'), (2, 1, 'g'), (2, 2, 'h')])
sphinx_plot(g.graphplot(edge_labels=True,
                        color_by_label=True,
                        edge_style='dashed'))