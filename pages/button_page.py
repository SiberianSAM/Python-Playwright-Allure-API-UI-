from .base_page import BasePage


class ButtonPage(BasePage):
    SEARCH_INPUT = 'input[type="text"]'
    SEARCH_BUTTON = 'button[id="updatingButton"]'


    async def open(self):
        await self.navigate("http://uitestingplayground.com/textinput?")

    async def search(self, query:str):
        await self.page.wait_for_selector(self.SEARCH_INPUT, state="visible", timeout=10000)
        await self.page.fill(self.SEARCH_INPUT, query)
        await self.page.locator(self.SEARCH_BUTTON).click()




