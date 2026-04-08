from .base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = 'input[type="email"]'
    PASS_INPUT = 'input[type="password"]'
    BUTTON = '[data-test="login-submit"]'
    ERROR = '.help-block'
    ACCOUNT_INFO = '[data-test="page-title"]'
    PASSWORD_ERROR = '[data-test="password-error"]'
    EMAIL_ERROR = '[data-test="email-error"]'


    async def open(self):
        await self.navigate("https://practicesoftwaretesting.com/auth/login")

    async def login(self, email:str, password:str):
        await self.page.fill(self.EMAIL_INPUT, email)
        await self.page.wait_for_timeout(1000)
        await self.page.fill(self.PASS_INPUT, password)
        await self.page.wait_for_timeout(1000)
        await self.page.locator(self.BUTTON).click()
        await self.page.wait_for_load_state("networkidle")

    async def account_page(self):
        await self.page.wait_for_selector(self.ACCOUNT_INFO, timeout=10000)

    async def get_current_url(self):
        return self.page.url

    async def get_error(self):
        return self.page.locator(self.ERROR)

    async def get_password_error(self):
        await self.page.wait_for_selector(self.PASSWORD_ERROR)
        return self.page.locator(self.PASSWORD_ERROR)

    async def get_email_error(self):
        await self.page.wait_for_selector(self.EMAIL_ERROR)
        return self.page.locator(self.EMAIL_ERROR)