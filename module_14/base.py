from product import Product, Smartphone, LawnGrass, Category

if __name__ == "__main__":
    p = Product("Универсальный товар", "Описание", 100, 5)
    print(p.get_info())
    print("Метрика:", p.calculate_metric())
    print()

    s = Smartphone(
        name="PhoneX",
        description="Смартфон",
        price=999,
        quantity=10,
        efficiency=85,
        model="X10",
        memory=256,
        color="black"
    )
    print(s.get_info())
    print("Метрика:", s.calculate_metric())
    print()

    g = LawnGrass(
        name="Газонная смесь",
        description="Трава",
        price=150,
        quantity=20,
        country="Россия",
        germination_period=14,
        color="зелёный"
    )
    print(g.get_info())
    print("Метрика:", g.calculate_metric())