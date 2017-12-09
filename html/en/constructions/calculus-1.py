f = piecewise([((0,pi/2), -1), ((pi/2,pi), 2)])
s5 = f.fourier_series_partial_sum(5)
g = plot(f, (0,pi)) + plot(s5, (x,0,pi), color='red')
sphinx_plot(g)