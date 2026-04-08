from datetime import datetime
import allure
from allure_commons.types import AttachmentType

class BasePage:

    def __init__(self, page):
        self.page = page

    async def navigate(self, url:str):
        await self.page.goto(url)
        await self.page.wait_for_load_state()
        # await self.take_screenshot()

    async def take_screenshot(self, name: str = None):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/{name}_{timestamp}.png" if name else f"screenshots/{timestamp}.png"

        # Для локального сохранения
        # await self.page.screenshot(path=filename, full_page=True)

        screenshot = await self.page.screenshot(full_page=True)

        # Прикрепляем к Allure отчету
        allure.attach(
            screenshot,
            name=f"{name}_{timestamp}" if name else f"screenshot_{timestamp}",
            attachment_type=AttachmentType.PNG
        )


    async def click(self, selector: str):
        await self.wait_for_element(selector)
        await self.page.click(selector)

    async def wait_for_element(self, selector: str, timeout = 10000):
        await self.page.wait_for_selector(selector, timeout=timeout)



