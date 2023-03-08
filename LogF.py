#for example use decibel scale 
from manim import *
import math

class Logarithmic(Scene):
    def construct(self):

        ax = Axes(
            x_range=[-3, 8, 1],
            y_range=[-5, 4, 1],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
        )
        parenttext = Text("The logarithmic function is defined as: ", font_size=25).to_edge(UP)

        parent = MathTex(r"f(x) = log_{a} x", substrings_to_isolate="a,x")
        parent2 = MathTex(r"f(x) = log_{2} x").to_corner(UL)
        parent.set_color_by_tex("a", ORANGE)
        parent.set_color_by_tex("x", YELLOW)
        domain = Text("Domain: (0, +∞)", font_size=18).to_corner(DR)
        rangee = Text("Range: ℝ", font_size=18).next_to(domain, UP)
        funfact = Text("The logarithmic function is the inverse of the exponential function!", font_size=25, color=ORANGE)
        u1 = Underline(funfact[27:34], color=ORANGE)

        asymp = Text("Notice that f(x) never touches -y,\n but approaches asymptotically as  y → -∞", font_size=16, t2c={'[50:65]': ORANGE}, color=WHITE).next_to(domain, UP + LEFT*3)

        self.play(FadeIn(parenttext))
        self.play(FadeIn(parent))
        self.wait(2)
        self.play(FadeOut(parenttext))
        self.play(parent.animate.scale(0.8))
        self.play(parent.animate.to_corner(UL))
        self.play(FadeIn(ax))
        graph = ax.plot(lambda x: math.log2(x),x_range=[0.00001, 10] ,use_smoothing=False, color=YELLOW)
        self.play(Transform(parent, parent2))
        self.play(Write(graph))
        self.wait(2)
        self.play(FadeIn(domain, rangee, asymp))
        self.wait(3)

        self.play(FadeOut(domain, rangee, asymp, ax, graph, parent))

        self.play(FadeIn(funfact, u1))
        funfactg = Group(funfact, u1)
        self.play(funfactg.animate.scale(.6))
        self.play(funfactg.animate.to_corner(UL))

        ax2 = Axes(
            x_range=[-5, 10, 1],
            y_range=[-5, 10, 1],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
        )

        graph2 = ax2.plot(lambda x: 2.718**x, x_range=[-5,9], use_smoothing=False, color = RED)
        graph = ax2.plot(lambda x: math.log(x),x_range=[0.00001, 10] ,use_smoothing=False, color=YELLOW)    
        line = ax2.plot(lambda x: x, use_smoothing=False, color=WHITE)
        log1 = MathTex(r"y = log_{e} ^x", color=YELLOW).next_to(funfact, DOWN)
        exp1 = MathTex(r"y = e^x", color=RED).next_to(log1, DOWN)
        line1 = MathTex(r"y = x", color=WHITE).next_to(exp1, DOWN)
        funcs = VGroup(log1, exp1, line1)
        funcs.shift(LEFT)
        log1.scale(.7)
        exp1.scale(.7)
        line1.scale(.7)

        self.play(FadeIn(ax2))
        self.play(Write(graph))
        self.play(Write(graph2))
        self.play(Write(line))
        self.play(FadeIn(funcs))
        self.wait(3)

        self.play(FadeOut(funcs, ax2, graph, graph2, line, funfactg))
        


       








