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


if __name__ == "__main__":
    user_manager = UserManager()

    # 1. Rendimiento: agregar 1000 usuarios
    for i in range(1000):
        user_manager.add_user(i, f"usuario:{i}")

    print(f"Total de usuarios agregados: {len(user_manager.users)}")

    # Medir tiempo de búsqueda del usuario con ID 500
    start_time = time.time()
    user_found = user_manager.find_user(500)
    end_time = time.time()
    elapsed = end_time - start_time

    print(f"Usuario 500 encontrado: {user_found}")
    print(f"Tiempo de búsqueda: {elapsed:.6f} segundos")