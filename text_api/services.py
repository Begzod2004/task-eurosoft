from datetime import date, datetime
from typing import Dict

class TextService:
    _latin_to_cyril: Dict[str, str] = {
        'a': 'а', 'b': 'б', 'd': 'д', 'e': 'е', 'f': 'ф', 'g': 'г', 'h': 'ҳ',
        'i': 'и', 'j': 'ж', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н', 'o': 'о',
        'p': 'п', 'q': 'қ', 'r': 'р', 's': 'с', 't': 'т', 'u': 'у', 'v': 'в',
        'x': 'х', 'y': 'й', 'z': 'з', "'": 'ъ', 'ch': 'ч', 'sh': 'ш',
        'ya': 'я', 'yu': 'ю', 'yo': 'ё', "o'": 'ў', "g'": 'ғ'
    }

    @classmethod
    def convert_to_cyrillic(cls, text: str) -> str:
        if not text:
            return ""

        result = []
        i = 0
        text = text.lower()

        while i < len(text):
            if i + 1 < len(text):
                double_char = text[i:i+2]
                if double_char in cls._latin_to_cyril:
                    result.append(cls._latin_to_cyril[double_char])
                    i += 2
                    continue

            char = text[i]
            result.append(cls._latin_to_cyril.get(char, char))
            i += 1

        return ''.join(result)


class DateService:
    @staticmethod
    def calculate_days(birth_date: date) -> int:
        today = date.today()
        delta = today - birth_date
        return delta.days