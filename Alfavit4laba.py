import string

class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    _letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return self._letters_num

    @staticmethod
    def example():
        return "ГЫ"


alphabet = EngAlphabet()
alphabet.print()
print(alphabet.letters_num())
print(alphabet.is_en_letter('F'))
print(alphabet.is_en_letter('G'))
print(EngAlphabet.example())
