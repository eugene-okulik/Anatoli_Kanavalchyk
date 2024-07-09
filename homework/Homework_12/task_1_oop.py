class Flower:
    def __init__(self, name, color, price, lifespan, freshness, stem_length):
        self.name = name
        self.color = color
        self.price = price
        self.lifespan = lifespan
        self.freshness = freshness
        self.stem_length = stem_length

    def __repr__(self):
        return (f"{self.name} ({self.color}) - {self.price}$, "
                f"Lifespan: {self.lifespan} days, Freshness: {self.freshness} days, "
                f"Stem length: {self.stem_length} cm")


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def get_total_price(self):
        return sum(flower.price for flower in self.flowers)

    def get_avg_lifespan(self):
        if not self.flowers:
            return 0
        return sum(flower.lifespan for flower in self.flowers) / len(self.flowers)

    def sort_flowers(self, key):
        self.flowers.sort(key=lambda flower: getattr(flower, key))

    def find_flowers_by_lifespan(self, lifespan_threshold):
        return [flower for flower in self.flowers if flower.lifespan >= lifespan_threshold]

    def __repr__(self):
        return f"Bouquet with flowers: {self.flowers}"


# Экземпляры цветов
rose_red = Flower("Rose", "red", 5, 7, 2, 50)
rose_yellow = Flower("Rose", "yellow", 4, 6, 3, 45)
tulip_orange = Flower("Tulip", "orange", 3, 5, 1, 30)
tulip_pink = Flower("Tulip", "pink", 3.5, 6, 2, 35)
daisy_white = Flower
