from manim import *

class AbsoluteValue(Scene):
    def construct(self):

        #absolute value form
        AbValue = MathTex(r"f(x)= a|x-h|+k", substrings_to_isolate="a,h,k")
        AbValue.set_color_by_tex("a", color=ORANGE)
        AbValue.set_color_by_tex("h", color=BLUE)
        AbValue.set_color_by_tex("k", color=BLUE)



        AbValueText =  Text("The absolute value equation has the form: ", font_size=25, color=YELLOW).to_edge(UP)

        self.play(FadeIn(AbValueText))
        self.play(Create(AbValue))
        self.wait(3)
