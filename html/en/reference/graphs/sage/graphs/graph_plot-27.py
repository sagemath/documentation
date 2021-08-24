g = Graph({}, loops=True, multiedges=True, sparse=True)
g.add_edges([(0, 0, 'a'), (0, 0, 'b'), (0, 1, 'c'),
             (0, 1, 'd'), (0, 1, 'e'), (0, 1, 'f'),
             (0, 1, 'f'), (2, 1, 'g'), (2, 2, 'h')])
GP = g.graphplot(vertex_size=100, edge_labels=True,
                 color_by_label=True, edge_style='dashed')
GP.set_vertices(talk=True)
GP.set_vertices(vertex_color='green', vertex_shape='^')
sphinx_plot(GP)