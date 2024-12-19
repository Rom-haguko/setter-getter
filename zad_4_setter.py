class Word:
    def __init__(self, word):
        if not self.__check_word(word):
            raise ValueError('Неверно введены данные')
        else:
            self.word = word

    def __str__(self):
        return f'{self.word.capitalize()}'

    def __repr__(self):
        return f"Word('<{self.word}>')"

    def __eq__(self, other):
        if isinstance(other, Word):
            return len(self.word) == len(other.word)
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Word):
            return len(self.word) != len(other.word)
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Word):
            return len(self.word) < len(other.word)
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Word):
            return len(self.word) <= len(other.word)
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Word):
            return len(self.word) > len(other.word)
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Word):
            return len(self.word) >= len(other.word)
        return NotImplemented

    @staticmethod
    def __check_word(wd):
        return isinstance(wd, str) and wd and all(c.isalpha() for c in wd)





pt1 = Word('woRD')
pt2 = Word('o')
print(pt1)
print(repr(pt1))

print(pt1 == pt2)
print(pt1 != pt2)

print(pt1 > pt2)
print(pt1 >= pt2)

print(pt1 < pt2)
print(pt1 <= pt2)
