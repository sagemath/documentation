d = DiGraph(loops=True, multiedges=True, sparse=True)
d.add_edges([(0, 0, 'a'), (0, 0, 'b'), (0, 1, 'c'),
             (0, 1, 'd'), (0, 1, 'e'), (0, 1, 'f'),
             (0, 1, 'f'), (2, 1, 'g'), (2, 2, 'h')])
GP = d.graphplot(vertex_size=100, edge_labels=True,
                 color_by_label=True, edge_style='dashed')
GP.set_edges(edge_style='solid')
sphinx_plot(GP)