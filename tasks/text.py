from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    words = text.split()
    if not words:
        return None, None

    min_word = max_word = words[0]
    min_length = max_length = len(min_word)

    for word in words[1:]:
        word_length = len(word)
        if word_length < min_length:
            min_length = word_length
            min_word = word
        elif word_length > max_length:
            max_length = word_length
            max_word = word

    return min_word, max_word
