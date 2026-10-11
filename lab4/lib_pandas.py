import pandas as pd # Підключаємо pandas під псевдонімом pd

def run(): # Оголошуємо функцію запуску модуля
    df = pd.DataFrame({"Мова": ["Python"], "Оцінка": [10]}) # Створюємо таблицю DataFrame
    print(f"  - pandas: Розмір таблиці = {df.shape}") # Виводимо розмірність таблиці