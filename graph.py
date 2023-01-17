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
        FacEq2 = MathTex(r"(x - 5)", substrings_to_isolate="5")
        FacEq1.set_color_by_tex("2", GREEN)
        FacEq2.set_color_by_tex("5", ORANGE)




        factoredequation = MathTex(r"(x + 2)(x - 5)", substrings_to_isolate="2,5").to_edge(UP)
        factoredequation.set_color_by_tex("2", GREEN)
        factoredequation.set_color_by_tex("5", ORANGE)
        exp2 = Text("2 and 5 sum to 7 and multiply to 10, which represents a and b of the quadratic.", color=WHITE).scale(0.5).to_edge(UP)

        exp1 = Text('The x-intercepts of the graphed quadratic are equal to its factored form', color=BLUE).scale(0.5).to_edge(UP, buff=0.1)
       # 10, 13

        x = ax.get_x_axis()
        y = ax.get_y_axis()
       

        num2 = x.numbers[1]
        num5 = x.numbers[4]
        num2.set_color(GREEN)
        num5.set_color(ORANGE)

        a = MathTex(r"a",color=GREEN).next_to(num2, DOWN)
        b = MathTex(r"b",color=ORANGE).next_to(num5, DOWN)


      

        
        graph = ax.plot(lambda x: x**2 - 7*x + 10, x_range=[0,10], use_smoothing=False, color = YELLOW)

        
      
       
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

     
        


        self.play(AddTextLetterByLetter(exp1, time_per_char=0.01))
        


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

       



        self.play(FacEq1.animate.next_to(factor2, DOWN))
        self.play(FacEq2.animate.next_to(factor1, DOWN))

        self.wait(5)
         




       #(x + 2) (x - 5)
       #2 and 5 should move in from factor1 and factor2

        #show factor 1 and 2 convert into factored with cool transformation
        #maybe use transformMatchingTex



        

        #self.remove(ax,graph)

        
        