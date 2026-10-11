import json # Підключаємо вбудований модуль для роботи з JSON

def run(): # Оголошуємо функцію запуску модуля
    data = {"lab": 4, "status": "ok"} # Створюємо звичайний словник Python
    json_str = json.dumps(data) # Конвертуємо словник у JSON-рядок
    print(f"  - json: JSON-рядок = {json_str}") # Виводимо результат у консоль