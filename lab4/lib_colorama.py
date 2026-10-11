from colorama import Fore, Style, init # Імпортуємо кольори та ініціалізатор з colorama

def run(): # Оголошуємо функцію запуску модуля
    init(autoreset=True) # Ініціалізуємо colorama з автоскиданням стилю
    print(f"  - colorama: {Fore.GREEN}Зелений текст!{Style.RESET_ALL}") # Виводимо зелений текст