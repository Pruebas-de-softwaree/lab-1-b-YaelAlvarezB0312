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

    def average_user_id(self):
        if not self.users:   # manejo de lista vacía
            return None
        return sum([u["id"] for u in self.users]) / len(self.users)


if __name__ == "__main__":
    user_manager = UserManager()

    print("=== PRUEBA DE ROBUSTEZ ===")

    # 1. Intentar eliminar un usuario que no existe
    try:
        user_manager.delete_user(9999)  # no existe
        print("Eliminar usuario inexistente: NO generó error ")
    except Exception as e:
        print("Eliminar usuario inexistente: ERROR ", e)

    # 2. Calcular average_user_id en lista vacía
    try:
        avg = user_manager.average_user_id()
        print(f"average_user_id en lista vacía: {avg} (NO error) ")
    except Exception as e:
        print("average_user_id en lista vacía: ERROR ", e)