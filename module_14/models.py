class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    def __str__(self):
        return f'Название продукта, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        return self.price * self.quantity + other.price * other.quantity



class Category:
    # 1. Общие атрибуты класса
    category_count = 0
    product_count = 0

    # 2. Обычные атрибуты с типами
    name: str
    description: str

    def __init__(self, name, description, products):
        # 3. Личные атрибуты
        self.name = name
        self.description = description
        self.__products = products


        Category.category_count += 1
        Category.product_count += len(self.__products)


        def add_product(self, product):
            self.__products.append(product)
            Category.product_count += 1

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
