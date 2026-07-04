import pytest
from product import Product, Category, Smartphone, LawnGrass

def test_smartphone_creation():
    s = Smartphone(
        name="iPhone",
        price=1000,
        quantity=2,
        efficiency=95,
        model="15 Pro",
        memory=256,
        color="black",
        description="Крутой смартфон"  # <-- добавили
    )
    assert s.name == "iPhone"
    assert s.model == "15 Pro"
    assert s.memory == 256
    assert s.color == "black"


def test_lawn_grass_creation():
    g = LawnGrass(
        name="Газонная трава",
        price=500,
        quantity=10,
        country="Россия",
        germination_period=14,
        color="green",
        description="Хорошая трава"  # <-- добавили
    )
    assert g.country == "Россия"
    assert g.germination_period == 14


def test_add_same_class_works():
    s1 = Smartphone("Phone A", 100, 1, 80, "X1", 64, "red", "Первый телефон")
    s2 = Smartphone("Phone B", 200, 2, 90, "Y2", 128, "blue", "Второй телефон")
    result = s1 + s2
    assert result == 100 * 1 + 200 * 2  # 500


def test_add_different_classes_raises_error():
    s = Smartphone("Phone", 100, 1, 80, "X1", 64, "red", "Телефон")
    g = LawnGrass("Grass", 50, 5, "RU", 7, "green", "Трава")
    with pytest.raises(TypeError):
        _ = s + g


def test_category_add_valid_product():
    cat = Category()
    p = Product("Обычный товар", 10, 5, "yellow", "Описание")
    cat.add_product(p)
    assert len(cat.products) == 1
    assert cat.products[0] is p


def test_category_reject_invalid_object():
    cat = Category()
    with pytest.raises(TypeError):
        cat.add_product("Это просто строка, а не товар!")