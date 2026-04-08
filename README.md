# Автотесты для Practice Software Testing

UI и API тесты демо-приложения https://practicesoftwaretesting.com/

## Технологии
- Язык: Python 3.13.7
- Фреймворк: Pytest / Playwright
- Ассерты: PyTest

[//]: # (- Контейнеризация: Docker, Docker Compose)


## Установка

install --upgrade pip
pip install playwright
playwright install 
pip install pytest-asyncio
pip install allure-pytest
pip install pydantic

# Запуск всех тестов
pytest -v

# Конкретный файл
pytest tests/test_products.py

# С конкретным маркером
pytest -m positive / pytest -m negative


## Отчётность
# Для создания Allure отчёта
pytest --alluredir=allure-results     

# Запуск сервера Allure
allure serve allure-results  

## Структура проекта

```
Study_project/
├── conftest.py
├── pytest.ini
├── tests/
│   ├── test_login.py
│   ├── __init__.py
│   └── test_order.py
├── __init__.py
├── README.md
├── .gitignore
├── API/
│   ├── base_api.py
│   ├── login_api.py
│   ├── tests/
│   │   ├── test_api_login.py
│   │   ├── test_api_products.py
│   │   └── __init__.py
│   ├── __init__.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── schemas.py
│   │   ├── products_id.py
│   │   └── test_data.py
│   ├── token_storage.py
│   └── products_api.py
└── pages/
    ├── base_page.py
    ├── login_page.py
    ├── __init__.py
    ├── button_page.py
    ├── cart_page.py
    └── product_page.py
```

## Полезные команды

# Запустить только упавшие тесты
pytest --lf

# Отладка с выводом print
pytest -s
# Python-Playwright-Allure-API-UI-
