import pytest
from module_14.product import BaseProduct, Product, Smartphone, LawnGrass, Category


def test_base_product_abstract():
    with pytest.raises(TypeError):
        BaseProduct("Тест", "Описание", 100, 5)


def test_product_creation():
    p = Product("Книга", "Толстая", 350, 10)
    assert p.name == "Книга"
    assert p.price == 350
    assert p.quantity == 10


def test_smartphone_creation():
    s = Smartphone("iPhone", "Смартфон", 1000, 2, 95, "15 Pro", 256, "черный")
    assert s.model == "15 Pro"
    assert s.efficiency == 95
    assert s.memory == 256


def test_lawn_grass_creation():
    g = LawnGrass("Газон", "Трава", 500, 10, "Россия", 7, "зеленый")
    assert g.country == "Россия"
    assert g.germination_period == 7


def test_add_same_class():
    p1 = Product("A", "desc", 100, 2)
    p2 = Product("B", "desc", 200, 3)
    assert p1 + p2 == 100 * 2 + 200 * 3


def test_add_different_classes_raises_error():
    p = Product("A", "desc", 100, 2)
    s = Smartphone("Phone", "desc", 999, 1, 85, "X", 256, "black")
    with pytest.raises(TypeError):
        p + s


def test_category_add_product():
    cat = Category("Тест", "Описание")
    p = Product("Товар", "Описание", 100, 2)
    cat.add_product(p)
    assert len(cat._Category__products) == 1


def test_category_rejects_non_product():
    cat = Category("Тест", "Описание")
    with pytest.raises(TypeError):
        cat.add_product("Строка")


def test_new_product():
    data = {"name": "Телефон", "description": "Смарт", "price": 300, "quantity": 1}
    p = Product.new_product(data)
    assert p.name == "Телефон"
    assert p.quantity == 1


def test_new_product_updates():
    existing = [Product("TV", "Old", 1000, 2)]
    data = {"name": "TV", "price": 1200, "quantity": 3}
    updated = Product.new_product(data, existing)
    assert updated is existing[0]
    assert updated.quantity == 5
    assert updated.price == 1200


def test_price_setter():
    p = Product("Товар", "Описание", 500, 1)
    p.price = -100
    assert p.price == 500  # цена не изменилась


def test_category_iterator():
    p1 = Product("A", "desc", 10, 1)
    p2 = Product("B", "desc", 20, 2)
    cat = Category("Тест", "Тест", [p1, p2])
    names = [prod.name for prod in cat]
    assert names == ["A", "B"]


def test_str_methods():
    p = Product("Книга", "Описание", 350, 10)
    assert str(p) == "Книга, 350 руб. Остаток: 10 шт."
    cat = Category("Категория", "Описание", [p])
    assert str(cat) == "Категория, количество продуктов: 10 шт."