D = DiGraph(multiedges=True, sparse=True)
for i in range(5):
     D.add_edge((i,i+1,'a'))
     D.add_edge((i,i-1,'b'))
sphinx_plot(D.graphplot(edge_labels=True,edge_colors=D._color_by_label()))