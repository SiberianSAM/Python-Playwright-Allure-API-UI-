import allure
import json
import re
import pytest
from jsonschema import validate
from API.utils.schemas import PRODUCT_SCHEMA
from API.utils.test_data import INVALID_ID
from API.utils.test_data import sql_injections
from API.utils.products_id import save_id

from Study_project.API.utils.products_id import load_id


@allure.feature("Products_API")
@allure.title("Получение всего списка товаров")
@pytest.mark.asyncio
async def test_get_all_products(products_api):
    response = await products_api.get_all_products()

    with allure.step("Проверка статуса ответа"):
        assert response.status == 200
    products = await response.json()


    # Для сохранения id первого товара
    first_prod_id = (await response.json())["data"][0]["id"]
    save_id(first_prod_id)

    assert "data" in products

    allure.attach(
        name="Response Body",
        body=json.dumps(products, indent=2, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON
    )


@allure.feature("Products_API")
@allure.title("Получение конкретного товара по ID")
@pytest.mark.asyncio
async def test_get_specific_product(products_api):

    product_id = load_id()

    with allure.step("Запрос информации о конкретном товаре по ID"):
        response = await products_api.get_product_info(product_id)
        assert response.status == 200

    product = await response.json()
    print(json.dumps(product, indent=2, ensure_ascii=False))

    validate(product, PRODUCT_SCHEMA)

    allure.attach(
        name="Product Details Response",
        body=json.dumps(product, indent=2, ensure_ascii=False),
        attachment_type=allure.attachment_type.JSON
    )

    with allure.step("Проверка соответсвия ID (ID запроса = ID ответа)"):
        assert product["id"] == product_id

    with allure.step("Проверка длины ID = 26 символов"):
        assert len(product["id"]) == 26

    with allure.step("Проверка формата ID"):
        assert re.match(r'^[A-Z0-9]+$', product["id"])


@allure.feature("Products_API")
@allure.title("Попытка получения товара по несуществующему ID")
@pytest.mark.asyncio
async def test_product_invalid_id(products_api):
    for bad_id in INVALID_ID:
        with allure.step(f"Проверить формат ID: {bad_id}"):
            response = await products_api.get_product_info(bad_id)
            assert response.status == 404, \
            f"Получен {response.status}"

        error_response = await response.json()

        allure.attach(
            name="Product Details Response",
            body=json.dumps(error_response, indent=2, ensure_ascii=False),
            attachment_type=allure.attachment_type.JSON
        )

        with allure.step("Проверка ответа об ошибке"):
            assert error_response["message"] == "Requested item not found"


@allure.feature("Products_API")
@allure.title("SQL инъекция в ID")
@pytest.mark.asyncio
async def test_sql_injection(products_api):

    with allure.step("Проверка уязвимостей SQL инъекцией"):
        for inj in sql_injections:
            response = await products_api.get_product_info(inj)

            assert response.status in [400, 404], \
                f"Для SQL инъекции ожидался 400/404, получен {response.status}"

            assert response.status != 500, \
                f"API упал с 500 при SQL инъекции: {sql_injections}"