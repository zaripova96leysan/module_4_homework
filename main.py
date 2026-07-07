from module_14.product import Smartphone, LawnGrass, Category

if __name__ == "__main__":
    phone = Smartphone("iPhone", "Смартфон", 1000, 2, 95, "15 Pro", 256, "черный")
    grass = LawnGrass("Газон", "Трава", 500, 10, "Россия", 7, "зеленый")
    cat = Category("Тест", "Описание")
    cat.add_product(phone)
    cat.add_product(grass)
    print("✅ Всё работает!")