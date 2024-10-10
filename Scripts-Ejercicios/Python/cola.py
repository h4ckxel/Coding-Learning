# clase cola para gestionar la sala de espera
class Cola:
    def __init__(self):
        self.items = []  # aquí guardo los pacientes en una lista

    def is_empty(self):
        # verifico si la cola está vacía
        return len(self.items) == 0

    def encolar(self, item):
        # agrego un paciente al final de la cola
        self.items.append(item)

    def desencolar(self):
        # elimino al paciente que está al frente de la cola
        if self.is_empty():
            raise IndexError("Cola vacía. no hay pacientes para atender.")
        return self.items.pop(0)

    def peek(self):
        # obtengo el paciente al frente de la cola sin eliminarlo
        if self.is_empty():
            raise IndexError("Cola vacía. no hay pacientes en espera.")
        return self.items[0]

    def imprimir_cola(self):
        # muestro todos los pacientes que están en la cola
        if self.is_empty():
            print("\nNo hay pacientes en espera.")
        else:
            print("Pacientes en espera:")
            for paciente in self.items:
                print(f"Paciente: {paciente.nombre}, hora de llegada: {paciente.hora_llegada}")

# clase paciente con nombre y hora de llegada
class Paciente:
    def __init__(self, nombre, hora_llegada):
        self.nombre = nombre
        self.hora_llegada = hora_llegada

def main():
    sala_espera = Cola()  # creo una cola para la sala de espera

    while True:
        print("\n1. Agregar paciente")
        print("2. Ver siguiente paciente")
        print("3. Atender paciente")
        print("4. Ver todos los pacientes en espera")
        print("5. Salir")

        opcion = int(input("\nSelecciona una opción: "))

        if opcion == 1:
            # agrego un paciente nuevo a la cola
            nombre = input("Nombre del paciente: ")
            hora = input("Hora de llegada (hh:mm): ")
            nuevo_paciente = Paciente(nombre, hora)
            sala_espera.encolar(nuevo_paciente)
            print(f"\nPaciente {nombre} agregado a la cola.")

        elif opcion == 2:
            # muestro al siguiente paciente que será atendido
            try:
                siguiente = sala_espera.peek()
                print(f"\nSiguiente paciente: {siguiente.nombre}, hora de llegada: {siguiente.hora_llegada}")
            except IndexError as e:
                print(e)

        elif opcion == 3:
            # atiendo al paciente frontal de la cola
            try:
                atendido = sala_espera.desencolar()
                print(f"\nAtendiendo a: {atendido.nombre}, hora de llegada: {atendido.hora_llegada}")
            except IndexError as e:
                print(e)

        elif opcion == 4:
            # muestro la lista de todos los pacientes en espera
            sala_espera.imprimir_cola()

        elif opcion == 5:
            # salgo del programa
            print("\nSaliendo del programa.")
            break

        else:
            print("\nOpción no válida. intenta nuevamente.")

main()
