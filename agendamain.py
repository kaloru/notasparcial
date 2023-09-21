from dataclasses import dataclass

@dataclass # Decorator
class User:
    id : str
    name : str
    age : int

    def show_data (self):
        return f"ID: {self.id} \nNombre: {self.name} \nEdad: {self.age}"
    
if __name__ == '__main__':
    usuario1 = User("1", "Juan", 18)
    usuario2 = User("2", "Pedro", 20)
    usuario3 = User("3", "Maria", 19)
    usuario4 = User("4", "Jose", 21)
    usuarios = []
    usuarios.append(usuario1)
    
    #usuarios = [usuario1, usuario2, usuario3, usuario4]
    for usuario in usuarios:
        print (usuario.show_data())
        print ("-------------------------")
