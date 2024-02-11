from typing import Optional
import pandas as pd
from pathlib import Path
from sensible.data.tickers import Ticker


class DataBase:
    def __init__(self, ticker: Ticker, cache_dir: Path = Path(".cache/")) -> None:
        self.ticker: Ticker = ticker
        self.cache_dir: Path = cache_dir
        self._data: Optional[pd.DataFrame] = None

    @property
    def data(self) -> pd.DataFrame:
        if self._data is None:
            raise ValueError("Data is not generated")
        return self._data

    @data.setter
    def data(self, to_set: pd.DataFrame) -> None:
        if self._data is not None:
            raise ValueError("`data` attribute is already set.")
        self._data = to_set
