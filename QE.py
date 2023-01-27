from manim import *
import time

class LogScalingExample(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-8, 10, 2],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
            #y_axis_config={"scaling": LogBase(custom_labels=True)},
        )

        #f(x)=ax^2+bx+c
        equation = MathTex(r'f(x)=ax^2''+bx''+c', substrings_to_isolate="x,a,b,c")
        equation.set_color_by_tex('x', YELLOW)
        equation.set_color_by_tex('a', GREEN)
        equation.set_color_by_tex('b', ORANGE)
        equation.set_color_by_tex('c', BLUE)
        #equation.substrings_to_isolate="x,a,b,c"
        

       # equation[2].set_color(YELLOW)
    

        eq = 'f(x) = x^2 - 7x + 10'


        #f(x)= x^2-7x+10
        
        
        
        equationWithnum =  MathTex(eq, substrings_to_isolate='7,10')


        
        

        
        
        equationWithnum.set_color_by_tex('7', ORANGE)
        equationWithnum.set_color_by_tex('10', BLUE)
       

        factor1 = MathTex(r"2 + 5 = 7", substrings_to_isolate='2,5,7')
        factor2 = MathTex(r"2 * 5 = 10",substrings_to_isolate="2,5,10")

        factor1.set_color_by_tex('2', GREEN)
        factor1.set_color_by_tex('5', ORANGE)
        factor1.set_color_by_tex('7', ORANGE)

        factor2.set_color_by_tex('2', GREEN)
        factor2.set_color_by_tex('5', ORANGE)
        factor2.set_color_by_tex('10', BLUE)

        FacEq1 = MathTex(r"(x + 2)", substrings_to_isolate="2")
        FacEq2 = MathTex(r"(x + 5)", substrings_to_isolate="5")
        FacEq1.set_color_by_tex("2", GREEN)
        FacEq2.set_color_by_tex("5", ORANGE)




        factoredequation = MathTex(r"(x + 2)(x + 5)", substrings_to_isolate="2,5").to_edge(UP)
        factoredequation.set_color_by_tex("2", GREEN)
        factoredequation.set_color_by_tex("5", ORANGE)
        
       

        exp2 = Text("2 and 5 sum to 7 and multiply to 10, which represents a and b of the quadratic.", color=WHITE).scale(0.5).to_edge(UP)

        exp1 = Text('The x-intercepts of the graphed quadratic are equal to its factored form', color=BLUE).scale(0.5).to_edge(UP, buff=0.1)

        applicationText = Text("The quadratic can be used to model projectile trajectories.", color=ORANGE, font_size=25).to_edge(DOWN)

       # 10, 13
        factoredetext = Text("Factored Form", color=WHITE, font_size=25).to_edge(DOWN)
        VertexText = Text("The vertex (v 1,8) of the curve can be interpreted as the highest point the projectile will reach.", color=YELLOW, font_size=20).to_edge(UP)
        function1 = MathTex(r"h(t) = -4.9t^2 + 10t + 3").next_to(VertexText, DOWN)
        functionexp = Text("-4.9 serves as the gravitational constant\n 10 is the initial speed \n 3 is the initial height of the projectile", color=GREEN, font_size=20).next_to(function1, DOWN)

        factoredequation2 = MathTex(r"(x + 2)(x + 5)", substrings_to_isolate="2,5")
        factoredequation2.set_color_by_tex("2", GREEN)
        factoredequation2.set_color_by_tex("5", ORANGE)

        x = ax.get_x_axis()
        y = ax.get_y_axis()
       

        num2 = x.numbers[1]
        num5 = x.numbers[4]
        num2.set_color(GREEN)
        num5.set_color(ORANGE)

        a = MathTex(r"a",color=GREEN).next_to(num2, DOWN)
        b = MathTex(r"b",color=ORANGE).next_to(num5, DOWN)

        VertexForm = MathTex(r"y = -4.9(x - 1)^2 + 8",substrings_to_isolate="1,8").to_edge(ORIGIN)
        VertexForm.set_color_by_tex("1", ORANGE)
        VertexForm.set_color_by_tex("8", ORANGE)


        VertexFormExp = Text("The function in vertex form.", font_size=30, color=WHITE).to_edge(UP)
        VertexFormExp2 = Text("Notice the vertex x and y coordinates in the vertex form equation (rounded).", font_size=25, color=WHITE).to_edge(DOWN)

      

        
        graph = ax.plot(lambda x: x**2 - 7*x + 10, x_range=[0,9], use_smoothing=False, color = YELLOW)

        
      
       
        self.play(Create(equation))
        self.play(equation.animate.shift(UP))
        
        self.play(Create(equationWithnum))

        self.play(equation.animate.to_edge(DOWN))
        self.play(equationWithnum.animate.next_to(equation, UP))
        
        self.play(Create(ax))
        self.play(Create(graph))
        self.wait(2)
        
        
        self.play(Create(factoredequation))
        self.play(Create(a))
        self.play(Create(b))
        

        num2.set_color(GREEN)
        num5.set_color(ORANGE)

     
        


        self.play(FadeIn(exp1))
        


        self.wait(5)
        animations = [FadeOut(ax,graph,a,b,factoredequation)]
        self.play(AnimationGroup(*animations, lag_ratio=0.5))

        self.play(equationWithnum.animate.move_to(ORIGIN))
        self.play(equation.animate.next_to(equationWithnum, DOWN))
        self.play(factor1.animate.next_to(equation, DOWN))
        self.play(factor1.animate.shift(RIGHT))
        self.play(factor2.animate.next_to(equation, DOWN))
        self.play(factor2.animate.shift(LEFT * 1.5))

       
        self.play(FadeOut(exp1, shift=DOWN))

        self.play(equationWithnum.animate.next_to(equation, UP))
        self.play(FadeIn(exp2, shift=DOWN))

        



        
        self.play(FadeIn(factoredetext))
        self.play(factoredequation2.animate.next_to(factoredetext, UP))





        self.wait(5)

        screen = Group(equation, equationWithnum, factor1, factor2, exp2,factoredetext,factoredequation2)
        self.play(FadeOut(screen))
        num2.set_color(WHITE)
        num5.set_color(WHITE)

        #h(t) = -4.9t^+10t+3

        graph = ax.plot(lambda x: -4.9*x**2 + 10*x + 3, x_range=[0,2.5], use_smoothing=False, color = YELLOW)

        G1 = VGroup(ax,graph)
        animations3 = [FadeIn(ax,graph)]
        self.play(AnimationGroup(*animations3, lag_ratio=0.5))
        self.play(FadeIn(applicationText))
        u1 = Underline(applicationText, color=ORANGE)
        self.play(Create(u1))


        
        self.wait(5)

        

        d1 = Dot().set_color(ORANGE) 
        l2 = VMobject()
        self.add(d1, l2)
        
        self.play(MoveAlongPath(d1, graph), rate_func=linear)

        self.wait(2)
        self.play(FadeOut(d1))

        x = ax.get_x_axis()
        y = ax.get_y_axis()
      
        d2 = Dot().set_color(BLUE)

        self.add(d2.next_to(y.numbers[7]))
        self.play(d2.animate.shift(RIGHT * 1.1))
        v = Text(r"v",color=ORANGE, font_size=23).next_to(d2, UP)
        self.play(Create(v))

       

        




        

      

        self.play(FadeIn(VertexText))


        function1 = MathTex(r"h(t) = -4.9t^2 + 10t + 3").next_to(VertexText, DOWN)
        self.play(Create(function1))

        self.play(FadeIn(functionexp))



        self.wait(5)

       

        self.play(FadeOut(G1, VertexText, applicationText, functionexp, u1, d1, d2, v))
        

        self.play(FadeIn(VertexForm))
        self.play(FadeIn(VertexFormExp))
        self.play(FadeIn(VertexFormExp2))

        self.wait(7)

        self.play(FadeOut(VertexForm, VertexFormExp, VertexFormExp2, function1))




        #the parent function: f(x) = x^2
        # The parent function is inverted and shifted over the x axi
        #make graph show parent function
        ax2 = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
            #y_axis_config={"scaling": LogBase(custom_labels=True)},
        )

        G1 = VGroup(ax2,graph)
        


        graph = ax2.plot(lambda x: x**2, x_range=[-5,5], use_smoothing=False, color=ORANGE)
        animations3 = [FadeIn(ax2,graph)]


        parentfunctext = Text("Parent function: ", font_size=25, color=WHITE).to_edge(UR)
        parentdesctext = Text("The line is inverted and shifted over the y axis to form our function: ", font_size=25, color=WHITE).to_edge(ORIGIN)
        domaintext = Text("The domain of the function is: (-∞,∞) ", font_size=25, color=ORANGE).to_edge(UP)
        rangetext = Text("The range: (y ≤ 8)", font_size=25, color=ORANGE).next_to(domaintext, DOWN)

        Parentfunc = MathTex(r"f(x) = x^2").next_to(parentfunctext, DOWN)

        self.play(AnimationGroup(*animations3, lag_ratio=0.5))

        self.play(FadeIn(parentfunctext))
        self.play(FadeIn(Parentfunc))

        self.wait(3)



        ax3 = Axes(
            x_range=[0, 10, 1],
            y_range=[-8, 10, 2],
            tips=False,
            axis_config={"include_numbers": True, "font_size": 30}
            #y_axis_config={"scaling": LogBase(custom_labels=True)},
        )

        self.play(FadeOut(ax2))
        self.play(FadeOut(graph))
        self.play(FadeIn(parentdesctext))
        self.wait(3)
        
        self.play(FadeOut(parentdesctext))

        graph = ax3.plot(lambda x: -4.9*x**2 + 10*x + 3, x_range=[0,2.5], use_smoothing=False, color = YELLOW)

        self.play(FadeIn(ax3, graph))

        self.play(FadeIn(domaintext))
        self.play(FadeIn(rangetext))
        self.wait(5)






















        


         







        

    

        
        