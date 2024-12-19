#В условии задачи пишется использовать @property поэтому я отказался от методов set_name и get_name и т.д
class User:
    def __init__(self, name, age):
        if not self.__check_name(name):
            raise ValueError("Некорректное имя")
        if not self.__check_age(age):
            raise ValueError("Некорректный возраст")

        self.__name = name
        self._age = age


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if self.__check_name(new_name):
            self.__name = new_name
        else:
            raise ValueError("Некорректное имя")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if self.__check_age(new_age):
            self._age = new_age
        else:
            raise ValueError("Некорректный возраст")

    @staticmethod
    def __check_name(name):
        if isinstance(name, str) and name and all(i.isalpha() for i in name):
            return True
        return False

    @staticmethod
    def __check_age(age):
        if isinstance(age, int) and 0 <= age <= 110:
            return True
        return False

    def __str__(self):
        return f'Имя: {self.__name}\nВозраст: {self._age}'

user1 = User('Рома', 18)
print(user1)

user1.name = 'Иван'
user1.age = 100

print(user1)