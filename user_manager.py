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


if __name__ == "__main__":
    user_manager = UserManager()

    print("=== PRUEBA DE INTEGRIDAD DE DATOS ===")

    # Agregar usuarios duplicados
    user_manager.add_user(10, "duplicado1")
    user_manager.add_user(10, "duplicado2")
    user_manager.add_user(10, "duplicado3")

    # Evaluar find_user
    print("Resultado de find_user(10):")
    print(user_manager.find_user(10))  

    # Evaluar delete_user
    user_manager.delete_user(10)
    print("\nUsuarios con ID 10 después de delete_user:")
    print([u for u in user_manager.users if u["id"] == 10])  
   