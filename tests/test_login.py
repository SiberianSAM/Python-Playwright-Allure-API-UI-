import pytest
from pages.login_page import LoginPage
from playwright.async_api import expect
import allure

@pytest.fixture
def login_data():
    return {
        "correct_data" : ('customer2@practicesoftwaretesting.com', 'welcome01'),
        "incorrect_data" : ('test54@random.com', 'LSOT)kwy1'),
        "empty_password" : ('customer2@practicesoftwaretesting.com', ''),
        "empty_login" : ('', 'welcome01'),
        "space_only" : ('     ', '     '),
        "big_data" : ('customer2customer2customer2customer2customer2customer2customer2customer2customer2customer2customer2c@practicesoftwaretesting.com',
                      'F3qAnxIkJN48ZlAJHV7RZmrHc5wVVTaSoe4OExrMonBjctcoi1YVealtVdthw6is7BQ2ZRJ2YlWkkp5RVpDqsxwz6l9auKXvH6XbWxvOSSDUzb8EUOfr9O1uzJQQJaEh')
    }


@allure.feature("Sign in")
@allure.story("Login")
@allure.title("Успешный вход")
@pytest.mark.positive
@pytest.mark.asyncio
async def test_successful_login(page, login_data):

    login_page = LoginPage(page)
    with allure.step("Поля логин и пароль заполенны валидными значениями"):
        await login_page.open()
        await login_page.login(*login_data["correct_data"])
        await login_page.account_page()
        await login_page.take_screenshot("success_login")

        current_url = await login_page.get_current_url()
        assert current_url == 'https://practicesoftwaretesting.com/account'


@allure.feature("Sign in")
@allure.story("Login")
@allure.title("Вход с неверным логином")
@pytest.mark.negative
@pytest.mark.asyncio
async def test_wrong_login(page, login_data):

    login_page = LoginPage(page)
    with allure.step("Поле логин заполенно невалидными данными"):
        await login_page.open()
        await login_page.login(*login_data["incorrect_data"])


        error = await login_page.get_error()
        await expect(error).to_be_visible()
        await login_page.take_screenshot("incorrect_login")
        await expect(error).to_have_text("Invalid email or password")


@allure.feature("Sign in")
@allure.story("Login")
@allure.title("Вход с пустым паролем")
@pytest.mark.negative
@pytest.mark.asyncio
async def test_empty_password(page, login_data):

    login_page = LoginPage(page)

    with allure.step("Поле логин заполнено корректно, поле пароль пустое"):
        await login_page.open()
        await login_page.login(*login_data["empty_password"])

        error = await login_page.get_password_error()
        await expect(error).to_be_visible()
        await login_page.take_screenshot("empty_password")
        await expect(error).to_have_text("Password is required")


@allure.feature("Sign in")
@allure.story("Login")
@allure.title("Вход с пустым логином")
@pytest.mark.negative
@pytest.mark.asyncio
async def test_empty_login(page, login_data):

    login_page = LoginPage(page)

    with allure.step("Поле логин пустое, пароль заполнен"):
        await login_page.open()
        await login_page.login(*login_data["empty_login"])

        email_error = await login_page.get_email_error()
        await expect(email_error).to_be_visible()
        await login_page.take_screenshot("empty_login")
        await expect(email_error).to_have_text("Email is required")


@allure.feature("Sign in")
@allure.story("Login")
@allure.title("Логин и пароль заполненым пробелами")
@pytest.mark.negative
@pytest.mark.asyncio
async def test_login_with_spaces_only(page, login_data):

    login_page = LoginPage(page)

    with allure.step("Поля логин и пароль заполняются пробелами"):
        await login_page.open()
        await login_page.login(*login_data["space_only"])

        email_error = await login_page.get_email_error()
        await expect(email_error).to_be_visible()
        await login_page.take_screenshot("only_space")
        await expect(email_error).to_have_text("Email is required")


@allure.feature("Sign in")
@allure.story("Login")
@allure.title("Вход при помощи SQL инъекции")
@pytest.mark.negative
@pytest.mark.asyncio
async def test_sql_injection(page):

    login_page = LoginPage(page)

    with allure.step("Попытка использования SQL инъекции"):
        await login_page.open()
        await login_page.login("' OR '1'='1", "anything")

        email_error = await login_page.get_email_error()
        await expect(email_error).to_be_visible()
        await login_page.take_screenshot("sql_injection")
        await expect(email_error).to_have_text(" Email format is invalid")


@allure.feature("Sign in")
@allure.story("Login")
@allure.title("Вход при помощи XSS атаки")
@pytest.mark.negative
@pytest.mark.asyncio
async def test_xss_attack(page):

    login_page = LoginPage(page)

    with allure.step("Попытка входа с использованием XSS атаки"):
        await login_page.open()
        await login_page.login("<script>alert('xss')</script>", "password")

        email_error = await login_page.get_email_error()
        await expect(email_error).to_be_visible()
        await login_page.take_screenshot("xss_attack")
        await expect(email_error).to_have_text(" Email format is invalid")


@allure.feature("Sign in")
@allure.story("Login")
@allure.title("Пароль при вводе скрыт")
@pytest.mark.positive
@pytest.mark.asyncio
async def test_password_hidden(page, login_data):

    login_page = LoginPage(page)
    password_field = page.locator('input[type="password"]')

    with allure.step("Пароль при заполнении скрыт"):
        await login_page.open()
        await login_page.login(*login_data["correct_data"])

        input_type = await password_field.get_attribute('type')
        await login_page.take_screenshot("hidden_pass")
        assert input_type == 'password', f"Expected type='password', got '{input_type}'"


@allure.feature("Sign in")
@allure.story("Login")
@allure.title("Проверка максимальной длины полей логин и пароль")
@pytest.mark.negative
@pytest.mark.asyncio
async def test_max_length_fields(page, login_data):

    login_page = LoginPage(page)

    with allure.step("Поля логин и пароль заполняются длиной строки 256 символов"):
        await login_page.open()
        await login_page.login(*login_data["big_data"])

        email_error = await login_page.get_email_error()
        password_error = await login_page.get_password_error()
        await expect(email_error).to_be_visible()
        await expect(password_error).to_be_visible()
        await login_page.take_screenshot("max_length_fields")
        await expect(email_error).to_have_text("Email format is invalid")
        await expect(password_error).to_have_text("Password length is invalid")
