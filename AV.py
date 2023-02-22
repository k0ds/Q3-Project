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

     
        formexp = Text("a tells us how far the graph stretches vertically and if it opens up or down,\n h and k tells us how far the graph shifts horizontally and vertically",font_size=25, t2c={'[:1]':ORANGE, '[6:9]':BLUE, 'k':BLUE}).to_edge(DOWN)
        formexp1 = Text("a tells us how for the graph strectches vertically and if it opens up or down", font_size=25, t2c={'[:1]': ORANGE}).to_edge(DOWN)
        formexp2 = Text("h and k tells us how far the graph shifts horizontally and vertically", font_size=25, t2c={'[6:7]': BLUE, '[:1]': '#58adbd'}).next_to(formexp1, UP)


        #TODO: Fix the colors of this ^^^

        




        AbValueText =  Text("The absolute value equation has the form: ", font_size=25, color=YELLOW).to_edge(UP)
        parentfunctext = Text("The parent function: ", font_size=25, color=WHITE).to_edge(DR + UP)
        parentfunc = MathTex("y = |x|").next_to(parentfunctext, DOWN)


        self.play(FadeIn(AbValueText))
        self.play(Create(AbValue))
        self.play(FadeIn(formexp1))
        self.play(FadeIn(formexp2))
        self.wait(4)

        self.play(FadeOut(AbValue, AbValueText, formexp1, formexp2))



                                #replace this with a real ab value func
        graph = ax.plot(lambda x: np.abs(x) , x_range=[-5,5], use_smoothing=False, color=YELLOW)



        self.play(Create(ax))
        self.play(Create(graph))
        self.play(FadeIn(parentfunctext))
        self.play(FadeIn(parentfunc))

        self.wait(5)

        self.play(FadeOut(ax,graph,parentfunc,parentfunctext))

        Dialoague1 = Text("If we wanted to graph this function: ", font_size=20, color=YELLOW)

        func2 = MathTex(r"f(x)= -2 |x| + 2", substrings_to_isolate="-2, x, 2").next_to(Dialoague1,DOWN)
        Dialouge2 = Text("We would refer to the form of the function:", font_size=25, color=YELLOW).next_to(func2, DOWN)


        self.play(FadeIn(Dialoague1, func2))
        self.play(FadeIn(Dialouge2))
        AbValue.next_to(Dialouge2, DOWN)
        self.play(FadeIn(AbValue))

        self.wait(4)

        self.play(FadeOut(Dialouge2, AbValue))
        #move this up, fade in graphed version and explain each part
        g1 = VGroup(func2, Dialoague1)
        self.play(g1.animate.to_edge(UP))
        self.play(FadeIn(ax))

       
        self.play(func2.animate.shift(LEFT * 3))
        graph = ax.plot(lambda x: -2 * np.abs(x) + 2, x_range=[-5,5], use_smoothing=False, color=YELLOW)
        self.play(FadeIn(graph))

        textexp1 = Text("Notice that the first term is negative\n making the graph open downwards\n and the start of the graph is at 2", font_size=20, color=WHITE).to_edge(UR)
        textexp1.shift(DOWN)
        self.play(FadeIn(textexp1))

        self.wait(2)
         





        




