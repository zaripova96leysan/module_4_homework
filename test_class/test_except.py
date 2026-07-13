import pytest
from module_14.product import Product, Smartphone, LawnGrass, Category

def test_create_product_success():
    p = Product("Ноутбук", "Хороший ноутбук", 50000, 5)
    assert p.name == "Ноутбук"
    assert p.price == 50000
    assert p.quantity == 5

def test_create_product_zero_quantity():
    with pytest.raises(ValueError) as exc_info:
        Product("Бракованный", "Неверное количество", 1000, 0)
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"

def test_add_two_products():
    p1 = Product("Товар1", "", 100, 2)
    p2 = Product("Товар2", "", 50, 3)
    assert p1 + p2 == 350

def test_add_different_classes_raises_error():
    phone = Smartphone("iPhone", "", 1000, 1, 95, "15", 256, "black")
    grass = LawnGrass("Трава", "", 500, 2, "RU", 7, "green")
    with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
        phone + grass

def test_price_setter_negative():
    p = Product("Товар", "", 100, 1)
    p.price = -10
    assert p.price == 100

def test_new_product_creates_new():
    data = {"name": "Телефон", "description": "Смартфон", "price": 20000, "quantity": 3}
    p = Product.new_product(data)
    assert p.name == "Телефон"
    assert p.quantity == 3

def test_new_product_updates_existing():
    existing = [Product("Телефон", "", 15000, 2)]
    data = {"name": "Телефон", "price": 18000, "quantity": 1}
    updated = Product.new_product(data, existing_products=existing)
    assert updated is existing[0]
    assert updated.quantity == 3
    assert updated.price == 18000

def test_category_add_product():
    cat = Category("Электроника", "Гаджеты")
    p = Product("Ноутбук", "", 50000, 2)
    cat.add_product(p)
    # Проверяем через итератор
    assert p in list(cat)

def test_category_iterator():
    cat = Category("Тест", "Описание")
    p1 = Product("A", "", 1, 1)
    p2 = Product("B", "", 2, 1)
    cat.add_product(p1)
    cat.add_product(p2)
    names = [prod.name for prod in cat]
    assert names == ["A", "B"]