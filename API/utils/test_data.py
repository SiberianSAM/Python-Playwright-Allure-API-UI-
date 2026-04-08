
# Если передавать пустую строку или строку с проблеми, система расценивает
# это как запрос к /products/ и выдает все товары
INVALID_ID =[
    "01KN8QZ7K11E2MM4XR35JWK3P", #25 символов
    "01KN8QZ7K11E2MM4XR35JWK3PX1", #27 символов
    "1", #1 симоввол
    "0 1 K N 8 Q Z 7 K 1 1 E 2 M", # пробелы
    "00000000000000000000000000", #26 символов
    "id-with-dashes",
    "id with spaces",
    "id.with.dots",
    "id@with$special#chars",
    "1234567890" * 10,  # очень длинный ID
    "null",
    "undefined"
]

sql_injections = [
    "'; DROP TABLE products; --",
    "' OR '1'='1",
    "1; DELETE FROM products WHERE '1'='1",
    "' UNION SELECT * FROM users --",
]
