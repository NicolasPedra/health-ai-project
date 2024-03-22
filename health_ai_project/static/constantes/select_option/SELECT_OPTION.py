from typing import Final, List

class SELECT_OPTION:
    VALOR: str
    NOME: str

    def __init__(self, valor, nome):
        self.VALOR = valor
        self.NOME = nome

BIRADS_USG: Final[List[SELECT_OPTION]] = [
    SELECT_OPTION("0", "BI-RADS 3"),
    SELECT_OPTION("1", "BI-RADS 4a"),
    SELECT_OPTION("2", "BI-RADS 4b"),
    SELECT_OPTION("3", "BI-RADS 4c"),
    SELECT_OPTION("4", "BI-RADS 5"),
]

BIRADS_MAMOGRAFIA: Final[List[SELECT_OPTION]] = [
    SELECT_OPTION("0", "BI-RADS 0"),
    SELECT_OPTION("1", "BI-RADS 1"),
    SELECT_OPTION("2", "BI-RADS 2"),
    SELECT_OPTION("3", "BI-RADS 3"),
    SELECT_OPTION("4", "BI-RADS 4"),
    SELECT_OPTION("5", "BI-RADS 5"),
]