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

        self.play(Write(parenttext))
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
        self.play(FadeIn(domain, rangee, ))
        self.play(Write(asymp))
        self.wait(3)

        self.play(FadeOut(domain, rangee, asymp, ax, graph, parent))

        self.play(Write(funfact))
        self.play(Write(u1))
        funfactg = Group(funfact, u1)
        self.wait(1)
        self.play(funfactg.animate.scale(.6))
        self.play(funfactg.animate.to_corner(UL))

        ax2 = Axes(
            x_range=[-5, 10, 1],
            y_range=[-5, 10, 1],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
        )

        graph2 = ax2.plot(lambda x: math.e**x, x_range=[-5,9], use_smoothing=False, color = RED)
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



        self.play(FadeOut(exp1, line1, graph, line, funfactg))
        self.play(log1.animate.to_corner(UR))
        nattext = Text("This is also known as the the \"natural\" log.\n Where e is is Eulers Number = 2.718281828459...\n also written as: ", font_size=17, color=ORANGE).next_to(log1, DOWN + LEFT)
        nattext.shift(RIGHT / 5)
        natlog = MathTex(r"f(x) = ln(x)", ).next_to(nattext, DOWN)
        natlog.scale(0.8)
        graphg = Group(ax2, graph2)
        self.play(graphg.animate.shift(LEFT))
        self.play(Write(nattext))
        self.play(FadeIn(natlog))
        
        
        self.wait(4)
        graphg = Group(ax2)
        self.play(FadeOut(nattext, natlog, graph2, log1))   

        self.play(graphg.animate.shift(RIGHT))

        xint = Text("The graph of the parent function will always intersect the x-axis at x=1", font_size=18, color=ORANGE).to_corner(UR)
        
        updater1 = MathTex(r"a = ").to_corner(UL)
        number = ValueTracker(1.1)
        graph3 = ax2.plot(lambda x: math.log(x, 1.1), x_range=[0.0001, 10], use_smoothing=False, color=YELLOW)

        tracker = ValueTracker(1.1)
        number = DecimalNumber(1).scale(0.8).next_to(updater1, RIGHT)
        number.add_updater(lambda m: m.set_value(tracker.get_value()))
        
        

        def update_graph(mob):
            mob.become(ax2.plot(lambda x: math.log(x, tracker.get_value()), x_range=[0.000001,10], use_smoothing=False, color=YELLOW))
        graph3.add_updater(update_graph)
        self.play(Write(xint))
        self.play(FadeIn(updater1, number))
        
        parentog = MathTex(r"f(x) = log_{a}x").next_to(updater1, DOWN)
        parentog.scale(.6)
        self.play(FadeIn(parentog))
        
        
       
        self.play(Create(graph3))
        self.play(tracker.animate(run_time=8).set_value(10))
        self.wait(3)
        self.play(FadeOut(tracker, ax2, graph3, xint, updater1, number, parentog))


        algetext = Text("We can also find the x-intercept algebraically. ", font_size=20, color=WHITE).to_edge(UP)
        algetex2 = Text("Since the log function is the opposite of the exponential function,\n we can equate log function to its exponential counterpart:", font_size=20, color=YELLOW).next_to(algetext, DOWN)
        self.play(Write(algetext))
        self.play(Write(algetex2))
        gen_form = MathTex(r"y = log_{a}x").next_to(algetex2, DOWN)
        part1 = MathTex(r"y = 0").next_to(gen_form, RIGHT)
        s1 = MathTex(r"0 = log_{a}x").next_to(gen_form, DOWN)
        s2 = MathTex(r"a^0 = x").next_to(s1, DOWN)
        s3 = MathTex(r"x = 1").next_to(s2, DOWN)
        final = Text("As we can see, for any value of a, the x intercept is 1", font_size=25, color=ORANGE).next_to(s3, DOWN)

        self.play(FadeIn(gen_form))
        self.wait(1)
        self.play(FadeIn(s1))
        self.wait(1)
        self.play(FadeIn(s2))
        self.wait(1)
        self.play(FadeIn(s3))
        self.wait(1)
        self.play(Write(final))

        self.wait(3)











