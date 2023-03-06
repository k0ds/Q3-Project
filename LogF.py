#for example use decibel scale as its log
from manim import *

class Logarithmic(Scene):
    def construct(self):

        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-1, 10, 1],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
        )



