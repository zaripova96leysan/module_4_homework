from abc import ABC, abstractmethod


class BaseProduct(ABC):
    def __init__(self, name, description, price, quantity, **kwargs):
        self.name = name
        self.description = description
        self._price = price
        self.quantity = quantity
        self._extra = kwargs

    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def calculate_metric(self):
        pass


class LoggingMixin:
    def __init__(self, *args, **kwargs):
        print(f"[LOG] Создаётся {self.__class__.__name__}, args={args}, kwargs={kwargs}")
        super().__init__(*args, **kwargs)


class Product(LoggingMixin, BaseProduct):
    total_products = 0

    def __init__(self, name, description, price, quantity, **kwargs):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        super().__init__(name, description, price, quantity, **kwargs)
        Product.total_products += 1

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if value < self._price:
            answer = input(
                f"Цена снижается с {self._price} до {value}. Подтвердите (y/n): "
            )
            if answer.lower() != "y":
                print("Изменение цены отменено")
                return

        self._price = value

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
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return self.price * self.quantity + other.price * other.quantity

    def get_info(self):
        return str(self)

    def calculate_metric(self):
        return self.price * self.quantity


class Smartphone(Product):
    def __init__(
        self, name, description, price, quantity, efficiency, model, memory, color
    ):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(
        self, name, description, price, quantity, country, germination_period, color
    ):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color


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
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты Product или его наследников"
            )
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