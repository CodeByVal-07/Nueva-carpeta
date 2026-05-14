import json

class Usuario:
    def __init__(self, id_usuario,nombre,correo,contraseña):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__correo = correo
        self.__contraseña = contraseña 

    def get_id_usuario(self):
        return self.__id_usuario
    
    def get_nombre(self):
        return self.__nombre
    
    def get_correo(self):
        return self.__correo
    
    def get_contraseña(self):
        return self.__contraseña
    
    def mostrar_perfil(self):
        print("Id:", self.__id_usuario)
        print("Nombre:", self.__nombre)
        print("Correo:", self.__correo)
        print("Contraseña:", self.__contraseña)

class Estudiante(Usuario):

    def __init__(self,id_usuario,nombre,correo,contraseña,codigo_estudiante,curso_inscrito,progreso):
        super().__init__(id_usuario,nombre,correo,contraseña)
        self.__codigo_estudiante = codigo_estudiante
        self.__curso_inscrito = curso_inscrito
        self.__progreso = progreso
    
    def mostrar_perfil(self):
        super().mostrar_perfil()
        print("Codigo Estudiantil:", self.__codigo_estudiante)
        print("Curso Inscrito:", self.__curso_inscrito)
        print("Progreso:", self.__progreso)

    def to_dict(self):
        return {
            "tipo": "Estudiante",
            "Id_usuario": self.get_id_usuario(),
            "Nombre": self.get_nombre(),
            "Correo": self.get_correo(),
            "Contraseña": self.get_contraseña(),
            "Codigo Estudiantil": self._Estudiante__codigo_estudiante,
            "Curso Inscrito ": self._Estudiante__curso_inscrito,
            "Progreso": self._Estudiante__progreso
    }

class Profesor(Usuario):

    def __init__(self,id_usuario,nombre,correo,contraseña,especialidad,Cursos_impartidos,calificacion):
        super().__init__(id_usuario,nombre,correo,contraseña)
        self.__especialidad = especialidad
        self.__cursos_impartidos = Cursos_impartidos
        self.__calificacion = calificacion
    
    def mostrar_perfil(self):
        super().mostrar_perfil()
        print("Especializacion:", self.__especialidad)
        print("Cursos Impartidos:", self.__cursos_impartidos)
        print("Calificacion:", self.__calificacion)

    def to_dict(self):
        return {
            "tipo": "Profesor",
            "Id_usuario": self.get_id_usuario(),
            "Nombre": self.get_nombre(),
            "Correo": self.get_correo(),
            "Contraseña": self.get_contraseña(),
            "Especializacion": self._Profesor__especialidad,
            "Cursos Impartidos": self._Profesor__cursos_impartidos,
            "Calificacion": self._Profesor__calificacion
    }

def guardar_datos(lista_usuarios, nombre_archivo="usuarios.json"):
    try:
        datos_dict = [u.to_dict() for u in lista_usuarios]
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            json.dump(datos_dict, f, indent=4, ensure_ascii=False)
        print("Datos guardados exitosamente.")
    except Exception as e:
        print(f"Error al guardar: {e}")


def cargar_datos(nombre_archivo="usuarios.json"):
    lista_usuarios = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f:
            datos = json.load(f)
            for d in datos:
                if d["tipo"] == "Estudiante":
                    obj = Estudiante(
                        d["Id_usuario"], d["Nombre"], d["Correo"], d["Contraseña"],
                        d["Codigo Estudiantil"], d["Curso Inscrito"], d["Progreso"]
                    )
                elif d["tipo"] == "Profesor":
                    obj = Profesor(
                        d["Id_usuario"], d["Nombre"], d["Correo"], d["Contraseña"],
                        d["Especializacion"], d["Cursos Impartidos"], d["Calificacion"]
                    )
                lista_usuarios.append(obj)
        print("Datos cargados correctamente.")
    except FileNotFoundError:
        print("No se encontró archivo previo. Iniciando lista vacía.")
    return lista_usuarios

def menu():
    usuarios = cargar_datos()
    while True:
        print("\n--- PLATAFORMA DE CURSOS VIRTUALES ---")
        print("1. Registrar Estudiante")
        print("2. Registrar Profesor")
        print("3. Mostrar todos los usuarios")
        print("4. Buscar usuario por ID")
        print("5. Guardar y Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            
            id_u = input("ID: ")
            nom = input("Nombre: ")
            cor = input("Correo: ")
            con = input("Contraseña: ")
            
            cod = input("Código Estudiantil: ")
            cur = input("Curso: ")
            pro = input("Progreso: ")
            
            nuevo = Estudiante(id_u, nom, cor, con, cod, cur, pro)
            usuarios.append(nuevo)
            print("Estudiante agregado.")

        elif opcion == "2":
            print("\n--- Registro de Profesor ---")
            id_u = input("ID: ")
            nom = input("Nombre: ")
            cor = input("Correo: ")
            con = input("Contraseña: ")
            
           
            esp = input("Especialización: ")
            cur = input("Cursos Impartidos: ")
            cal = input("Calificación: ")
            
            nuevo = Profesor(id_u, nom, cor, con, esp, cur, cal)
            usuarios.append(nuevo)
            print("Profesor agregado exitosamente.")

        elif opcion == "3":
            for u in usuarios:
                u.mostrar_perfil() 

        elif opcion == "4":
            id_buscada = input("Ingrese el ID del usuario a buscar: ")
            encontrado = False
            
            for u in usuarios:
                if u.get_id_usuario() == id_buscada:
                    print("\n--- Usuario Encontrado ---")
                    u.mostrar_perfil()
                    encontrado = True
                    break 
            
            if not encontrado:
                print("Error: No se encontró ningún usuario con ese ID.") 

        elif opcion == "5":
            guardar_datos(usuarios)
            break


if __name__ == "__main__":
    menu()