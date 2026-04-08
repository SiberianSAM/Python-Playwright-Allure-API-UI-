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

Study_project/
├── allure-results/
├── API/                 
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_api_login.py
│   │   └── test_api_products.py
│   ├─ utils/
│   │   ├── __init__.py
│   │   ├── products_id.py
│   │   ├── schemas.py
│   │   └── test_data.py
│   ├─__init__.py
│   ├─ base_api.py 
│   ├─ login_api.py
│   ├─ products_api.py
│   └── token_storage.py
├── pages/   
├── tests/   

├── tests/               # Тесты
│   ├── conftest.py
│   └── test_products.py
├── data/                # Тестовые данные
│   └── test_data.json
├── utils/               # Утилиты
│   └── helpers.py
├── .                 # Переменные окружения
├── .gitignore
├──
├── requirements.txt
└── README.md



## Полезные команды

# Запустить только упавшие тесты
pytest --lf

# Отладка с выводом print
pytest -s
# Python-Playwright-Allure-API-UI-
