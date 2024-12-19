class FoodInfo:
    def __init__(self, proteins, fats, carbohydrates):
        self.proteins = proteins
        self.fats = fats
        self.carbohydrates = carbohydrates

    def __repr__(self):
        return f"FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})"

    def __str__(self):
        return f"Кол-во белков: {self.proteins}, кол-во жиров: {self.fats}, кол-во углеводов: {self.carbohydrates}"

    def __add__(self, other):
        if isinstance(other, FoodInfo):
            return FoodInfo(
                self.proteins + other.proteins,
                self.fats + other.fats,
                self.carbohydrates + other.carbohydrates
            )
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            return FoodInfo(
                self.proteins * n,
                self.fats * n,
                self.carbohydrates * n
            )
        return NotImplemented

    def __truediv__(self, n):
        if isinstance(n, (int, float)) and n != 0:
            return FoodInfo(
                self.proteins / n,
                self.fats / n,
                self.carbohydrates / n
            )
        return NotImplemented

    def __floordiv__(self, n):
        if isinstance(n, (int, float)) and n != 0:
            return FoodInfo(
                self.proteins // n,
                self.fats // n,
                self.carbohydrates // n
            )
        return NotImplemented

food1 = FoodInfo(10, 5, 20)
food2 = FoodInfo(15, 10, 25)

food_sum = food1 + food2
print(food_sum)

food_mul = food1 * 2
print(food_mul)

food_div = food1 / 2
print(food_div)

food_floordiv = food1 // 3
print(food_floordiv)