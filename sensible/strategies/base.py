from abc import ABC, abstractclassmethod
from sensible.data.base import DataBase


class StrategyBase(ABC):
    def __init__(self) -> None:
        pass

    @abstractclassmethod
    def strategy(self) -> None: ...

    @abstractclassmethod
    def backtest(self, data: DataBase) -> None: ...
