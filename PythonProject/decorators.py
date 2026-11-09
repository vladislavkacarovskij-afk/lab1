def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Декоратор спрацював перед викликом функції!")
        result = func(*args, **kwargs)
        print("Декоратор спрацював після виклику функції!")
        return result
    return wrapper