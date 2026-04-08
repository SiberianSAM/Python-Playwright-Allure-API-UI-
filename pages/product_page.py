from .base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_NAME = 'h1'
    BUTTON_ADD_TO_CART = '[data-test="add-to-cart"]'
    FIRST_PRODUCT_LINK = '[data-test^="product-"]'
    CART_ICON = '[data-test="nav-cart"]'
    BUTTON_IN_CART = '[data-test="proceed-1"]'


    async def open_first_product(self):
        await self.navigate("https://practicesoftwaretesting.com/")
        await self.wait_for_element(self.FIRST_PRODUCT_LINK)
        await self.click(self.FIRST_PRODUCT_LINK)
        await self.wait_for_element(self.PRODUCT_NAME)

    async def go_to_cart(self):
        await self.wait_for_element(self.CART_ICON, timeout=5000)
        await self.click(self.CART_ICON)
        await self.navigate("https://practicesoftwaretesting.com/checkout")
        await self.wait_for_element(self.BUTTON_IN_CART,timeout=10000)
        await self.take_screenshot("product_in_cart")

    async def add_product_to_cart(self):
        await self.wait_for_element(self.BUTTON_ADD_TO_CART, timeout=5000)
        await self.click(self.BUTTON_ADD_TO_CART)


