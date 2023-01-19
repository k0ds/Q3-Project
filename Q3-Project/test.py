from manim import *

class LogScalingExample(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-8, 10, 2],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
        )


        graph = ParametricFunction(lambda t: ax.c2p(t, - 4.9*t**2 + 10*t + 3), t_range= [0,2.5], color = YELLOW) 
        self.play(Create(ax))
        self.play(Create(graph))