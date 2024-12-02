import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import matplotlib.animation as animation

from defaults import background_color

fig, ax = plt.subplots(figsize=(8, 4))
here = Path(__file__).parent
frames = 4 * 60
x = np.arange(0, 2 * np.pi, 0.01)
line, *_ = ax.plot(x, np.sin(x))
line2, *_ = ax.plot(x, np.cos(x))
fig.savefig(here / "example.png")


def animate(i):
    rot = 2 * np.pi * i / frames
    line.set_ydata(np.sin(x + rot))
    line2.set_ydata(np.cos(x + rot))
    return (line, line2)


ani = animation.FuncAnimation(
    fig, animate, interval=1 / 60, blit=True, save_count=frames
)

writer = animation.FFMpegWriter(fps=60, bitrate=1800, codec="libx264")
ani.save(
    here / "video.mp4", writer=writer, savefig_kwargs={"facecolor": background_color}
)
