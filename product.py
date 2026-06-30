class Product:
    total_products = 0

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        Product.total_products += 1

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self.__price:  # если цена понижается
            answer = input(f"Цена снижается с {self.__price} до {value}. Подтвердите (y/n): ")
            if answer.lower() != 'y':
                print("Изменение цены отменено")
                return

        self.__price = value

    @classmethod
    def new_product(cls, data, existing_products=None):
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

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        return self.price * self.quantity + other.price * other.quantity


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
            result += str(p) + "\n"
        return result

    def __str__(self):
        total = 0
        for product in self.__products:
            total += product.quantity
        return f"{self.name}, количество продуктов: {total} шт."

    def __iter__(self):
        return CategoryIterator(self.__products)


class CategoryIterator:
    def __init__(self, products):
        self.products = products
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.products):
            raise StopIteration
        product = self.products[self.index]
        self.index += 1
        return product