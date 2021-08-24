G = graphs.HeawoodGraph().copy(sparse=True)
for u, v, l in G.edges():
    G.set_edge_label(u, v, f'({u},{v})')
sphinx_plot(G.graphplot(edge_labels=True))