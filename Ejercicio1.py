import json

class vehiculo:
    def __init__(self, placa,marca,modelo):
        self.__placa = placa
        self.__marca = marca
        self.__modelo = modelo

    def get_placa(self):
        return self.__placa
    
    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo
    
    def mostrar_informacion(self):
        print("Placa:", self.__placa)
        print("Marca:", self.__marca)
        print("Modelo:", self.__modelo)
    
class Bus(vehiculo):
    def __init__(self,placa,marca,modelo,capacidad_pasajeros,numero_ruta):
        super().__init__(placa,marca,modelo)
        self.__capacidad_pasajeros = capacidad_pasajeros
        self.__numero_ruta = numero_ruta
    
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Capacidad:", self.__capacidad_pasajeros)
        print("Ruta:", self.__numero_ruta)

    def to_dict(self):
        return {
            "tipo": "Bus",
            "placa": self.get_placa(),
            "marca": self.get_marca(),
            "modelo": self.get_modelo(),
            "capacidad": self._Bus__capacidad_pasajeros,
            "ruta": self._Bus__numero_ruta
    }

class taxi(vehiculo):
    def __init__(self,placa,marca,modelo,turno_servicio,aire_acondicionado):
        super().__init__(placa,marca,modelo)
        self.__turno_servicio = turno_servicio
        self.__aire_acondicionado = aire_acondicionado

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Turno:", self.__turno_servicio)
        print("Aire:", self.__aire_acondicionado)

    def to_dict(self):
        return {
            "tipo": "Taxi",
            "placa": self.get_placa(),
            "marca": self.get_marca(),
            "modelo": self.get_modelo(),
            "turno": self._taxi__turno_servicio,
            "aire": self._taxi__aire_acondicionado
    }

class camion(vehiculo):
    def __init__(self,placa,marca,modelo,ruta_asignada,capacidad_carga,peso_max):
        super().__init__(placa,marca,modelo)
        self.__ruta_asignada = ruta_asignada
        self.__capacidad_carga = capacidad_carga
        self.__peso_max = peso_max
        
    def mostrar_informacion(self):
        super().mostrar_informacion()
        print("Ruta:", self.__ruta_asignada)
        print("Capacidad de carga:", self.__capacidad_carga)
        print("Peso maximo:", self.__peso_max)

    def to_dict(self):
        return {
            "tipo": "camion",
            "placa": self.get_placa(),
            "marca": self.get_marca(),
            "modelo": self.get_modelo(),
            "ruta": self._camion__ruta_asignada,
            "capacidad de carga": self._camion__capacidad_carga,
            "peso maximo": self._camion__peso_max

    }

def guardar_datos(lista_vehiculos):
    with open("vehiculos.json", "w") as archivo:
        
        lista_dicts = [v.to_dict() for v in lista_vehiculos]
        json.dump(lista_dicts, archivo, indent=4)
    print("¡Datos guardados!")

def cargar_datos():
    try:
        with open("vehiculos.json", "r") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return []
    
def menu():
    
    datos_crudos = cargar_datos()
    lista_vehiculos = []
    
    
    for d in datos_crudos:
        if d["tipo"] == "Bus":
            v = Bus(d["placa"], d["marca"], d["modelo"], d["capacidad"], d["ruta"])
        elif d["tipo"] == "Taxi":
            v = taxi(d["placa"], d["marca"], d["modelo"], d["turno"], d["aire"])
        elif d["tipo"] == "camion":
            v = camion(d["placa"], d["marca"], d["modelo"], d["ruta"], d["capacidad de carga"], d["peso maximo"])
        lista_vehiculos.append(v)

    while True:
        print("\n--- MENÚ DE TRANSPORTE ---")
        print("1. Registrar Bus")
        print("2. Registrar Taxi")
        print("3. Registrar Camión")
        print("4. Ver todos los vehículos")
        print("5. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion in ["1", "2", "3"]:
            p = input("Placa: ")
            m = input("Marca: ")
            mo = input("Modelo: ")
            
            if opcion == "1":
                cap = input("Capacidad pasajeros: ")
                ru = input("Número de ruta: ")
                nuevo = Bus(p, m, mo, cap, ru)
            elif opcion == "2":
                tur = input("Turno (Dia/Noche): ")
                ai = input("¿Tiene aire? (Si/No): ")
                nuevo = taxi(p, m, mo, tur, ai)
            elif opcion == "3":
                ra = input("Ruta asignada: ")
                cc = input("Capacidad carga: ")
                pm = input("Peso máximo: ")
                nuevo = camion(p, m, mo, ra, cc, pm)
            
            lista_vehiculos.append(nuevo)
            guardar_datos(lista_vehiculos) 
            print("¡Vehículo registrado y guardado!")

        elif opcion == "4":
            print("\n--- LISTA DE VEHÍCULOS ---")
            if not lista_vehiculos:
                print("No hay vehículos registrados.")
            for v in lista_vehiculos:
                v.mostrar_informacion() 
                print("-" * 20)

        elif opcion == "5":
            print("Cerrando sistema...")
            break
        else:
            print("Opción inválida, intenta de nuevo.")


if __name__ == "__main__":
    menu()