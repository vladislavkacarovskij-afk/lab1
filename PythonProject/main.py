# Імпортуємо декоратор з першого файлу
from decorators import my_decorator


# Використовуємо декоратор для нашої функції з варіанту
@my_decorator
def get_data():
    # Наприклад, ваша функція повертає кортеж за завданням
    return (10, 20, 30)


if __name__ == "__main__":
    # Викликаємо функцію
    result_tuple = get_data()
    print("Повернений результат:", result_tuple)

    # Якщо за завданням треба перетворити кортеж на список:
    result_list = list(result_tuple)
    print("Перетворений список:", result_list)