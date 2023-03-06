from manim import *


class ExponentialFunction(Scene):
    def construct(self):

        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-1, 10, 1],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
         )

        ExpFunc = MathTex(r"f(x) = a^x", font_size=70 ,substrings_to_isolate="x")
        ExpFunc2 = MathTex(r"f(x) = 2^x",substrings_to_isolate="x").to_corner(UL)
        ExpFuncExample = MathTex(r"f(x) = 2^x")
        ExpGrowth = MathTex(r"f(x) = a(1+r)^x", substrings_to_isolate='x,a,r')
        ExpGrowth.set_color_by_tex("a", YELLOW)
        ExpGrowth.set_color_by_tex("r", BLUE)
        ExpGrowth.set_color_by_tex("x", ORANGE)

        ExpGrowthExp1 = Text("a = Initial amount",font_size=20, t2c={'[:1]': YELLOW}).next_to(ExpGrowth, DOWN)
        ExpGrowthExp2 = Text("r = Growth rate",font_size=20, t2c={'[:1]': BLUE}).next_to(ExpGrowthExp1, DOWN)
        ExpGrowthExp3 = Text("x = Number of time intervals",font_size=20, t2c={'[:1]': ORANGE}).next_to(ExpGrowthExp2, DOWN)
        DomainText = Text("Domain: ℝ",font_size=17, color=ORANGE).next_to(ExpFunc, RIGHT * 5 + DOWN)
        RangeText = Text("Range: while a > 0, (0, +∞)", font_size=17, color=ORANGE).next_to(DomainText, DOWN)
        ExpGrowthStuff = VGroup(ExpGrowthExp1, ExpGrowthExp2, ExpGrowthExp3)


        ExpFunc.set_color_by_tex("x", YELLOW)
        ExpFunc2.set_color_by_tex("x", YELLOW)
        ExpFuncText = Text("The exponential function is generally defined by the formula: ", font_size=25, color=WHITE).to_edge(UP)
        ExpFuncText2 = Text("The input variable is x.\n The exponential curve depends on the value of x.", font_size=25, t2c={'[22:23]': YELLOW, '[72:73]': YELLOW}, color=WHITE).to_edge(DOWN)
        ExpFuncText3 = Text("a is the constant which defines the base of the exponentiation.", font_size=25, color=WHITE).to_edge(DOWN)

        wowtext = Text("For any value of a, the y-intercept is always 1", font_size=25, color=BLUE).to_edge(DOWN)
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


        tracker = ValueTracker(2)
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

        def update_graph(mob):
            mob.become(ax.plot(lambda x: tracker.get_value()**x, x_range=[-4,4], use_smoothing=False, color=YELLOW))

        self.play(Transform(ExpFunc,ExpFunc3))
        self.play(FadeIn(updater1, number))
        self.wait(2)
        graph.add_updater(update_graph)
        self.play(tracker.animate(run_time=6).set_value(10))


        self.wait(3)

        self.play(FadeOut(ax, graph, tracker,wowtext, updater1, number, asymp))
        self.play(ExpFunc.animate.shift(ORIGIN))
        self.play(ExpFunc.animate.scale(1))

        self.play(ReplacementTransform(ExpFunc, ExpGrowth))

      

       
        
        



        #introduce the exp growth function:
        self.play(FadeIn(ExpGrowth))
        self.wait(2)
        self.play(FadeIn(ExpGrowthStuff))
        self.wait(3)
        self.play(FadeOut(ExpGrowthStuff))


        ExpGrowthExp12 = Text("a = 1000",font_size=20, t2c={'[:1]': YELLOW}).next_to(ExpFunc, DOWN)
        ExpGrowthExp22 = Text("r = 5.7% = 5.7/100 = 0.057 (rate of interest)",font_size=20, t2c={'[:1]': BLUE}).next_to(ExpGrowthExp1, DOWN)
        ExpGrowthExp32 = Text("x = Years",font_size=20, t2c={'[:1]': ORANGE}).next_to(ExpGrowthExp2, DOWN)
        Exp2 = VGroup(ExpGrowthExp12, ExpGrowthExp22, ExpGrowthExp32)
        compinterest = MathTex(r"f(x) = 1000(1 +0.057)^x", substrings_to_isolate="1000, 0.057, x")
        compinterest.set_color_by_tex("1000", YELLOW)
        compinterest.set_color_by_tex("0.057", BLUE)
        compinterest.set_color_by_tex("x", ORANGE)
        compinterestgood = compinterest.copy().to_corner(UR)

        compinterestIntro = Text("An example of exponential growth is compound interest:\nWith an initial investment of $1000 at 5.7% annual interest:", font_size=20, color=WHITE).to_edge(UP)
        

        Title = Text("Compound Interest", font_size=20).next_to(ax, UP)

       
        self.play(FadeIn(compinterestIntro))

        self.play(Transform(ExpGrowth, compinterest))
        self.play(FadeIn(Exp2))

        self.wait(3)
        self.play(FadeOut(Exp2, compinterestIntro, compinterest, ExpGrowth))
        self.play(FadeIn(compinterestgood))
        self.play(compinterestgood.animate.scale(0.8))
        
        
        

       
        self.wait(1)



        

        ax = Axes(
            x_range=[0,  30, 5],
            y_range=[0, 4000, 500],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 25}
         )
        
        
        self.play(FadeIn(Title))
        self.play(FadeIn(ax))
        graph =  ax.plot(lambda x: 1000 * (1 + 0.057)**x, use_smoothing=False, color=YELLOW)
        
        x_label = ax.get_y_axis_label(Tex("\$ Investment Value ").scale(0.50))
        y_label = ax.get_x_axis_label(Tex("Years").scale(0.50))
     
        self.play(FadeIn(x_label, y_label))

        self.play(compinterestgood.animate.shift(DOWN*2))

        self.play(FadeIn(graph))

        self.wait(5)


        self.play(FadeOut(Title, ax, x_label, y_label, graph, compinterestgood))
        
        yinttext = Text("We can determine the y-intercept algebraically: ", color=YELLOW, font_size=25).to_edge(UP)
        yint1 = MathTex(r"x = 0").next_to(yinttext, DOWN)

        compinteresty = MathTex(r"f(0) &= 1000(1 +0.057)^0\\")
        # r" &=1000*1.057^0 \\", r"&=1000*1\\", r"&=1000"
        compinteresty2 = MathTex(r" &=1000*1.057^0 \\").next_to(compinteresty, DOWN)
        compinterest3 = MathTex( r"&=1000*1\\").next_to(compinteresty2, DOWN)
        compinterest4 = MathTex(r"&=1000").next_to(compinterest3, DOWN)
        yint2 = Text("The y-intercept is 1000", color=YELLOW, font_size=25).next_to(compinterest4, DOWN)
        compinterestgood2 = compinterestgood.copy().shift(ORIGIN + UP)
        self.play(FadeIn(compinterestgood2))
       
        self.play(FadeIn(yinttext))
        self.play(FadeIn(yint1))

        self.play(Transform(compinterestgood2, compinteresty[0]))
        self.play(FadeOut(yint1))
        self.play(FadeIn(compinteresty2))
        self.wait(1)
        self.play(FadeIn(compinterest3))
        self.wait(1)
        self.play(FadeIn(compinterest4))
        self.wait(1)
        


        self.play(FadeIn(yint2))

        self.wait(3)

        



     
        
        






       


        



        

