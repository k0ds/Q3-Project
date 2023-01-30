from manim import *

class AbsoluteValue(Scene):
    def construct(self):

        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 3, 1],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
         )

        #absolute value form
        AbValue = MathTex(r"f(x)= a|x-h|+k", substrings_to_isolate="a,h,k")
        AbValue.set_color_by_tex("a", color=ORANGE)
        AbValue.set_color_by_tex("h", color=BLUE)
        AbValue.set_color_by_tex("k", color=BLUE)


        formexp = Text("a tells us how far the graph stretches vertically and if it opens up or down,\n h and k tells us how far the graph shifts horizontally and vertically",font_size=25, t2c={'[:1]':ORANGE, '[5:7]':BLUE, 'k':BLUE}).to_edge(DOWN)
        
        




        AbValueText =  Text("The absolute value equation has the form: ", font_size=25, color=YELLOW).to_edge(UP)
        parentfunctext = Text("The parent function: ", font_size=25, color=WHITE).to_edge(DR + UP)
        parentfunc = MathTex("y = |x|").next_to(parentfunctext, DOWN)


        self.play(FadeIn(AbValueText))
        self.play(Create(AbValue))
        self.play(FadeIn(formexp))
        self.wait(3)

        self.play(FadeOut(AbValue, AbValueText))


                                #replace this with a real ab value func
        graph = ax.plot(lambda x: np.abs(x) , x_range=[-5,5], use_smoothing=False, color=YELLOW)



        self.play(Create(ax))
        self.play(Create(graph))
        self.play(FadeIn(parentfunctext))
        self.play(FadeIn(parentfunc))

        self.wait(3)

        Dialoague1 = Text("If we wanted to graph this function: ", font_size=25, color=YELLOW)

        func2 = MathTex(r"f(x)= -2 |x| + 4", substrings_to_isolate="-2, x, 4").next_to(Dialoague1,DOWN)





