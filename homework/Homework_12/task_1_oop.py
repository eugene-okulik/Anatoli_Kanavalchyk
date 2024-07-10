class Flower:
    def __init__(self, name, color, price, lifespan, freshness, stem_length):
        self.name = name
        self.color = color
        self.price = price
        self.lifespan = lifespan
        self.freshness = freshness
        self.stem_length = stem_length

    def __repr__(self):
        return f"{self.name} ({self.color}): Price={self.price}$, Lifespan={self.lifespan} days, " \
               f"Freshness={self.freshness} days, Stem length={self.stem_length} cm"


class Rose(Flower):
    def __init__(self, color, stem_length, price):
        super().__init__("Rose", color, price, 7, 3, stem_length)


class Tulip(Flower):
    def __init__(self, color, stem_length, price):
        super().__init__("Tulip", color, price, 5, 4, stem_length)


class Daisy(Flower):
    def __init__(self, color, stem_length, price):
        super().__init__("Daisy", color, price, 4, 5, stem_length)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def get_total_price(self):
        return sum(flower.price for flower in self.flowers)

    def calculate_wilt_time(self):
        if not self.flowers:
            return 0
        total_lifespan = sum(flower.lifespan for flower in self.flowers)
        return total_lifespan / len(self.flowers)

    def sort_flowers_by_freshness(self):
        self.flowers.sort(key=lambda f: f.freshness, reverse=True)

    def sort_flowers_by_color(self):
        self.flowers.sort(key=lambda f: f.color)

    def sort_flowers_by_stem_length(self):
        self.flowers.sort(key=lambda f: f.stem_length, reverse=True)

    def sort_flowers_by_price(self):
        self.flowers.sort(key=lambda f: f.price, reverse=True)

    def search_flowers_by_lifespan(self, target_lifespan):
        return [f for f in self.flowers if f.lifespan >= target_lifespan]

    def __repr__(self):
        return f"Bouquet with flowers: {self.flowers}"


# Создаем экземпляры цветов
rose_red = Rose("red", 50, 5)
rose_yellow = Rose("yellow", 45, 4)
tulip_white = Tulip("white", 40, 3.5)
tulip_pink = Tulip("pink", 35, 3)
daisy_yellow = Daisy("yellow", 25, 2)

bouquet = Bouquet()
bouquet.add_flower(rose_red)
bouquet.add_flower(rose_yellow)
bouquet.add_flower(tulip_white)
bouquet.add_flower(tulip_pink)
bouquet.add_flower(daisy_yellow)

print("Information about the bouquet:")
print(bouquet)
print()

# Стоимость букета
total_price = bouquet.get_total_price()
print(f"Total price of the bouquet: {total_price}$")
print()

# Среднее время букета
avg_wilt_time = bouquet.calculate_wilt_time()
print(f"Average wilt time of the bouquet: {avg_wilt_time:.2f} days")
print()

# Сортируем цветы
print("Sorting flowers by stem length:")
bouquet.sort_flowers_by_stem_length()
print(bouquet)
print()

print("Sorting flowers by price:")
bouquet.sort_flowers_by_price()
print(bouquet)
print()

# Поиск цветов с минимальным временем жизни
min_lifespan = 5
print(f"Finding flowers with lifespan >= {min_lifespan} days:")
found_flowers = bouquet.search_flowers_by_lifespan(min_lifespan)
if found_flowers:
    for found_flower in found_flowers:
        print(found_flower)
else:
    print("No flowers found with the specified lifespan criteria.")
