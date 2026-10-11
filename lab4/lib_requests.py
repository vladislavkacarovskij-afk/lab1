import requests # Підключаємо бібліотеку для HTTP-запитів

def run(): # Оголошуємо функцію запуску модуля
    try: # Початок блоку переنесення помилок
        response = requests.get("https://httpbin.org/json", timeout=3) # Робимо GET-запит на сервер
        print(f"  - requests: Статус запиту = {response.status_code}") # Виводимо статус-код відповіді
    except Exception as e: # Ловимо потенційну помилку мережі
        print(f"  - requests: Помилка -> {e}") # Виводимо текст помилки