from .base_page import BasePage



class CartPage(BasePage):

    USER_STREET = '[data-test="street"]'
    USER_CITY = '[data-test="city"]'
    USER_STATE = '[data-test="state"]'
    USER_COUNTRY = '[data-test="country"]'
    USER_POSTAL_CODE = '[data-test="postal_code"]'

    BUTTON_IN_CART_1 = '[data-test="proceed-1"]'
    BUTTON_IN_CART_2 = '[data-test="proceed-2"]'
    BUTTON_IN_CART_3 = '[data-test="proceed-3"]'
    BUTTON_IN_CART_4 = '[data-test="finish"]'

    PAYMENT_METHOD = '[data-test="payment-method"]'
    PAYMENT_SUCCESS = '[data-test="payment-success-message"]'
    ORDER_MESSAGE = '[id="order-confirmation"]'

    CREDIT_CARD_NUMBER = '[data-test="credit_card_number"]'
    CREDIT_EXPIRATION_DATE = '[data-test="expiration_date"]'
    CREDIT_CARD_CVV = '[data-test="cvv"]'
    CREDIT_CARD_HOLDER_NAME = '[data-test="card_holder_name"]'
    PAYMENT_ERROR_MESSAGE = '[data-test="payment-error-message"]'

    BANK_NAME = '[data-test="bank_name"]'
    ACCOUNT_NAME = '[data-test="account_name"]'
    ACCOUNT_NUMBER = '[data-test="account_number"]'

    MONTHLY_INSTALLMENTS = '[data-test="monthly_installments"]'

    GIFT_CARD_NUMBER = '[data-test="gift_card_number"]'
    GIFT_CODE = '[data-test="validation_code"]'


    async def cart_checkout(self):
        await self.click(self.BUTTON_IN_CART_1)

    async def cart_singing(self):
        await self.click(self.BUTTON_IN_CART_2)

    async def cart_form_address(self, user_street:str, user_city:str, user_state:str, user_country:str, user_postal_code:str):
        await self.page.fill(self.USER_STREET, user_street)
        await self.page.wait_for_timeout(1000)
        await self.page.fill(self.USER_CITY, user_city)
        await self.page.wait_for_timeout(1000)
        await self.page.fill(self.USER_STATE, user_state)
        await self.page.wait_for_timeout(1000)
        await self.page.fill(self.USER_COUNTRY, user_country)
        await self.page.wait_for_timeout(1000)
        await self.page.fill(self.USER_POSTAL_CODE, user_postal_code)
        await self.page.wait_for_timeout(1000)
        await self.click(self.BUTTON_IN_CART_3)

    async def cart_payment_cash(self):
        await self.page.select_option(self.PAYMENT_METHOD, value="cash-on-delivery")
        await self.click(self.BUTTON_IN_CART_4)


    async def cart_payment_credit_card(self, credit_card_number:str, credit_expiration_date:str, credit_card_cvv:str, credit_card_holder:str):
        await self.page.select_option(self.PAYMENT_METHOD, value="credit-card")
        await self.page.fill(self.CREDIT_CARD_NUMBER, credit_card_number)
        await self.page.wait_for_timeout(1000)
        await self.page.fill(self.CREDIT_EXPIRATION_DATE, credit_expiration_date)
        await self.page.wait_for_timeout(1000)
        await self.page.fill(self.CREDIT_CARD_CVV, credit_card_cvv)
        await self.page.wait_for_timeout(1000)
        await self.page.fill(self.CREDIT_CARD_HOLDER_NAME, credit_card_holder)
        await self.page.wait_for_timeout(1000)
        # await self.take_screenshot("credit_card_info")
        await self.click(self.BUTTON_IN_CART_4)


    async def cart_success_payment(self):
        await self.wait_for_element(self.PAYMENT_SUCCESS, timeout=5000)
        await self.click(self.BUTTON_IN_CART_4)

    async def cart_success_payment_order(self):
        await self.click(self.BUTTON_IN_CART_4)
        await self.wait_for_element(self.PAYMENT_SUCCESS, timeout=5000)
        await self.click(self.BUTTON_IN_CART_4)
        await self.wait_for_element(self.ORDER_MESSAGE, timeout=5000)

    async def cart_payment_bank_transfer(self, bank_name:str, account_name:str,  account_number:str):
        await self.page.select_option(self.PAYMENT_METHOD, value="bank-transfer")
        await self.page.fill(self.BANK_NAME, bank_name)
        await self.page.wait_for_timeout(1000)
        await self.page.fill(self.ACCOUNT_NAME, account_name)
        await self.page.wait_for_timeout(1000)
        await self.page.fill(self.ACCOUNT_NUMBER, account_number)
        await self.page.wait_for_timeout(1000)
        await self.click(self.BUTTON_IN_CART_4)

    async def cart_payment_buy_now_pay_later(self, value:str):
        await self.page.select_option(self.PAYMENT_METHOD, value="buy-now-pay-later")
        await self.page.select_option(self.MONTHLY_INSTALLMENTS, value)
        await self.click(self.BUTTON_IN_CART_4)


    async def cart_payment_gift_card(self, gift_card_number:str, validation_code:str):
        await self.page.select_option(self.PAYMENT_METHOD, value="gift-card")
        await self.page.fill(self.GIFT_CARD_NUMBER, gift_card_number)
        await self.page.wait_for_timeout(1000)
        await self.page.fill(self.GIFT_CODE, validation_code)
        await self.page.wait_for_timeout(1000)
        await self.click(self.BUTTON_IN_CART_4)

