# árbol de decisión básico manual utilizando funciones y condicionales
def decision_tree_manual(features):
    # nodo raíz: condición basada en el clima
    if features['weather'] == 'rainy':
        # segundo nivel del árbol: decisión basada en la temperatura
        if features['temperature'] < 15:
            return 'stay inside'
        else:
            return 'carry an umbrella'
    elif features['weather'] == 'sunny':
        # segundo nivel del árbol: decisión basada en la humedad
        if features['humidity'] < 50:
            return 'go for a walk'
        else:
            return 'drink water'
    else:
        return 'no decision'

# ejemplo de uso con datos
features = {'weather': 'rainy', 'temperature': 12, 'humidity': 80}
decision = decision_tree_manual(features)
print(decision)  # salida: stay inside
