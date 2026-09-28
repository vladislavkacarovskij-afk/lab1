# товари магазину
products = [
    {"name": "ноутбук", "price": 25000.00, "quantity": 5},
    {"name": "мишка", "price": 750.50, "quantity": 10},
    {"name": "клавіатура", "price": 1200.00, "quantity": 8},
    {"name": "навушники", "price": 1800.75, "quantity": 6}
]

# кошик покупця
cart = []

# дані адміністратора
ADMIN_LOGIN = "vlad"
ADMIN_PASSWORD = "2009"

# формат ціни
price_format = lambda x: f"{x:.2f} грн"


# показати каталог
def show_catalog():
    print("\n- каталог -")

    for i, product in enumerate(products, 1):
        print(
            f"{i}. {product['name']} - "
            f"{price_format(product['price'])} - "
            f"{product['quantity']} шт."
        )


# показати кошик
def show_cart():
    print("\n- кошик -")

    if not cart:
        print("кошик пустий")
        return

    total = 0

    for i, item in enumerate(cart, 1):
        cost = item["price"] * item["quantity"]
        total += cost

        print(
            f"{i}. {item['name']} - "
            f"{item['quantity']} шт. - "
            f"{price_format(cost)}"
        )

    print(f"разом: {price_format(total)}")


# додати товар
def add_to_cart():
    show_catalog()

    try:
        number = int(input("номер товару: "))
        amount = int(input("кількість: "))

        if number < 1 or number > len(products):
            print("такого товару нема")
            return

        product = products[number - 1]

        if amount <= 0 or amount > product["quantity"]:
            print("неправильна кількість")
            return

        # шукаємо товар у кошику
        item = next(
            (x for x in cart if x["name"] == product["name"]),
            None
        )

        if item:
            item["quantity"] += amount
        else:
            cart.append({
                "name": product["name"],
                "price": product["price"],
                "quantity": amount
            })

        print("товар добавлено")

    except ValueError:
        print("введіть число")


# видалити товар
def remove_from_cart():
    show_cart()

    if not cart:
        return

    try:
        number = int(input("номер товару: "))

        if 1 <= number <= len(cart):
            cart.pop(number - 1)
            print("товар видалено")
        else:
            print("неправильний номер")

    except ValueError:
        print("введіть число")


# купити товари
def buy():
    if not cart:
        print("кошик порожній")
        return

    show_cart()

    answer = input("купити? (так/ні): ").lower()

    if answer == "так":

        for item in cart:
            for product in products:
                if product["name"] == item["name"]:
                    product["quantity"] -= item["quantity"]

        cart.clear()
        print("покупку здійснено")

    else:
        print("покупку скасовано")


# вхід адміністратора
def admin():
    login = input("логін: ")
    password = input("пароль: ")

    if login == ADMIN_LOGIN and password == ADMIN_PASSWORD:

        print("\n- оставшейся -")

        # сортуємо товари по назві
        for product in sorted(
            products,
            key=lambda x: x["name"]
        ):
            print(
                f"{product['name']} - "
                f"{product['quantity']} шт."
            )

    else:
        print("неправильний логін або пароль")


# головне меню
while True:

    print("\n-магазин-")
    print("1  каталог")
    print("2  добавити в кошик")
    print("3  кошик")
    print("4  видалити з кошика")
    print("5  купити")
    print("6  адміністратор")
    print("0  вихід")

    choice = input("ваш вибір: ")

    if choice == "1":
        show_catalog()

    elif choice == "2":
        add_to_cart()

    elif choice == "3":
        show_cart()

    elif choice == "4":
        remove_from_cart()

    elif choice == "5":
        buy()

    elif choice == "6":
        admin()

    elif choice == "0":
        print("до побачення")
        break

    else:
        print("такого пункту нема")