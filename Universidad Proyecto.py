class Asignatura:
    def __init__(self, nombre, creditos, costo_por_credito):
        self.nombre = nombre
        self.creditos = creditos
        self.costo_por_credito = costo_por_credito
        self.estudiantes = []


class Estudiante:
    def __init__(self, nombre, genero, edad, estrato):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        self.estrato = estrato



asignaturas = {}


def validar_entrada(mensaje, tipo=int, positivo=True):
    while True:
        try:
            valor = tipo(input(mensaje))
            if positivo and valor <= 0:
                print("Error: Ingrese un valor positivo.")
            else:
                return valor
        except ValueError:
            print("Error: Intente de nuevo.")


def registrar_asignatura():
    nombre = input("Nombre de la asignatura: ")
    creditos = validar_entrada("Cantidad de créditos: ")
    costo_por_credito = validar_entrada("Costo por crédito: ", float)

    if nombre not in asignaturas:
        asignaturas[nombre] = Asignatura(nombre, creditos, costo_por_credito)
    else:
        print("La asignatura ya está registrada.")


def registrar_estudiante():
    asignatura = input("Nombre de la asignatura: ")
    if asignatura not in asignaturas:
        print("Error: La asignatura no existe.")
        return

    nombre = input("Nombre del estudiante: ")
    genero = input("Género: ")
    edad = validar_entrada("Edad: ")
    estrato = validar_entrada("Estrato (1, 2 o 3): ", int)

    nuevo_estudiante = Estudiante(nombre, genero, edad, estrato)
    asignaturas[asignatura].estudiantes.append(nuevo_estudiante)


def estudiantes_por_asignatura():
    for nombre, asignatura in asignaturas.items():
        print(f"En la asignatura {nombre} hay en total {len(asignatura.estudiantes)} estudiantes.")


def asignatura_mayor_recaudo():
    if asignaturas:
        mayor = max(asignaturas.values(), key=lambda a: a.creditos * a.costo_por_credito * len(a.estudiantes))
        total = mayor.creditos * mayor.costo_por_credito * len(mayor.estudiantes)
        print(f"La asignatura que más recaudó es: {mayor.nombre} con un total de ${total:.2f}.")
    else:
        print("No hay asignaturas registradas.")


def promedio_costo_credito():
    if not asignaturas:
        print("No hay asignaturas registradas.")
        return

    total_costo = sum(asig.costo_por_credito for asig in asignaturas.values())
    promedio = total_costo / len(asignaturas)
    print(f"El promedio de costo por crédito es: {promedio:.2f}.")


def total_descuentos_por_estrato(estrato):
    total_descuento = 0
    descuentos = {1: 0.5, 2: 0.3, 3: 0.1}

    for asignatura in asignaturas.values():
        for estudiante in asignatura.estudiantes:
            if estudiante.estrato == estrato:
                costo = asignatura.creditos * asignatura.costo_por_credito
                total_descuento += costo * descuentos.get(estrato, 0)

    print(f"El total de descuentos para el estrato {estrato} es: ${total_descuento:.2f}.")


def estudiantes_estrato_1_por_asignatura():
    for nombre, asignatura in asignaturas.items():
        cantidad = sum(1 for est in asignatura.estudiantes if est.estrato == 1)
        print(f"En la asignatura {nombre} hay {cantidad} estudiantes de estrato 1.")


def total_recaudado():
    total = 0
    for asignatura in asignaturas.values():
        total += asignatura.creditos * asignatura.costo_por_credito * len(asignatura.estudiantes)
    print(f"El total recaudado de todas las asignaturas es: ${total:.2f}.")


def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar asignatura")
        print("2. Registrar estudiante")
        print("3. Mostrar estudiantes por asignatura")
        print("4. Asignatura con mayor recaudo")
        print("5. Promedio de costo por crédito")
        print("6. Total descuentos por estrato")
        print("7. Estudiantes de estrato 1 por asignatura")
        print("8. Total de recaudo de todas las asignaturas")
        print("9. Salir")

        opcion = validar_entrada("Seleccione una opción: ")

        if opcion == 1:
            registrar_asignatura()
        elif opcion == 2:
            registrar_estudiante()
        elif opcion == 3:
            estudiantes_por_asignatura()
        elif opcion == 4:
            asignatura_mayor_recaudo()
        elif opcion == 5:
            promedio_costo_credito()
        elif opcion == 6:
            estrato = validar_entrada("Ingrese el estrato (1, 2 o 3): ", int)
            total_descuentos_por_estrato(estrato)
        elif opcion == 7:
            estudiantes_estrato_1_por_asignatura()
        elif opcion == 8:
            total_recaudado()
        elif opcion == 9:
            break
        else:
            print("La opción no es válida.")


if __name__ == "__main__":
    menu()
