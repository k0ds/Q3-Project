from manim import *
import math
import numpy as np

class Radical(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        Radicalf = MathTex(r"y = \sqrt{x}")
       
        rad1 = Text("The radical function has the general form: ", font_size=25, color=WHITE).to_edge(UP)

        self.play(Write(rad1))
        self.play(Write(Radicalf))
        self.wait(3)
        self.play(FadeOut(rad1))
        self.play(Radicalf.animate.to_corner(UL))
        self.play(Radicalf.animate.scale(.8))


        ax2 = Axes(
            x_range=[-2, 10, 1],
            y_range=[-2, 10, 1],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
        )

        self.play(Create(ax2))
        graph = ax2.plot(lambda x: math.sqrt(x), x_range=[0.000001, 10], use_smoothing=False, color=YELLOW)
        graph2 = ax2.plot(lambda x: x**2, use_smoothing=False, color=RED)
        line = ax2.plot(lambda x: x, use_smoothing=False, color=WHITE)
        domain = Text("Domain: (0, ∞)")
        range = Text("Range:0,∞")
        wow = Text("The inverse of this function is the exponential function", font_size=20, color=ORANGE).to_edge(UP)
        inv = MathTex(r"y = x^2").next_to(Radicalf, DOWN)
        self.play(Create(graph))

        self.wait(2)
        self.play(Write(wow))
        self.play(Write(inv))
        self.play(Create(graph2))
        self.play(Create(line))

        dvl = ax2.coords_to_point(0,0)
        dvl2 = ax2.coords_to_point(1, -2) 
        
        cool = Text("Notice how the 2 graphs mirror each other over the line,\n showing that they are inverse", font_size=15, color=ORANGE).next_to(dvl2, DOWN)
        
       

        self.play(self.camera.frame.animate.scale(0.5).move_to(dvl))
        self.play(Write(cool))
        self.wait(2)
        self.play(Restore(self.camera.frame))
        self.play(FadeOut(cool, graph2, wow, inv, line, Radicalf))
        yandxint = Text("This function has no y or x intercept with real numbers,\n as the square root of a negative number is not real", font_size=30, color=WHITE).to_edge(UP)
        however = Text("However, a cube root, with index of 3 has an x and y intercept of 0", font_size=25, color=ORANGE).next_to(yandxint, DOWN)
        self.play(FadeOut(graph, ax2))
       

        
        ax3 = Axes(
            x_range=[-5, 3, 1],
            y_range=[-5, 3, 1],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
        )
        cuberootf = MathTex(r"f(x) = \sqrt[3]{x}").to_corner(UL)
        cuberoot = ax3.plot(lambda x: np.cbrt(x), use_smoothing=False, color=YELLOW)

        self.play(Write(yandxint))
        self.play(Write(however))
        self.wait(3)
        self.play(FadeOut(yandxint, however))

        self.play(Create(ax3))

        self.play(Create(cuberoot))
        self.play(Write(cuberootf))


        self.wait(3)

        self.play(FadeOut(cuberoot, cuberootf))

        ax4 = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
        )
        self.play(Transform(ax3, ax4))

       

        
        tt = Text("If we shift the parent function down by 2, we have the function: ", font_size=20, color=ORANGE).to_edge(UP)
        transform = MathTex(r"y = \sqrt{x} - 2").next_to(tt, DOWN + LEFT)
        graph4 = ax4.plot(lambda x: math.sqrt(x) - 2, x_range=[0.0000001, 10], use_smoothing=False, color=YELLOW )
        self.play(Write(tt))
        self.play(Write(transform))
        self.play(Create(graph4))
        self.wait(3)
        
        self.play(FadeOut(transform, tt, ax3, graph4))
        ax3.scale(0.8)



       

        alge = Text("We can determine the x-intercept algebraically: ", font_size=25).to_edge(UP)
        s1 = MathTex(r"y = 0").next_to(transform, DOWN)
        s2 = MathTex(r"&0 = \sqrt{x} - 2\\").next_to(s1, DOWN)
        s3 = MathTex(r"&2 = \sqrt{x}\\").next_to(s2, DOWN)
        s4 = MathTex(r"&x = 2^2 \\ &x = 4").next_to(s3, DOWN)

        steps = [s1, s2, s3, s4]
        self.play(Write(alge))
        self.play(Write(transform))
        self.play(transform.animate.next_to(alge, DOWN))

        for i in steps:
            self.wait(1)
            self.play(Write(i))

        self.wait(3)

        