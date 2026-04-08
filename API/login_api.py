from API.base_api import BaseAPI
import allure

class LoginAPI(BaseAPI):
    @allure.step("Логин пользователя")
    async def login(self, correct_data):
        return await self.post("/users/login", data=correct_data)

    @allure.step("Регистрация нового пользователя")
    async def register(self, new_user_data):
        return await self.post("/users/register", data=new_user_data)

    @allure.step("Получение информации об авторизированном пользователе")
    async def get_me(self):
        return await self.get("/users/me")

    @allure.step("Получение информации обо всех пользователях (только для адмнистратора)")
    async def get_all_users(self, token: str):
        return await self.get(
            "/users",
            headers={"Authorization": f"Bearer {token}"}
        )

    @allure.step("Удалить пользователя по ID (только для адмнистратора)")
    async def delete_user(self, user_id: str):
        return await self.delete(f"/users/{user_id}")