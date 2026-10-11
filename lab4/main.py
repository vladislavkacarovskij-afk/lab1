import sys  # Підключаємо системний модуль для роботи з шляхами
import os  # Підключаємо модуль взаємодії з операційною системою

sys.path.append(os.path.dirname(os.path.abspath(__file__)))  # Додаємо поточну папку в шляхи пошуку модулів Python

from lib_math import run as run_math  # Імпортуємо функцію з файлу math під псевдонімом
from lib_random import run as run_random  # Імпортуємо функцію з файлу random
from lib_datetime import run as run_datetime  # Імпортуємо функцію з файлу datetime
from lib_os import run as run_os  # Імпортуємо функцію з файлу os
from lib_json import run as run_json  # Імпортуємо функцію з файлу json

from lib_requests import run as run_requests  # Імпортуємо функцію з файлу requests
from lib_colorama import run as run_colorama  # Імпортуємо функцію з файлу colorama
from lib_rich import run as run_rich  # Імпортуємо функцію з файлу rich
from lib_bs4 import run as run_bs4  # Імпортуємо функцію з файлу beautifulsoup4
from lib_pillow import run as run_pillow  # Імпортуємо функцію з файлу pillow
from lib_numpy import run as run_numpy  # Імпортуємо функцію з файлу numpy
from lib_pandas import run as run_pandas  # Імпортуємо функцію з файлу pandas
from lib_matplotlib import run as run_matplotlib  # Імпортуємо функцію з файлу matplotlib
from lib_sympy import run as run_sympy  # Імпортуємо функцію з файлу sympy
from lib_click import run as run_click  # Імпортуємо функцію з файлу click (замість pygame)


def main():  # Оголошуємо головну функцію програми
    print("=" * 50)  # Виводимо декоративну лінію в консоль
    print("       ЗАПУСК ЛАБОРАТОРНОЇ РОБОТИ №4")  # Виводимо заголовок
    print("=" * 50)  # Виводимо декоративну лінію

    print("\n[INFO] Вбудовані бібліотеки:")  # Інформаційне повідомлення
    run_math()  # Викликаємо функцію math
    run_random()  # Викликаємо функцію random
    run_datetime()  # Викликаємо функцію datetime
    run_os()  # Викликаємо функцію os
    run_json()  # Викликаємо функцію json

    print("\n[INFO] Сторонні бібліотеки:")  # Інформаційне повідомлення
    run_requests()  # Викликаємо функцію requests
    run_colorama()  # Викликаємо функцію colorama
    run_rich()  # Викликаємо функцію rich
    run_bs4()  # Викликаємо функцію bs4
    run_pillow()  # Викликаємо функцію pillow
    run_numpy()  # Викликаємо функцію numpy
    run_pandas()  # Викликаємо функцію pandas
    run_matplotlib()  # Викликаємо функцію matplotlib
    run_sympy()  # Викликаємо функцію sympy
    run_click()  # Викликаємо функцію click

    print("\n" + "=" * 50)  # Виводимо декоративну лінію
    print(" Усі модулі виконано успішно!")  # Повідомлення про завершення
    print("=" * 50)  # Виводимо декоративну лінію


if __name__ == "__main__":  # Перевіряємо, чи файл запущено напряму
    main()  # Запускаємо головну функцію