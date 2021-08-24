from sage.plot.colors import rainbow
C = graphs.CubeGraph(5)
R = rainbow(5)
edge_colors = {}
for i in range(5):
    edge_colors[R[i]] = []
for u, v, l in C.edges():
    for i in range(5):
        if u[i] != v[i]:
            edge_colors[R[i]].append((u, v, l))
sphinx_plot(C.graphplot(vertex_labels=False, vertex_size=0,
                        edge_colors=edge_colors))