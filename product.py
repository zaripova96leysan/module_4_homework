class Product:
    """Товар с приватной ценой, геттером и сеттером."""
    total_products = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.total_products += 1

    @classmethod
    def new_product(cls, data: dict, existing_products=None):
        name = data["name"]
        description = data.get("description", "")
        price = data["price"]
        quantity = data["quantity"]

        if existing_products is not None:
            for prod in existing_products:
                if prod.name.lower() == name.lower():
                    prod.quantity += quantity
                    if price > prod.price:
                        prod.price = price
                    return prod

        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self.__price:
            answer = input(f"Цена снижается с {self.__price} до {value}. Подтвердите (y/n): ")
            if answer.lower() != 'y':
                print("Изменение цены отменено")
                return

        self.__price = value


class Category:
    category_count = 0
    product_count = 0
    total_products = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []

        Category.category_count += 1
        Category.product_count += len(self.__products)
        Category.total_products += len(self.__products)

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1
        Category.total_products += 1

    @property
    def products(self):
        result = ""
        for p in self.__products:
            result += f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт.\n"
        return result