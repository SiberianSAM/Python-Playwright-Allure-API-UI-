from API.base_api import BaseAPI
import allure


class ProductsAPI(BaseAPI):
    @allure.step("Получить все товары")
    async def get_all_products(self):
        return await self.get("/products")

    @allure.step("Получить информацию о товаре по id")
    async def get_product_info(self, product_id):
        return await self.get(f"/products/{product_id}")
