import matplotlib.pyplot as plt
from matplotlib.widgets import Button

class Visualizer:
    def __init__(self):
        self.dragging = False
        self.drag_start = None

    def interactive_env(self, env):
        fig, ax = plt.subplots(figsize=(6,6))
        plt.subplots_adjust(bottom=0.2)
        ax.set_xlim(env.xlim)
        ax.set_ylim(env.ylim)

        def onclick(event):
            if event.inaxes != ax:
                return
            if env.start is None:
                env.set_start(event.xdata, event.ydata)
                ax.scatter(*env.start, c='green', s=100, label='Start')
                fig.canvas.draw()
            elif env.goal is None:
                env.set_goal(event.xdata, event.ydata)
                ax.scatter(*env.goal, c='blue', s=100, label='Goal')
                fig.canvas.draw()
            else:
                self.dragging = True
                self.drag_start = (event.xdata, event.ydata)

        def onrelease(event):
            if self.dragging and self.drag_start is not None:
                x1, y1 = self.drag_start
                x2, y2 = event.xdata, event.ydata
                r = ((x2-x1)**2 + (y2-y1)**2)**0.5
                env.add_obstacle(x1, y1, r)
                circle = plt.Circle((x1, y1), r, color='red', alpha=0.4)
                ax.add_patch(circle)
                fig.canvas.draw()
            self.dragging = False

        cid_click = fig.canvas.mpl_connect('button_press_event', onclick)
        cid_release = fig.canvas.mpl_connect('button_release_event', onrelease)

        ax_button = plt.axes([0.4, 0.05, 0.2, 0.075])
        btn_done = Button(ax_button, 'Start GA')
        btn_done.on_clicked(lambda event: plt.close(fig))

        plt.title("First click = Start, Second click = Goal, then drag to create obstacles")
        plt.show()

    def plot_path(self, start, goal, obstacles, path):
        plt.figure(figsize=(6,6))
        for ox, oy, r in obstacles:
            circle = plt.Circle((ox, oy), r, color='red', alpha=0.4)
            plt.gca().add_patch(circle)
        xs, ys = zip(*([start] + path + [goal]))
        plt.plot(xs, ys, marker='o')
        plt.scatter(*start, c='green', s=100, label='Start')
        plt.scatter(*goal, c='blue', s=100, label='Goal')
        plt.xlim(0, 20)
        plt.ylim(0, 20)
        plt.legend()
        plt.title("Optimal Path with Genetic Algorithm - User Defined Environment")
        plt.show()
