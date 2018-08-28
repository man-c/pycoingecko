import pytest
import responses
import unittest
import unittest.mock as mock

from pycoingecko import CoinGeckoAPI
from requests.exceptions import HTTPError

class TestWrapper(unittest.TestCase):

    @responses.activate
    def test_failed_ping(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/ping',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().ping()

    @responses.activate
    def test_ping(self):
        # Arrange
        ping_json = { 'gecko_says':'(V3) To the Moon!' }
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/ping',
                          json = ping_json, status = 200)

        # Act
        response = CoinGeckoAPI().ping()

        ## Assert
        assert response == ping_json

    @responses.activate
    def test_failed_get_coins(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_coins()

    @responses.activate
    def test_get_coins(self):
        # Arrange
        coins_json_sample = [ { "id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "localization": { "en": "Bitcoin", "es": "Bitcoin", "de": "Bitcoin", "nl": "Bitcoin", "pt": "Bitcoin", "fr": "Bitcoin", "it": "Bitcoin", "hu": "Bitcoin", "ro": "Bitcoin", "sv": "Bitcoin", "pl": "Bitcoin", "id": "Bitcoin", "zh": "Bitcoin", "zh-tw": "Bitcoin", "ja": "Bitcoin", "ko": "Bitcoin", "ru": "Bitcoin", "ar": "Bitcoin", "th": "Bitcoin", "vi": "Bitcoin", "tr": "Bitcoin" }, "image": { "thumb": "https://assets.coingecko.com/coins/images/1/thumb/bitcoin.png?1510040391", "small": "https://assets.coingecko.com/coins/images/1/small/bitcoin.png?1510040391", "large": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1510040391" } } ]

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins',
                          json = coins_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_coins()

        ## Assert
        assert response == coins_json_sample

    @responses.activate
    def test_failed_get_coins_list(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/list',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_coins_list()

    @responses.activate
    def test_get_coins_list(self):
        # Arrange
        coins_json_sample = [ { "id": "bitcoin", "symbol": "btc", "name": "Bitcoin" }, { "id": "litecoin", "symbol": "ltc", "name": "Litecoin" }, { "id": "auroracoin", "symbol": "aur", "name": "Auroracoin" }, { "id": "peercoin", "symbol": "ppc", "name": "Peercoin" }, { "id": "dogecoin", "symbol": "doge", "name": "Dogecoin" }, { "id": "nxt", "symbol": "nxt", "name": "NXT" }, { "id": "omni", "symbol": "omni", "name": "Omni (Mastercoin)" } ]

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/list',
                          json = coins_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_coins_list()

        ## Assert
        assert response == coins_json_sample

    @responses.activate
    def test_failed_get_coins_markets(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_coins_markets('usd')

    @responses.activate
    def test_get_coins_markets(self):
        # Arrange
        markets_json_sample = [ { "id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png?1510040391", "current_price": 7015.11823787848, "market_cap": 120934444800.105, "market_cap_rank": 1, "total_volume": 6121170828.21792, "high_24h": 7054.21193531031, "low_24h": 6668.29100755648, "price_change_24h": "299.72373285508", "price_change_percentage_24h": "4.46323343521924", "market_cap_change_24h": "5197755386.983", "market_cap_change_percentage_24h": "4.4910178555649", "circulating_supply": "17236100.0", "ath": 19665.3949272416, "ath_change_percentage": -64.2200698307594, "ath_date": "2017-12-16T00:00:00.000Z", "roi": 0, "last_updated": "2018-08-28T12:12:53.390Z" } ]

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd',
                          json = markets_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_coins_markets('usd')

        ## Assert
        assert response == markets_json_sample

    @responses.activate
    def test_failed_get_coin_by_id(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/bitcoin/',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_coin_by_id('bitcoin')


    @responses.activate
    def test_get_coin_by_id(self):
        # Arrange
        bitcoin_json_sample = { "id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "categories": [ "Cryptocurrency" ], "localization": { "en": "Bitcoin", "es": "Bitcoin", "de": "Bitcoin", "nl": "Bitcoin", "pt": "Bitcoin", "fr": "Bitcoin", "it": "Bitcoin", "hu": "Bitcoin", "ro": "Bitcoin", "sv": "Bitcoin", "pl": "Bitcoin", "id": "Bitcoin", "zh": "比特币", "zh-tw": "比特幣", "ja": "ビットコイン", "ko": "비트코인", "ru": "биткоина", "ar": "بيتكوين", "th": "บิตคอยน์", "vi": "Bitcoin", "tr": "Bitcoin"}}

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/bitcoin/',
                          json = bitcoin_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_coin_by_id('bitcoin')

        ## Assert
        assert response == bitcoin_json_sample
