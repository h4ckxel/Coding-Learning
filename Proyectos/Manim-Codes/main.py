from manim import *

class QuantumSuperposition(Scene):
    def construct(self):
        # titulo
        title = Text("Superposición Cuántica y Colapso de la Función de Onda", font_size=32)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # representación de la partícula cuántica
        particle = Dot(color=BLUE).scale(2)
        particle_label = Text("Partícula Cuántica", font_size=24).next_to(particle, DOWN)

        # partícula
        self.play(FadeIn(particle), Write(particle_label))  # Paréntesis corregido aquí
        self.wait(1)

        # superposición
        superposition_text = Text("La partícula está en una superposición de estados", font_size=24).to_edge(UP)
        self.play(Write(superposition_text))
        self.wait(2)

        # estados posibles (|0⟩ y |1⟩)
        state_0 = Dot(color=RED).shift(LEFT * 3)
        state_1 = Dot(color=GREEN).shift(RIGHT * 3)
        state_0_label = MathTex(r"|0\rangle", font_size=24).next_to(state_0, DOWN)
        state_1_label = MathTex(r"|1\rangle", font_size=24).next_to(state_1, DOWN)

        # estados posibles (show)
        self.play(FadeIn(state_0), Write(state_0_label))
        self.play(FadeIn(state_1), Write(state_1_label))
        self.wait(2)

        # superposición como una onda que conecta los dos estados
        wave = CurvedArrow(state_0.get_center(), state_1.get_center(), angle=-TAU/4, color=YELLOW)
        self.play(Create(wave))
        self.wait(2)

        # colapso de la función de onda
        collapse_text = Text("Al medir, la partícula colapsa a uno de los estados", font_size=24).to_edge(UP)
        self.play(ReplacementTransform(superposition_text, collapse_text))
        self.wait(2)

        # colapso a uno de los estados (ejemplo, |0⟩)
        self.play(particle.animate.move_to(state_0.get_center()), FadeOut(wave))
        self.wait(2)

        # resultado de la medición
        result_text = MathTex(r"\text{Resultado de la medición: } |0\rangle", font_size=32)
        self.play(Write(result_text))
        self.wait(3)

        # escena limpia
        self.play(*[FadeOut(mob) for mob in self.mobjects])
