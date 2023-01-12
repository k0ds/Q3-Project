from manim import *
import time

class LogScalingExample(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-8, 10, 1],
            y_range=[-8, 10, 2],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
            #y_axis_config={"scaling": LogBase(custom_labels=True)},
        )

        #y=ax^{2}+bx+c

        equation = MathTex(r"f(x)=ax^2+bx+c",substrings_to_isolate="x",)
        equationWithnum =  MathTex(r"f(x)= x^2-7x+10", )


        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: x**2 - 7*x + 10, use_smoothing=True, color = YELLOW)

        equation.set_color_by_tex("x", YELLOW)
        equation.set_color_by_tex("a", GREEN)
        equation.set_color_by_tex("b", ORANGE)
        self.play(Create(equation))
        self.wait(1)
        self.play(equation.animate.shift(UP))
        self.play(Create(equationWithnum))

        self.play(equation.animate.to_edge(UP - 2))
        self.play(equationWithnum.animate.next_to(equation, UP))
        
        self.play(Create(ax))
        self.play(Create(graph))
        self.wait(3)
        #self.remove(ax,graph)

        
        