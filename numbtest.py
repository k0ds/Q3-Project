from manim import *

class ChangingVariableWithValueTracker(Scene):
    def construct(self):
        tracker = ValueTracker(1)
        number = DecimalNumber(1).scale(5)
        number.add_updater(lambda m: m.set_value(tracker.get_value()))
        self.add(number)
        self.play(tracker.animate(run_time=5).set_value(10))
        self.wait()