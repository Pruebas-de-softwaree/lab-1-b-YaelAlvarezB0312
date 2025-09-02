import time

class UserManager:
    def __init__(self):   
        self.users = []  

    def add_user(self, user_id, name):
        self.users.append({"id": user_id, "name": name})

    def find_user(self, user_id):
        user = None
        for u in self.users:
            if u["id"] == user_id:
                user = u
        return user  

    def delete_user(self, user_id):
        for u in self.users:
            if u["id"] == user_id:
                self.users.remove(u)
                break  

    def get_all_names(self):
        return [u["id"] for u in self.users]

    def average_user_id(self):
        if not self.users:   
            return None
        return sum([u["id"] for u in self.users]) / len(self.users)


if __name__ == "__main__":   
    user_manager = UserManager()

    # RNF1: Manejar hasta 1000 usuarios
    for i in range(1000): 
        user_manager.add_user(i, f"yo soy el num:{i}")

    print(f"Total de usuarios agregados: {len(user_manager.users)}\n")

    # Buscar algunos usuarios de prueba
    for i in [0, 500, 999]:
        user_found = user_manager.find_user(i)
        print(f"Usuario {i} encontrado:", user_found)

    # Eliminar algunos usuarios de prueba
    for i in [0, 500, 999]:
        user_manager.delete_user(i)
        user_found = user_manager.find_user(i)
        print(f"Usuario {i} tras eliminar:", user_found)

    # Calcular promedio de IDs
    print("\nPromedio de IDs actuales:", user_manager.average_user_id())

print("end")