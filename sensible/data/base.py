from abc import ABC, abstractclassmethod
from pathlib import Path
from sensible.data.tickers import Ticker
from sensible.brokers.base import BrokerBase
from datetime import datetime


class DataBase(ABC):
    def __init__(
        self, ticker: Ticker, broker: BrokerBase, cache_dir: Path = Path(".cache/")
    ) -> None:
        self.ticker: Ticker = ticker
        self.cache_dir: Path = cache_dir
        self.broker: BrokerBase = broker

    @abstractclassmethod
    def get_data(self, start_date: datetime, end_date: datetime) -> None: ...
