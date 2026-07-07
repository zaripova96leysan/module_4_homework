from module_14.product import Product, Category


def test_product_init():
    product = Product("Книга", "Толстая", 350.0, 100)
    assert product.name == "Книга"
    assert product.description == "Толстая"
    assert product.price == 350.0


def test_category_init():
    product1 = Product("Книга", "Толстая", 350.0, 100)
    product2 = Product("Смартфон", "Android", 50000.0, 5)
    category = Category("Электроника", "Гаджеты", [product1, product2])

    assert category.name == "Электроника"
    assert category.description == "Гаджеты"

    first_product_name = category._Category__products[0].name
    assert first_product_name == "Книга"
