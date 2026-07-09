import pytest
from module_14.product import Product, Category, Smartphone, LawnGrass


def test_smartphone_creation():
    s = Smartphone(
        name="iPhone",
        description="Крутой смартфон",
        price=1000,
        quantity=2,
        efficiency=95,
        model="15 Pro",
        memory=256,
        color="black"
    )
    assert s.name == "iPhone"
    assert s.model == "15 Pro"
    assert s.memory == 256
    assert s.color == "black"


def test_lawn_grass_creation():
    g = LawnGrass(
        name="Газонная трава",
        description="Хорошая трава",
        price=500,
        quantity=10,
        country="Россия",
        germination_period=14,
        color="green"
    )
    assert g.country == "Россия"
    assert g.germination_period == 14


def test_add_same_class_works():
    s1 = Smartphone(
        name="Phone A",
        description="Первый телефон",
        price=100,
        quantity=1,
        efficiency=80,
        model="X1",
        memory=64,
        color="red"
    )
    s2 = Smartphone(
        name="Phone B",
        description="Второй телефон",
        price=200,
        quantity=2,
        efficiency=90,
        model="Y2",
        memory=128,
        color="blue"
    )
    result = s1 + s2
    assert result == 100 * 1 + 200 * 2   # 500


def test_add_different_classes_raises_error():
    s = Smartphone(
        name="Phone",
        description="Телефон",
        price=100,
        quantity=1,
        efficiency=80,
        model="X1",
        memory=64,
        color="red"
    )
    g = LawnGrass(
        name="Grass",
        description="Трава",
        price=50,
        quantity=5,
        country="RU",
        germination_period=7,
        color="green"
    )
    with pytest.raises(TypeError):
        _ = s + g


def test_category_add_valid_product():
    cat = Category("Тестовая категория", "Для теста")
    p = Product("Обычный товар", "Описание", 10, 5)
    cat.add_product(p)
    assert len(cat._Category__products) == 1
    assert cat._Category__products[0] is p


def test_category_reject_invalid_object():
    cat = Category("Тестовая категория", "Для теста")
    with pytest.raises(TypeError):
        cat.add_product("Это просто строка, а не товар!")
