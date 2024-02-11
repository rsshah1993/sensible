from abc import ABC, abstractclassmethod
from dataclasses import dataclass
from sensible.data.base import DataBase


@dataclass
class Credentials:
    # TODO: turn this into something secure
    username: str
    password: str


class BrokerBase(ABC):
    def __init__(self, credentials: Credentials) -> None:
        self.credentials = credentials

    @abstractclassmethod
    def connect(self) -> None: ...

    @abstractclassmethod
    def get_data(self, data: DataBase) -> DataBase: ...
