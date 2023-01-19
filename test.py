from manim import *

class LogScalingExample(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-8, 10, 2],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
        )


        graph = ax.plot(lambda x: -4.9*x**2 + 10*x + 3, x_range=[0,10], use_smoothing=False, color = YELLOW)
        self.play(Create(ax))
        self.play(Create(graph))






