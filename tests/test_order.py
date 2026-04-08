import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.cart_page import CartPage
from playwright.async_api import expect
import allure


@pytest.fixture
def user_data():
    return {
        "auth" : ('customer2@practicesoftwaretesting.com', 'welcome01'),
        "address" : ('Test street 54', 'Test city 54', 'Test state 54', 'Test country 54', '540000'),
        "credit_card" : ('1234-1234-1234-1234', '01/2030', '111', 'Alanna Morissette'),
        "bank_transfer" : ('Sberbank', 'Test user', '5401234'),
        "gift_card" : ('12345678', '12abc3d')
    }


@pytest.fixture
async def cart_with_items(page, user_data):
    login_page = LoginPage(page)
    product_page = ProductPage(page)
    cart_page = CartPage(page)

    await login_page.open()
    await login_page.login(*user_data["auth"])
    await login_page.account_page()

    await product_page.open_first_product()
    await product_page.add_product_to_cart()
    await product_page.go_to_cart()

    await cart_page.cart_checkout()
    await cart_page.cart_singing()
    await cart_page.cart_form_address(*user_data["address"])

    return cart_page


@allure.feature("Checkout")
@allure.story("Payment")
@allure.title("Оплата наличными")
@pytest.mark.positive
@pytest.mark.asyncio
async def test_successful_order_cash_on_delivery(page, cart_with_items):
    cart = cart_with_items
    with allure.step("Выбор оплаты наличными"):
        await cart.cart_payment_cash()
        await cart.take_screenshot("choice_cash")

    with allure.step("Подтверждение заказа"):
        await cart.cart_success_payment()
        await cart.cart_success_payment_order()
        await cart.take_screenshot("successful_order_cash_on_delivery")
        success_element = page.locator('[id="order-confirmation"]')
        await expect(success_element).to_contain_text("Thanks for your order! Your invoice number is", timeout=5000)


@allure.feature("Checkout")
@allure.story("Payment")
@allure.title("Оплата кредитной картой")
@pytest.mark.positive
@pytest.mark.asyncio
async def test_successful_order_credit_card(page, cart_with_items, user_data):
    cart = cart_with_items
    with allure.step("Выбор оплаты кредитной картой"):
        await cart.cart_payment_credit_card(*user_data["credit_card"])
        await cart.take_screenshot("choice_credit_card")

    with allure.step("Подтверждение заказа"):
        await cart.cart_success_payment_order()
        await cart.take_screenshot("successful_order_credit_card")

        success_element = page.locator('[id="order-confirmation"]')
        await expect(success_element).to_contain_text("Thanks for your order! Your invoice number is", timeout=5000)


@allure.feature("Checkout")
@allure.story("Payment")
@allure.title("Оплата банковским переводом")
@pytest.mark.positive
@pytest.mark.asyncio
async def test_successful_order_bank_transfer(page, cart_with_items, user_data):
    cart = cart_with_items
    with allure.step("Выбор оплаты банковский перевод"):
        await cart.cart_payment_bank_transfer(*user_data["bank_transfer"])
        await cart.take_screenshot("choice_bank_transfer")

    with allure.step("Подтверждение заказа"):
        await cart.cart_success_payment_order()
        await cart.take_screenshot("successful_order_bank_transfer")

        success_element = page.locator('[id="order-confirmation"]')
        await expect(success_element).to_contain_text("Thanks for your order! Your invoice number is", timeout=5000)


@allure.feature("Checkout")
@allure.story("Payment")
@allure.title("Купить сейчас оплатить позже")
@pytest.mark.positive
@pytest.mark.asyncio
async def test_successful_buy_now_pay_later(page, cart_with_items):

    value = '3'
    # value = '6'
    # value = '9'
    # value = '12'

    cart = cart_with_items
    with allure.step("Выбор оплатить позже"):
        await cart.cart_payment_buy_now_pay_later(value)
        await cart.take_screenshot("choice_pay_later")

    with allure.step("Подтверждение заказа"):
        await cart.cart_success_payment_order()
        await cart.take_screenshot("successful_buy_now_pay_later")

        success_element = page.locator('[id="order-confirmation"]')
        await expect(success_element).to_contain_text("Thanks for your order! Your invoice number is", timeout=5000)


@allure.feature("Checkout")
@allure.story("Payment")
@allure.title("Оплата подарочной картой")
@pytest.mark.positive
@pytest.mark.asyncio
async def test_successful_order_gift_card(page, cart_with_items, user_data):
    cart = cart_with_items
    with allure.step("Выбор оплаты подарочной картой"):
        await cart.cart_payment_gift_card(*user_data["gift_card"])
        await cart.take_screenshot("choice_gift_card")

    with allure.step("Подтверждение заказа"):
        await cart.cart_success_payment_order()
        await cart.take_screenshot("successful_gift_card")

        success_element = page.locator('[id="order-confirmation"]')
        await expect(success_element).to_contain_text("Thanks for your order! Your invoice number is", timeout=5000)

