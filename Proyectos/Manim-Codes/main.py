from manim import *

class EcuacionDeSchrodinger(Scene):
    def construct(self):
        # Título de la escena
        titulo = Tex("Ecuación de Schrödinger", font_size=48)
        self.play(Write(titulo))
        self.wait(2)
        self.play(FadeOut(titulo))

        # Ecuación de Schrödinger dependiente del tiempo
        ecuacion = MathTex(
            r"i\hbar \frac{\partial}{\partial t} \Psi(x, t) = \hat{H} \Psi(x, t)",
            font_size=40
        )
        ecuacion.shift(UP * 2)

        # Explicación de la ecuación
        explicacion = Tex(
            r"Donde:",
            r"$\Psi(x, t)$ es la función de onda,",
            r"$\hat{H}$ es el operador Hamiltoniano,",
            r"$i$ es la unidad imaginaria,",
            r"$\hbar$ es la constante reducida de Planck.",
            font_size=30
        )
        explicacion.arrange(DOWN, aligned_edge=LEFT)
        explicacion.next_to(ecuacion, DOWN, buff=1)

        # Mostrar la ecuación y su explicación
        self.play(Write(ecuacion))
        self.wait(1)
        for linea in explicacion:
            self.play(Write(linea))
            self.wait(0.5)

        # Representación de la función de onda
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": BLUE}
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label=r"\Psi(x, t)")

        # Función de onda inicial (un paquete de onda gaussiano)
        def funcion_de_onda(x, t=0):
            return np.exp(-(x - t)**2) * np.cos(2 * PI * (x - t))

        # Gráfica de la función de onda
        grafica = axes.plot(lambda x: funcion_de_onda(x, 0), color=YELLOW)
        grafica_label = MathTex(r"\Psi(x, 0)", font_size=30).next_to(grafica, UP)

        # Mostrar los ejes y la función de onda
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(grafica), Write(grafica_label))
        self.wait(2)

        # Animación de la evolución temporal
        tiempo = ValueTracker(0)
        grafica.add_updater(
            lambda m: m.become(
                axes.plot(lambda x: funcion_de_onda(x, tiempo.get_value()), color=YELLOW)
            )
        )

        # Texto para indicar la evolución temporal
        tiempo_texto = MathTex(r"t = 0", font_size=30).to_edge(DOWN)
        tiempo_texto.add_updater(lambda m: m.become(MathTex(fr"t = {tiempo.get_value():.2f}", font_size=30)))

        self.add(tiempo_texto)
        self.play(tiempo.animate.set_value(4), run_time=8, rate_func=linear)
        self.wait(2)

        # Conclusión
        conclusion = Tex(
            "La ecuación de Schrödinger describe cómo evoluciona la función de onda en el tiempo.",
            font_size=30
        )
        conclusion.to_edge(DOWN)
        self.play(Write(conclusion))
        self.wait(3)

        # Limpiar la escena
        self.play(*[FadeOut(mob) for mob in self.mobjects])
