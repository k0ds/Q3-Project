from manim import *


class ExponentialFunction(Scene):
    def construct(self):

        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 10, 1],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
         )

        ExpFunc = MathTex(r"f(x) = a^x", font_size=70 ,substrings_to_isolate="x")
        ExpFunc2 = MathTex(r"f(x) = 2^x",substrings_to_isolate="x").to_corner(UL)
        ExpFuncExample = MathTex(r"f(x) = 2^x")
        ExpGrowth = MathTex(r"f(x) = a(1+r)")
        ExpGrowthExp1 = Text("a = initial amount")
        ExpGrowthExp2 = Text("r = growth rate")
        ExpGrowthExp3 = Text("x = number of time intervals")
        DomainText = Text("Domain: ℝ",font_size=17, color=ORANGE).next_to(ExpFunc, RIGHT * 5 + DOWN)
        RangeText = Text("Range: while a > 0, (0, +∞)", font_size=17, color=ORANGE).next_to(DomainText, DOWN)


        ExpFunc.set_color_by_tex("x", YELLOW)
        ExpFunc2.set_color_by_tex("x", YELLOW)
        ExpFuncText = Text("The exponential function is generally defined by the formula: ", font_size=25, color=WHITE).to_edge(UP)
        ExpFuncText2 = Text("The input variable is x.\n The exponential curve depends on the value of x.", font_size=25, t2c={'[22:23]': YELLOW, '[72:73]': YELLOW}, color=WHITE).to_edge(DOWN)
        ExpFuncText3 = Text("a is the constant which defines the base of the exponentiation.", font_size=25, color=WHITE).to_edge(DOWN)

        wowtext = Text("notice that for any value of a, the y-intercept is always 1", font_size=25, color=BLUE).to_edge(DOWN)
        asymp = Text("Notice that f(x) never touches 0,\n but approaches asymptotically as  x → -∞", font_size=16, t2c={'[49:64]': ORANGE}, color=WHITE).next_to(ExpFunc2, DOWN)
        
        self.play(FadeIn(ExpFuncText))
        

        self.play(FadeIn(ExpFunc))
        self.wait(2)
        self.play(FadeIn(ExpFuncText2))
        self.wait(3)
        self.play(FadeOut(ExpFuncText2))
        self.play(FadeIn(ExpFuncText3))
        self.wait(3)
        self.play(FadeIn(DomainText, RangeText))
        
        self.wait(3)

        self.play(FadeOut(DomainText, RangeText, ExpFuncText, ExpFuncText3))

        graph = ax.plot(lambda x: 2**x, x_range=[-5,9], use_smoothing=False, color = YELLOW)
        self.play(ExpFunc.animate.scale(0.9))
        self.play(ExpFunc.animate.to_corner(UL))
        self.play(FadeIn(ax))
        self.play(Transform(ExpFunc, ExpFunc2))
        self.wait(2)
        self.play(Create(graph))

        
        asymp.shift(RIGHT * 0.8)
        self.play(FadeIn(asymp))

        updater1 = MathTex(r"a = ").next_to(asymp, DOWN)
        number = ValueTracker(1)


        tracker = ValueTracker(1)
        number = DecimalNumber(1).scale(0.8).next_to(updater1, RIGHT)
        number.add_updater(lambda m: m.set_value(tracker.get_value()))
        
        ExpFunc3 = MathTex(r"f(x) = a^x", substrings_to_isolate="x").to_corner(UL)
        ExpFunc3.set_color_by_tex('x', YELLOW)

        
       # graph = ax.plot(lambda x: tracker.get_value()**x, x_range=[-5,9], use_smoothing=False, color = YELLOW)
        #graph.add_updater(lambda m: m.become(ax.plot(lambda x:tracker.get_value()**x, x_range=[-5,9], use_smoothing=False, color = YELLOW)))


        self.wait(4)
        

        self.play(FadeIn(wowtext))

        self.add(graph)
        self.wait()

        self.play(Transform(ExpFunc,ExpFunc3))
        self.play(FadeIn(updater1, number))
        self.wait(2)
        self.play(tracker.animate(run_time=5).set_value(10))
        #now figure out a way to have the graph update along number, has to do with lines 71, 72, needs more research






       


        



        

