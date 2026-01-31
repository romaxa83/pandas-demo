import matplotlib.pyplot as plt
import numpy as np

from matplotlib.animation import FuncAnimation

def update_cos(frame, line, x):
    # frame - параметр, который меняется от кадра к кадру
    # в данном случае - это начальная фаза (угол)
    # line - ссылка на объект Line2D
    line.set_ydata(np.cos(x+frame))
    return [line]

fig, ax = plt.subplots()
x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.cos(x)
line, = ax.plot(x, y)

phasa = np.arange(0, 4*np.pi, 0.1)
animation = FuncAnimation(
    fig,             # фигура, где отображается анимация
    func=update_cos, # функция обновления текущего кадра
    frames=phasa,    # параметр, меняющийся от кадра к кадру
    fargs=(line, x), # дополнительные параметры для функции update_cos
    interval=30,     # задержка между кадрами, мс
    blit=True,       # использовать ли двойную буферизацию
    repeat=False,    # зацикливать ли анимацию
)

plt.show()