# clase cola para gestionar la sala de espera con prioridad según gravedad
class Cola:
    def __init__(self):
        self.items = []  # aquí guardo los pacientes en una lista

    def is_empty(self):
        # verifico si la cola está vacía
        return len(self.items) == 0

    def encolar(self, paciente):
        # agrego un paciente a la cola
        self.items.append(paciente)
        self.graveton()

    def graveton(self):
        # pacientes por gravedad 
        for i in range(len(self.items)):
            for j in range(i + 1, len(self.items)):
                if self.items[i].gravedad > self.items[j].gravedad:
                    # intercambio de pacientes gravedad
                    temp = self.items[i]
                    self.items[i] = self.items[j]
                    self.items[j] = temp

    def desencolar(self):
        # elimino al paciente que está al frente de la cola (más grave)
        if self.is_empty():
            raise IndexError("\nCola vacía. No hay pacientes para atender. Intentelo de nuevo")
        return self.items.pop(0)

    def peek(self):
        # obtengo el paciente al frente de la cola sin eliminarlo
        if self.is_empty():
            raise IndexError("\nCola vacía. No hay pacientes en espera.")
        return self.items[0]

    def imprimir_cola(self):
        # muestro todos los pacientes que están en la cola
        if self.is_empty():
            print("\nNo hay pacientes en espera.")
        else:
            print("\nPacientes en espera (ordenados por gravedad):")
            for paciente in self.items:
                print(f"\nPaciente: {paciente.nombre}, gravedad: {paciente.gravedad}, hora de llegada: {paciente.hora_llegada}")

# clase paciente con nombre, hora de llegada y gravedad
class Paciente:
    def __init__(self, nombre, hora_llegada, gravedad):
        self.nombre = nombre
        self.hora_llegada = hora_llegada
        self.gravedad = gravedad

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
            gravedad = int(input("Gravedad del paciente (1 más grave - 10 menos grave): "))
            nuevo_paciente = Paciente(nombre, hora, gravedad)
            sala_espera.encolar(nuevo_paciente)
            print(f"\nPaciente {nombre} agregado a la cola con gravedad {gravedad}.")

        elif opcion == 2:
            # muestro al siguiente paciente que será atendido
            if sala_espera.is_empty():
                print("\nNo hay pacientes en la sala de espera.")
            else:
                siguiente = sala_espera.peek()
                print(f"\nEl siguiente paciente es: {siguiente.nombre}, gravedad: {siguiente.gravedad}")

        elif opcion == 3:
            # atiendo al paciente con mayor prioridad
            '''
            para cancelar el programa, llamar directamente el index error
            si se quiere que funcione como un ciclo, y dejarlo intentar
            nuevamente al usuario, dejar el (try) y (except IndexError as e\n Print(e))
            '''
            #atendido = sala_espera.desencolar()
            #print(f"\nAtendiendo a: {atendido.nombre}, gravedad: {atendido.gravedad}, hora de llegada: {atendido.hora_llegada}")
            try:
                atendido = sala_espera.desencolar()
                print(f"\nAtendiendo a: {atendido.nombre}, gravedad: {atendido.gravedad}, hora de llegada: {atendido.hora_llegada}")
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
            print("\nOpción no válida. Intenta nuevamente.")

main()
