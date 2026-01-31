import matplotlib.pyplot as plt
import numpy as np

# строим синусойду в трехмерном графике
fig = plt.figure(figsize=(7, 4))
ax_3d = fig.add_subplot(projection='3d')

x = np.arange(-2*np.pi, 2*np.pi, 0.01)
y = np.arange(-2*np.pi, 2*np.pi, 0.01)

xgrid, ygrid = np.meshgrid(x,y)

zgrid = np.sin(xgrid) * np.sin(ygrid) / (xgrid * ygrid)

ax_3d.plot_wireframe(xgrid, ygrid, zgrid)

plt.show()