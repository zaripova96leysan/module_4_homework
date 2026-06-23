import pytest
from product import Product, Category


@pytest.fixture(autouse=True)
def reset_counters():
    Category.category_count = 0
    Category.product_count = 0
    Category.total_products = 0
    Product.total_products = 0


def test_new_product():
    data = {"name": "Phone", "description": "Smartphone", "price": 500, "quantity": 10}
    product = Product.new_product(data)
    assert product.name == "Phone"
    assert product.price == 500


def test_new_product_with_duplicate():
    existing = [Product("TV", "Old", 1000, 2)]
    data = {"name": "TV", "description": "New", "price": 1200, "quantity": 3}
    updated = Product.new_product(data, existing)
    assert updated is existing[0]
    assert updated.quantity == 5
    assert updated.price == 1200


def test_add_product():
    category = Category("Electronics", "Devices", [])
    product = Product("TV", "Big screen", 1000, 5)
    category.add_product(product)
    assert len(category._Category__products) == 1
    assert Category.total_products == 1


def test_category_products_getter():
    p1 = Product("Laptop", "Gaming", 1200, 3)
    p2 = Product("Mouse", "Wireless", 50, 10)
    category = Category("Electronics", "Gadgets", [p1, p2])
    expected = "Laptop, 1200 руб. Остаток: 3 шт.\nMouse, 50 руб. Остаток: 10 шт.\n"
    assert category.products == expected


def test_price_setter_positive():
    product = Product("Phone", "Smart", 500, 10)
    product.price = 600
    assert product.price == 600


def test_price_setter_negative(capsys):
    product = Product("Phone", "Smart", 500, 10)
    product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 500


def test_price_setter_decrease_confirmed(monkeypatch):
    product = Product("Phone", "Smart", 500, 10)
    monkeypatch.setattr('builtins.input', lambda _: 'y')
    product.price = 400
    assert product.price == 400


def test_price_setter_decrease_canceled(monkeypatch, capsys):
    product = Product("Phone", "Smart", 500, 10)
    monkeypatch.setattr('builtins.input', lambda _: 'n')
    product.price = 400
    captured = capsys.readouterr()
    assert "Изменение цены отменено" in captured.out
    assert product.price == 500


def test_private_price_access():
    product = Product("Phone", "Smart", 500, 10)
    with pytest.raises(AttributeError):
        print(product.__price)


def test_private_products_access():
    category = Category("Electronics", "Gadgets", [])
    with pytest.raises(AttributeError):
        print(category.__products)


def test_total_products_counter():
    category = Category("Fruits", "Fresh", [])
    apple = Product("Apple", "Red", 10, 50)
    banana = Product("Banana", "Yellow", 15, 30)
    category.add_product(apple)
    category.add_product(banana)
    assert Category.total_products == 2
