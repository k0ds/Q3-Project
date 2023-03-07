#for example use decibel scale 
from manim import *
import math

class Logarithmic(Scene):
    def construct(self):

        ax = Axes(
            x_range=[-1, 10, 2],
            y_range=[-10, 5, 2],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
        )
        parenttext = Text("The logarithmic function is defined as: ", font_size=25).to_edge(UP)

        parent = MathTex(r"f(x) = log_{a} x", substrings_to_isolate="a,x")
        parent2 = MathTex(r"f(x) = log_{2} x").to_corner(UL)
        parent.set_color_by_tex("a", ORANGE)
        parent.set_color_by_tex("x", YELLOW)
        domain = Text("Domain: (0, ++∞)", font_size=15).shift(RIGHT + DOWN)
        rangee = Text("Range: ℝ", font_size=15)
        funfact = Text("The logarithmic function is the inverse of the exponential function!", font_size=20, color=ORANGE).to_edge(DOWN)
        u1 = Underline(funfact[20:27])

        self.play(FadeIn(parenttext))
        self.play(FadeIn(parent))
        self.wait(2)
        self.play(FadeOut(parenttext))
        self.play(parent.animate.scale(0.8))
        self.play(parent.animate.to_corner(UL))
        self.play(FadeIn(ax))
        graph = ax.plot(lambda x: np.log2(x), use_smoothing=False, color=YELLOW)
        self.play(Transform(parent, parent2))
        self.play(Create(graph))
        self.wait(2)
        #self.play(FadeIn(domain, rangee))








