import datetime # Підключаємо вбудовану бібліотеку дати та часу

def run(): # Оголошуємо функцію запуску модуля
    now = datetime.datetime.now() # Отримуємо поточну системну дату та час
    print(f"  - datetime: Час = {now.strftime('%Y-%m-%d %H:%M:%S')}") # Форматуємо і виводимо час