class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad 
        
    def mostrar_persona(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def mostrar_grado(self):
        print(f"Grado: {self.grado}")

estudiante = Estudiante("Diego", 23, 11)
        
estudiante.mostrar_persona()
estudiante.mostrar_grado()
        