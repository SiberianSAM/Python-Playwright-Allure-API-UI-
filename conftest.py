import pytest
from playwright.async_api import async_playwright, APIRequestContext
from API.token_storage import load_token
from API.products_api import ProductsAPI
from API.login_api import LoginAPI

# UI
@pytest.fixture(scope="function")
async def page():
    async with async_playwright() as p:
        # browser = await p.chromium.launch(headless=False, slow_mo=150)
        browser = await p.chromium.launch()
        context = await browser.new_context()
        page = await context.new_page()
        yield page
        await context.close()
        await browser.close()

# API
@pytest.fixture(scope="function")
async def api_request_context():
    async with async_playwright() as p:
        token = load_token()

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
        }


        if token:
            headers["Authorization"] = f"Bearer {token}"
            print(f"Authorization header добавлен: {token[:20]}...")
        else:
            print("Authorization header отсутствует")

        request_context = await p.request.new_context(
            base_url="https://api.practicesoftwaretesting.com",
            extra_http_headers=headers
        )
        yield request_context
        await request_context.dispose()


@pytest.fixture
def products_api(api_request_context):
    return ProductsAPI(api_request_context)

@pytest.fixture
async def login_api(api_request_context):
    return LoginAPI(api_request_context)