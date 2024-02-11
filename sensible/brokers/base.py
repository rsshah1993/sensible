from abc import ABC, abstractclassmethod
from dataclasses import dataclass


@dataclass
class Credentials:
    # TODO: turn this into something secure
    username: str
    password: str


class BrokerBase(ABC):
    def __init__(self, credentials: Credentials) -> None:
        self.credentials = credentials

    @abstractclassmethod    
    def connect(self) -> None:
        ...
