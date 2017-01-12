from math import sin, cos, pi
P = graphs.PetersenGraph()
d = {'#FF0000':[0,5], '#FF9900':[1,6], '#FFFF00':[2,7], '#00FF00':[3,8],
    '#0000FF':[4,9]}
pos_dict = {}
for i in range(5):
    x = float(cos(pi/2 + ((2*pi)/5)*i))
    y = float(sin(pi/2 + ((2*pi)/5)*i))
    pos_dict[i] = [x,y]

for i in range(5,10):
    x = float(0.5*cos(pi/2 + ((2*pi)/5)*i))
    y = float(0.5*sin(pi/2 + ((2*pi)/5)*i))
    pos_dict[i] = [x,y]

pl = P.graphplot(pos=pos_dict, vertex_colors=d)
sphinx_plot(pl)