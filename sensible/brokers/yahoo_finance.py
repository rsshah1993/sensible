from sensible.brokers.base import BrokerBase
from sensible.data.base import DataBase
import yfinance as yf


class YahooFinance(BrokerBase):
    def get_data(self, data: DataBase) -> DataBase:
        y_ticker = yf.Ticker(data.ticker.value)
        # TODO: just testing
        data.data = y_ticker.history()
        return data

    def connect(self) -> None:
        pass
