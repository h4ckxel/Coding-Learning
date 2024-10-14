from manim import *

class Example(Scene):
    def constructor(self):
        self.play(FadeIn(Dot(Radius=4, color=WHITE)))
        self.wait(3)