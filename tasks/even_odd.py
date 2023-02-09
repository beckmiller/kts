__all__ = (
    'even_odd',
)


def even_odd(arr: list[int]) -> float:
    """
    Функция возвращает отношение суммы четных элементов массив к сумме нечетных
    Пример:
    even_odd([1, 2, 3, 4, 5]) == 0.8889
    """
    odd = []
    not_odd = []
    for i in arr:
        if i % 2 == 0:
            odd.append(i)
        else:
            not_odd.append(i)
    return sum(odd) / sum(not_odd) if sum(not_odd) != 0 else 0
