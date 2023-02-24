from manim import *


class ExponentialFunction(Scene):
    def construct(self):

        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 3, 1],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
         )
