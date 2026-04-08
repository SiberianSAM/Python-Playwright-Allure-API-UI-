import allure
import json
import pytest
from API.token_storage import save_token, load_token


# Тестовые данные
admin_data = {
    "email": "admin@practicesoftwaretesting.com",
    "password": "welcome01"
}

correct_data = {
    "email": "customer2@practicesoftwaretesting.com",
    "password": "welcome01"
}

incorrect_data = {
    "email": "custom@practicesoftwaretesting.com",
    "password": "welcome"
}

new_user_data = {
  "first_name": "Tes1",
  "last_name": "Test54",
  "address": {
    "street": "Test Street 54",
    "city": "Test city",
    "state": "Tets state",
    "country": "Test country",
    "postal_code": "540000"
  },
  "phone": "88888888",
  "dob": "2000-01-01",
  "password": "Test@test@test54",
  "email": "Test.user7@mail.ru"

}



@allure.feature("API_Login")
@allure.title("Логин пользователя и сохранение токена")
@pytest.mark.asyncio
async def test_user_login_save_token(login_api):

    response = await login_api.login(correct_data)
    assert response.status == 200

    data = await response.json()
    assert "access_token" in data

    allure.attach(
        name="Response Body",
        body=json.dumps(data, indent=2, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON
    )

    save_token(data["access_token"])


@allure.feature("API_Login")
@allure.title("Логин с неверным логином и паролем")
@pytest.mark.asyncio
async def test_invalid_login(login_api):

    response = await login_api.login(incorrect_data)
    assert response.status == 401

    json_body = await response.json()
    assert json_body["error"] == "Unauthorized"

    allure.attach(
        name="Response Body",
        body=json.dumps(json_body, indent=2, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON
    )


@allure.feature("API_Login")
@allure.title("Получение профиля по токену")
@pytest.mark.asyncio
async def test_get_me_info(login_api):
    response = await login_api.get_me()
    assert response.status == 200

    profile = await response.json()
    print(json.dumps(profile, indent=2, ensure_ascii=False),)

    allure.attach(
        name="Response Body",
        body=json.dumps(profile, indent=2, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON
    )


@allure.feature("API_Login")
@allure.title("Логин администратора и сохранение токена")
@pytest.mark.asyncio
async def test_admin_login_save_token(login_api):

    response = await login_api.login(admin_data)
    assert response.status == 200

    data = await response.json()

    allure.attach(
        name="Response Body",
        body=json.dumps(data, indent=2, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON
    )

    save_token(data["access_token"])


@allure.feature("API_Login")
@allure.title("Регистрация нового пользователя, логин и удаление пользователя")
@pytest.mark.asyncio
async def test_register_new_user_login_delete(login_api):

    with allure.step("Регистрация нового пользователя"):
        reg = await login_api.register(new_user_data)
        assert reg.status == 201, "Не удалось зарегистрировать пользователя"

        reg_data = await reg.json()
        user_id = reg_data.get("id")
        print(f"Создан пользователь с ID: {user_id}")

        allure.attach(
            name="Registration Response",
            body=json.dumps(reg_data, indent=2, ensure_ascii=False),
            attachment_type=allure.attachment_type.JSON
        )

    with allure.step("Логин с созданными учетными данными"):
        login = await login_api.login({
            "email": new_user_data["email"],
            "password": new_user_data["password"]
        })

        assert login.status == 200, "Не удалось авторизоваться с созданными данными"

        login_data = await login.json()
        assert "access_token" in login_data, "Токен не получен при авторизации"

        allure.attach(
            name="Login Response",
            body=json.dumps(login_data, indent=2, ensure_ascii=False),
            attachment_type=allure.attachment_type.JSON
        )


    with allure.step(f"Удаление пользователя с ID {user_id}"):
        print(user_id)
        delete_response = await login_api.delete_user(user_id)

        assert delete_response.status in [200, 204], (
            f"Ожидался статус 200 или 204, получен {delete_response.status}"
        )

        allure.attach(
            name="Delete User Result",
            body=f"User {user_id} successfully deleted",
            attachment_type=allure.attachment_type.TEXT
        )

    with allure.step(f"Проверка, что пользователь {user_id} удален"):
        get_response = await login_api.delete_user(user_id)
        assert get_response.status == 422, (
            f"Пользователь {user_id} должен быть удален, но получен статус {get_response.status}"
        )

        allure.attach(
            name="Verification",
            body=f"User {user_id} not found (404) - correctly deleted",
            attachment_type=allure.attachment_type.TEXT
        )


# @allure.feature("API_Login")
# @allure.title("Удаление пользователя по ID")
# @pytest.mark.asyncio
# async def test_delete_user(login_api):
#
#     user_id = '01knnw96x3qe17r8c7pw8kvwyc'
#     #
#     response = await login_api.delete_user(user_id)
#     assert response.status in [200, 204], (
#         f"Ожидался статус 200 или 204, получен {response.status}"
#     )


@allure.feature("API_Login")
@allure.title("Получение всех пользователей")
@pytest.mark.asyncio
@pytest.mark.positive
async def test_get_all_users(api_request_context):
    token = load_token()
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }
    response = await api_request_context.get("/users", data=headers)
    print(f"Status: {response.status}")

    users_data = await response.json()
    print(json.dumps(users_data, indent=2, ensure_ascii=False))

    allure.attach(
        name="Response Body",
        body=json.dumps(users_data, indent=4, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON
    )