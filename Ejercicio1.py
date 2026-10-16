class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print(f"{self.nombre} está estudiando en el grado {self.grado}.")
        

nombre = (input("Ingrese el nombre: "))
edad = (input("Ingrese la edad: "))
grado = (input("Ingrese el grado: "))

estudiante = Estudiante(nombre, edad, grado)

print(estudiante.nombre)

    