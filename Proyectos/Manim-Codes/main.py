from manim import *
import numpy as np

class QuantumSuperposition(Scene):
    def construct(self):
        title = Text("Superposición Cuántica", font_size=50).shift(UP*3)
        self.play(Write(title))
        self.wait(1)
        
        # Línea base
        line = Line(LEFT*4, RIGHT*4).set_color(GRAY)
        self.play(Create(line))
        
        # Onda de probabilidad inicial
        wave = FunctionGraph(lambda x: np.sin(2*np.pi*x) * np.exp(-x**2), x_range=[-3,3], color=BLUE)
        self.play(Create(wave), run_time=2)
        self.wait(1)
        
        # Expansión de la onda con efectos
        wave_expand = FunctionGraph(lambda x: np.sin(2*np.pi*x) * np.exp(-x**2/2), x_range=[-4,4], color=BLUE)
        self.play(Transform(wave, wave_expand), run_time=2)
        
        # División en superposición
        wave1 = FunctionGraph(lambda x: np.sin(2*np.pi*x) * np.exp(-(x-2)**2), x_range=[-4,4], color=GREEN)
        wave2 = FunctionGraph(lambda x: np.sin(2*np.pi*x) * np.exp(-(x+2)**2), x_range=[-4,4], color=RED)
        
        self.play(Transform(wave, VGroup(wave1, wave2)), run_time=2)
        self.wait(1)
        
        # Ondas oscilando con desplazamiento
        self.play(wave1.animate.shift(UP*0.5), wave2.animate.shift(DOWN*0.5), run_time=2)
        
        # Efecto de recombinación con interferencia
        final_wave = FunctionGraph(lambda x: np.sin(3*np.pi*x) * np.exp(-x**2) * np.cos(2*x), x_range=[-4,4], color=YELLOW)
        self.play(Transform(VGroup(wave1, wave2), final_wave), run_time=2)
        
        # Destellos y efectos visuales
        glow = Circle(radius=0.5, color=WHITE).shift(DOWN*2)
        self.play(AnimationGroup(FadeIn(glow), GrowFromCenter(glow), run_time=2))
        
        # Mensaje final con animación
        conclusion = Text("¡Así funciona la superposición cuántica!", font_size=40).shift(DOWN*2)
        self.play(Write(conclusion), run_time=2)
        
        # Fade out con efectos
        self.play(FadeOut(VGroup(final_wave, conclusion, glow)), run_time=3)
        self.wait(2)
