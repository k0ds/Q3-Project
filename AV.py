from manim import *

class AbsoluteValue(Scene):
    def construct(self):

        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-8, 10, 2],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
         )

        #absolute value form
        AbValue = MathTex(r"f(x)= a|x-h|+k", substrings_to_isolate="a,h,k")
        AbValue.set_color_by_tex("a", color=ORANGE)
        AbValue.set_color_by_tex("h", color=BLUE)
        AbValue.set_color_by_tex("k", color=BLUE)



        AbValueText =  Text("The absolute value equation has the form: ", font_size=25, color=YELLOW).to_edge(UP)

        self.play(FadeIn(AbValueText))
        self.play(Create(AbValue))
        self.wait(3)

        self.play(FadeOut(AbValue, AbValueText))

        #−2∣x∣+4
                                #replace this with a real ab value func
        graph = ax.plot(lambda x: -2 * x + 4 , x_range=[0,9], use_smoothing=False, color = YELLOW)


        self.play(Create(ax))
        self.play(Create(graph))