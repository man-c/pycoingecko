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

        # Act Assert
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

        # Act Assert
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

        # Act Assert
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

        # Act Assert
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

    @responses.activate
    def test_failed_get_coin_history_by_id(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/bitcoin/history?date=27-08-2018',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_coin_history_by_id('bitcoin', '27-08-2018')


    @responses.activate
    def test_get_coin_history_by_id(self):
        # Arrange
        history_json_sample = { "id": "bitcoin", "symbol": "btc", "name": "Bitcoin", "localization": { "en": "Bitcoin", "es": "Bitcoin", "de": "Bitcoin", "nl": "Bitcoin", "pt": "Bitcoin", "fr": "Bitcoin", "it": "Bitcoin", "hu": "Bitcoin", "ro": "Bitcoin", "sv": "Bitcoin", "pl": "Bitcoin", "id": "Bitcoin", "zh": "比特币", "zh-tw": "比特幣", "ja": "ビットコイン", "ko": "비트코인", "ru": "биткоина", "ar": "بيتكوين", "th": "บิตคอยน์", "vi": "Bitcoin", "tr": "Bitcoin" } }

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/bitcoin/history?date=27-08-2018',
                          json = history_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_coin_history_by_id('bitcoin', '27-08-2018')

        ## Assert
        assert response == history_json_sample

    @responses.activate
    def test_failed_get_coin_market_chart_by_id(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_coin_market_chart_by_id('bitcoin', 'usd', 1)


    @responses.activate
    def test_get_coin_market_chart_by_id(self):
        # Arrange
        json_response = { "prices": [ [ 1535373899623, 6756.942910425894 ], [ 1535374183927, 6696.894541693875 ], [ 1535374496401, 6689.990513793263 ], [ 1535374779118, 6668.291007556478 ], [ 1535375102688, 6703.7499879964 ], [ 1535375384209, 6706.898948451269 ] ] }

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1',
                          json = json_response, status = 200)

        # Act
        response = CoinGeckoAPI().get_coin_market_chart_by_id('bitcoin', 'usd', 1)

        ## Assert
        assert response == json_response

    @responses.activate
    def test_failed_get_exchanges_list(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/exchanges',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_exchanges_list()


    @responses.activate
    def test_get_exchanges_list(self):
        # Arrange
        json_response = [ { "id": "bitforex", "name": "Bitforex", "description": "", "url": "https://www.bitforex.com/", "image": "https://assets.coingecko.com/markets/images/214/small/bitforex.jpg?1533199114", "has_trading_incentive": "true", "trade_volume_24h_btc": 680266.637119918 }, { "id": "binance", "name": "Binance", "description": "Binance is a China-based cryptocurrency exchange that lists most of the Chinese coins. It is a popular exchange for its huge number of Initial Coin Offering (ICO) listings and low fees.", "url": "https://www.binance.com/", "image": "https://assets.coingecko.com/markets/images/52/small/binance.jpg?1519353250", "has_trading_incentive": "false", "trade_volume_24h_btc": 189744.350072168 } ]

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/exchanges',
                          json = json_response, status = 200)

        # Act
        response = CoinGeckoAPI().get_exchanges_list()

        ## Assert
        assert response == json_response

    @responses.activate
    def test_failed_get_exchanges_by_id(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/exchanges/bitforex',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_exchanges_by_id('bitforex')


    @responses.activate
    def test_get_exchanges_by_id(self):
        # Arrange
        json_response = { "name": "Bitforex", "has_trading_incentive": "true", "trade_volume_24h_btc": 680266.637119918, "tickers": [ { "base": "BTC", "target": "USDT", "market": { "name": "Bitforex", "identifier": "bitforex", "has_trading_incentive": "true" }, "last": 7039.55, "converted_last": { "btc": "1.001711841446200081963480716", "eth": "24.4986463149997536428213651518458101194944", "usd": "7043.71831205846008527901735024184383795812" }, "volume": 447378.73, "converted_volume": { "btc": "448144.5713519911718500979009072226084", "eth": "10960173.27267390510353832059421689917189597190216256", "usd": "3151209752.222085727501972469271259554059845134991788" }, "timestamp": "2018-08-28T12:46:25.719Z", "is_anomaly": "false" } ] }

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/exchanges/bitforex',
                          json = json_response, status = 200)

        # Act
        response = CoinGeckoAPI().get_exchanges_by_id('bitforex')

        ## Assert
        assert response == json_response

    @responses.activate
    def test_failed_get_exchange_rates(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/exchange_rates',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_exchange_rates()


    @responses.activate
    def test_get_exchange_rates(self):
        # Arrange
        json_response = { "rates": { "btc": { "name": "Bitcoin", "unit": "Ƀ", "value": 0, "type": "crypto" }, "eth": { "name": "Ether", "unit": "Ξ", "value": 24.451, "type": "crypto" }, "usd": { "name": "US Dollar", "unit": "$", "value": 7040.152, "type": "fiat" } } }

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/exchange_rates',
                          json = json_response, status = 200)

        # Act
        response = CoinGeckoAPI().get_exchange_rates()

        ## Assert
        assert response == json_response

    @responses.activate
    def test_failed_get_global(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/global',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_global()


    @responses.activate
    def test_get_global(self):
        # Arrange
        json_response = { "data": { "active_cryptocurrencies": 2517, "upcoming_icos": 360, "ongoing_icos": 423, "ended_icos": 2037, "markets": 197 } }

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/global',
                          json = json_response, status = 200)

        # Act
        response = CoinGeckoAPI().get_global()

        ## Assert
        expected_response = { "active_cryptocurrencies": 2517, "upcoming_icos": 360, "ongoing_icos": 423, "ended_icos": 2037, "markets": 197 }
        assert response == expected_response
