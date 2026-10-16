#creamos el metodo constructor

class Miembro:
    def __init__(self, codigo, nombre, apellido, edad, meses, activo, plan):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__apellido = apellido
        self.__edad = edad
        self.__meses = meses
        self.__activo = activo
        self.__plan = plan
        
#creamos los getters paraobetner los valores de los atributos privados    
    def get_codigo(self):
        return self.__codigo
    def get_nombre(self):
        return self.__nombre
    def get_apellido(self):
        return self.__apellido
    def get_edad(self):
        return self.__edad
    def get_meses(self):
        return self.__meses
    def get_activo(self):
        return self.__activo
    def get_plan(self):
        return self.__plan
    
    def set_activo(self, activo):
        self.__activo = activo
    

class MiembroBasico(Miembro):
    def __init__(self, codigo, nombre, apellido, edad, meses, activo, plan):
        super().__init__(codigo, nombre, apellido, edad, meses, activo, plan)
    
    def calcular_pago(self):
        return self.get_meses() * 80000
    
class MiembroPremium(Miembro):
    def __init__(self, codigo, nombre, apellido, edad, meses, activo, plan):
        super().__init__(codigo, nombre, apellido, edad, meses, activo, plan)
        
    def calcular_pago(self):
        return self.get_meses() * 120000
    
class Gimnacio:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = []
     
    def agregar_miembro(self, miembro):
        self.miembros.append(miembro)
    
    def listar_miembros(self):
        for miembro in self.miembros:
            print(f" Codigo: {miembro.get_codigo()} - Nombre: {miembro.get_nombre()} - apellido: {miembro.get_apellido()} - Plan: {miembro.get_plan()} - Pago: {miembro.calcular_pago()}")
    
    def buscar_miembro(self, codigo):
        for miembro in self.miembros:
            if miembro.get_codigo() == codigo:
                print(f" Codigo: {miembro.get_codigo()} - Nombre: {miembro.get_nombre()} - apellido: {miembro.get_apellido()} - Plan: {miembro.get_plan()} - Pago: {miembro.calcular_pago()} - Estado: {miembro.get_activo()}")
                break       
        else:
            print("None")
    
    def dar_de_baja(self, codigo):
        for miembro in self.miembros:
            if miembro.get_codigo() == codigo:
                miembro.set_activo(False)
                print("\nUsuario dado de baja")
                break
        else:
            print("\nUsuario no encontrado, intente de nuevo")
            
    def calcular_pago_total(self):
        total = 0
        for miembro in self.miembros:
            total += miembro.calcular_pago()
        print(f"\nEl pago total de los miembros es: {total}")
        
    def listar_ranking(self):
        ranking = []
        for miembro in self.miembros:
            ranking.append((miembro.get_nombre(), miembro.calcular_pago()))
        ranking.sort(key=lambda x: x[1], reverse=True)
        
        for nombre, pago in ranking:
            print(f"Nombre: {nombre}, ${pago}")
        
    
Gym = Gimnacio("Gimnacion La salle fit")

while True:
    print("\n==== GIMNACIO ====")
    print("1. Listar miembros")
    print("2. Buscar miembro")
    print("3. Dar de Baja")
    print("4. Ver ranking")
    print("5. Ver ingreso total")
    print("6. Agregar miembro")
    print("0. Salir")
    
    opcion = input("\nElija una opcion ")
    
    if opcion == "0":
        print("\nHasta luego ")
        break
    elif opcion == "1":
        Gym.listar_miembros()
    elif opcion == "2":
        codigo = input("\nIngrese el codigo del cliente ")
        Gym.buscar_miembro(codigo)
    elif opcion == "3":
        codigo = input("\nIngrese el codigo de quien quiere dar de baja al plan ")
        Gym.dar_de_baja(codigo)
    elif opcion == "4":
        Gym.listar_ranking()
    elif opcion == "5":
        Gym.calcular_pago_total()
    elif opcion == "6":
        codigo = input("\nIngrese el codigo del cliente ")
        nombre = input("Ingrese el nombre del cliente ")
        apellido = input("Ingrese el apellido del cliente ")
        edad = int(input("Ingrese la edad del cliente "))
        meses = int(input("Ingrese la cantidad de meses que desea pagar "))
        activo = True
        plan = input("Ingrese el plan (Basico o Premium) ")
        
        if plan.lower() == "basico":
            miembro = MiembroBasico(codigo, nombre, apellido, edad, meses, activo, plan)
            Gym.agregar_miembro(miembro)
            print("\nMiembro agregado exitosamente")
        elif plan.lower() == "premium":
            miembro = MiembroPremium(codigo, nombre, apellido, edad, meses, activo, plan)
            Gym.agregar_miembro(miembro)
            print("\nMiembro agregado exitosamente")
    else:
        print("\nIngrese una opcion valida según el listado anterior ")

        