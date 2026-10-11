from bs4 import BeautifulSoup # Імпортуємо парсер BeautifulSoup з bs4

def run(): # Оголошуємо функцію запуску модуля
    html_doc = "<html><body><h1>Привіт!</h1></body></html>" # Створюємо тестовий HTML-рядок
    soup = BeautifulSoup(html_doc, 'html.parser') # Створюємо об'єкт парсингу HTML
    print(f"  - bs4: Знайдено h1 -> {soup.h1.text}") # Виводимо текст знайненого тега h1