from typing import List
from random import randint
import pandas as pd

inteiros: List[int] = [randint(0, 100) for i in range(1, 10)]
reais: List[float] = [i * 4.2 for i in range(1, 10)]

matriz: List[list[int]] = [[4, 1, 5], [7, 8, 9]]

dataframe: pd.DataFrame = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
print(dataframe)


def concatenar(a: str, b: str) -> str:
    return a + b


def somar(a: float, b: float) -> float:
    return a + b


lista_inteiros = List[int]
dicionario_inteiros = dict[str, lista_inteiros]

dici_list: dicionario_inteiros = {
    'a': [1, 2, 6],
    'b': [4, 6, 7],
    'c': 's'
}

print(dici_list)
