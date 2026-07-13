from module_14.product import Smartphone, LawnGrass, Category

if __name__ == "__main__":
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством")
    else:
        print("Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством")

    print("=== Демонстрация работы проекта ===\n")

    print("1. Создаём смартфон:")
    phone = Smartphone("iPhone 15", "Смартфон", 1000, 2, 95, "15 Pro", 256, "черный")
    print(phone)

    print("\n2. Создаём траву:")
    grass = LawnGrass("Газон", "Трава", 500, 10, "Россия", 7, "зеленый")
    print(grass)

    print("\n3. Сложение двух смартфонов:")
    phone2 = Smartphone("Samsung", "Смартфон", 800, 3, 90, "S23", 128, "белый")
    result = phone + phone2
    print(f"Сумма = {result}")

    print("\n4. Попытка сложить смартфон и траву:")
    try:
        print(phone + grass)
    except TypeError as e:
        print(f"Ошибка (ожидаемо): {e}")

    print("\n5. Добавляем продукты в категорию:")
    cat = Category("Электроника", "Гаджеты")
    cat.add_product(phone)
    cat.add_product(grass)
    print(cat)
    print("Список продуктов:\n", cat.products)

    print("\n6. Информация о продукте (get_info):")
    print(phone.get_info())
    print("7. Метрика (calculate_metric):")
    print(phone.calculate_metric())

    print("\n✅ main.py работает без ошибок!")