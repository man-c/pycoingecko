import pytest
import requests.exceptions
import responses
import unittest
import unittest.mock as mock

from pycoingecko import CoinGeckoAPI
from requests.exceptions import HTTPError


class TestWrapper(unittest.TestCase):

    @responses.activate
    def test_connection_error(self):
        with pytest.raises(requests.exceptions.ConnectionError):
            CoinGeckoAPI().ping()

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


    #---------- SIMPLE ----------#

    #---------- /simple/price ----------#
    @responses.activate
    def test_get_price(self):
        # Arrange
        coins_json_sample = {"bitcoin": {"usd": 7984.89}}

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd',
                          json = coins_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_price('bitcoin', 'usd')

        ## Assert
        assert response == coins_json_sample

    @responses.activate
    def test_failed_get_price(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_price('bitcoin', 'usd')

    #---------- /simple/token_price/{id} ----------#
    @responses.activate
    def test_get_token_price(self):
        # Arrange
        coins_json_sample = {'0xB8c77482e45F1F44dE1745F52C74426C631bDD52': {'bnb': 1.0, 'bnb_market_cap': 144443301.0, 'bnb_24h_vol': 17983938.686249834, 'last_updated_at': 1558704332}}

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/simple/token_price/ethereum?include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true&contract_addresses=0xB8c77482e45F1F44dE1745F52C74426C631bDD52&vs_currencies=bnb',
                          json = coins_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_token_price('ethereum', '0xB8c77482e45F1F44dE1745F52C74426C631bDD52', 'bnb', include_market_cap='true', include_24hr_vol='true', include_last_updated_at='true')

        ## Assert
        assert response == coins_json_sample

    @responses.activate
    def test_failed_get_token_price(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/simple/token_price/ethereum?include_market_cap=true&include_24hr_vol=true&include_last_updated_at=true&contract_addresses=0xB8c77482e45F1F44dE1745F52C74426C631bDD52&vs_currencies=bnb',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_token_price('ethereum', '0xB8c77482e45F1F44dE1745F52C74426C631bDD52', 'bnb', include_market_cap='true', include_24hr_vol='true', include_last_updated_at='true')

    #---------- /simple/supported_vs_currencies ----------#
    @responses.activate
    def test_get_supported_vs_currencies(self):
        # Arrange
        coins_json_sample = ['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau']

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/simple/supported_vs_currencies',
                          json = coins_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_supported_vs_currencies()

        ## Assert
        assert response == coins_json_sample

    @responses.activate
    def test_failed_get_supported_vs_currencies(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/simple/supported_vs_currencies',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_supported_vs_currencies()


    #---------- /simple/supported_vs_currencies ----------#
    @responses.activate
    def test_get_supported_vs_currencies(self):
        # Arrange
        coins_json_sample = ['btc', 'eth', 'ltc', 'bch', 'bnb', 'eos', 'xrp', 'xlm', 'usd', 'aed', 'ars', 'aud', 'bdt', 'bhd', 'bmd', 'brl', 'cad', 'chf', 'clp', 'cny', 'czk', 'dkk', 'eur', 'gbp', 'hkd', 'huf', 'idr', 'ils', 'inr', 'jpy', 'krw', 'kwd', 'lkr', 'mmk', 'mxn', 'myr', 'nok', 'nzd', 'php', 'pkr', 'pln', 'rub', 'sar', 'sek', 'sgd', 'thb', 'try', 'twd', 'uah', 'vef', 'vnd', 'zar', 'xdr', 'xag', 'xau']

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/simple/supported_vs_currencies',
                          json = coins_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_supported_vs_currencies()

        ## Assert
        assert response == coins_json_sample

    @responses.activate
    def test_failed_get_supported_vs_currencies(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/simple/supported_vs_currencies',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_supported_vs_currencies()


    #---------- COINS ----------#

    #---------- /price/coins ----------#
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


    #---------- /price/coins/list ----------#
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


    #---------- /price/coins/markets ----------#
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


    #---------- /price/coins/{id} ----------#
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


    #---------- /price/coins/{id}/tickers ----------#
    @responses.activate
    def test_failed_get_coin_ticker_by_id(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/bitcoin/tickers',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_coin_ticker_by_id('bitcoin')


    @responses.activate
    def test_get_get_coin_ticker_by_id(self):
        # Arrange
        bitcoin_json_sample = {'name': 'Bitcoin', 'tickers': [{'base': 'BTC', 'target': 'USDT', 'market': {'name': 'BW.com', 'identifier': 'bw', 'has_trading_incentive': False}, 'last': 7963.0, '    volume': 93428.7568, 'converted_last': {'btc': 0.99993976, 'eth': 31.711347, 'usd': 7979.23}, 'converted_volume': {'btc': 93423, 'eth': 2962752, 'usd': 745489919}, '    bid_ask_spread_percentage': 0.111969, 'timestamp': '2019-05-24T11:20:14+00:00', 'is_anomaly': False, 'is_stale': False, 'trade_url': 'https://www.bw.com/trade/btc_us    dt', 'coin_id': 'bitcoin'}]}

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/bitcoin/tickers',
                          json = bitcoin_json_sample, status = 200)

        # Act
        response = CoinGeckoAPI().get_coin_ticker_by_id('bitcoin')

        ## Assert
        assert response == bitcoin_json_sample


    #---------- /price/coins/{id}/history ----------#
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


    #---------- /price/coins/{id}/market_chart ----------#
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


    #---------- /price/coins/{id}/status_updates ----------#
    # @responses.activate
    # def test_failed_get_coin_status_updates_by_id(self):
    #     # Arrange
    #     responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/litecoin/status_updates',
    #                       status = 404)
    #     exception = HTTPError("HTTP Error")
    #
    #     # Act Assert
    #     with pytest.raises(HTTPError) as HE:
    #         CoinGeckoAPI().get_coin_status_updates_by_id('litecoin')
    #
    #
    # @responses.activate
    # def test_get_coin_status_updates_by_id(self):
    #     # Arrange
    #     json_response = [ {'description': 'Travala.com Partners with Litecoin Foundation to Champion Crypto Payments. \r\n#TravelWithLitecoin www.travala.com/litecoin\r\n\r\nRead the full announcement here: bit.ly/2LumY3b', 'category': 'general', 'created_at': '2019-05-14T13:56:43.282Z', 'user': 'Keith Yong', 'user_title': 'Operations Director', 'pin': False, 'project': {'type': 'Coin', 'id': 'litecoin', 'name': 'Litecoin', 'symbol': 'ltc', 'image': {'thumb': 'https://assets.coingecko.com/coins/images/2/thumb/litecoin.png?1547033580', 'small': 'https://assets.coingecko.com/coins/images/2/small/litecoin.png?1547033580', 'large': 'https://assets.coingecko.com/coins/images/2/large/litecoin.png?1547033580'}}} ]
    #
    #     responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/litecoin/status_updates',
    #                       json = json_response, status = 200)
    #
    #     # Act
    #     response = CoinGeckoAPI().get_coin_status_updates_by_id('litecoin')
    #
    #     ## Assert
    #     assert response == json_response


    #---------- /price/coins/{id}/contract/{contract_address} ----------#
    @responses.activate
    def test_failed_get_coin_info_from_contract_address_by_id(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/ethereum/contract/0x0D8775F648430679A709E98d2b0Cb6250d2887EF',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_coin_info_from_contract_address_by_id(id='ethereum',contract_address='0x0D8775F648430679A709E98d2b0Cb6250d2887EF')


    @responses.activate
    def test_get_coin_info_from_contract_address_by_id(self):
        # Arrange
        json_response = {'id': '0x', 'symbol': 'zrx', 'name': '0x', 'block_time_in_minutes': 0, 'categories': ['Protocol'], 'localization': {'en': '0x', 'es': '0x', 'de': '0x', 'nl': '0x', 'pt': '0x', 'fr': '0x', 'it': '0x', 'hu': '0x', 'ro': '0x', 'sv': '0x', 'pl': '0x', 'id': '0x', 'zh': '0x协议', 'zh-tw': '0x協議', 'ja': 'ロエックス', 'ko': '제로엑스', 'ru': '0x', 'ar': '0x', 'th': '0x', 'vi': '0x', 'tr': '0x'}}

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/coins/ethereum/contract/0x0D8775F648430679A709E98d2b0Cb6250d2887EF',
                          json = json_response, status = 200)

        # Act
        response = CoinGeckoAPI().get_coin_info_from_contract_address_by_id(id='ethereum',contract_address='0x0D8775F648430679A709E98d2b0Cb6250d2887EF')

        ## Assert
        assert response == json_response


    #---------- EXCHANGES ----------#


    #---------- /exchanges ----------#
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


    #---------- /exchanges/list ----------#
    @responses.activate
    def test_failed_get_exchanges_id_name_list(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/exchanges/list',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_exchanges_id_name_list()


    @responses.activate
    def test_get_exchanges_id_name_list(self):
        # Arrange
        json_response = [{'id': 'abcc', 'name': 'ABCC'}, {'id': 'acx', 'name': 'ACX'}, {'id': 'airswap', 'name': 'AirSwap'}]

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/exchanges/list',
                          json = json_response, status = 200)

        # Act
        response = CoinGeckoAPI().get_exchanges_id_name_list()

        ## Assert
        assert response == json_response



    #---------- /exchanges/{id} ----------#
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


    #---------- EXCHANGE RATES ----------#

    #---------- /exchange_rates ----------#
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
    
    #---------- TRENDING ----------#

    #---------- /search/trending ----------#
    @responses.activate
    def test_failed_search_get_trending(self):
        # Arrange
        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/search/trending',
                          status = 404)
        exception = HTTPError("HTTP Error")

        # Act Assert
        with pytest.raises(HTTPError) as HE:
            CoinGeckoAPI().get_search_trending()


    @responses.activate
    def test_get_search_trending(self):
        # Arrange
        json_response = { "coins": [{"item": {"id":"iris-network", "name":"IRISnet", "symbol":"IRIS", "market_cap_rank":159, "thumb":"/coins/images/5135/thumb/IRIS.png", "score":0}}, {"item": {"id":"hegic", "name":"Hegic", "symbol":"HEGIC", "market_cap_rank":386, "thumb":"/coins/images/12454/thumb/Hegic.png", "score":1}}, {"item": {"id":"moonswap", "name":"MoonSwap", "symbol":"MOON", "market_cap_rank":373, "thumb":"/coins/images/12441/thumb/moon.jpg", "score":2}}, {"item": {"id":"yfv-finance", "name":"YFValue", "symbol":"YFV", "market_cap_rank":179, "thumb":"/coins/images/12198/thumb/yfv.jpg", "score":3}}, {"item": {"id":"yffi-finance", "name":"yffi finance", "symbol":"YFFI", "market_cap_rank":531, "thumb":"/coins/images/11940/thumb/yffi-finance.jpg", "score":4}}, {"item": {"id":"relevant", "name":"Relevant", "symbol":"REL", "market_cap_rank":915, "thumb":"/coins/images/11586/thumb/Relevant.png", "score":5}}, {"item": {"id":"sake-token", "name":"SakeToken", "symbol":"SAKE", "market_cap_rank":503, "thumb":"/coins/images/12428/thumb/sake.png", "score":6}}], "exchanges": [] }

        responses.add(responses.GET, 'https://api.coingecko.com/api/v3/search/trending',
                          json = json_response, status = 200)

        # Act
        response = CoinGeckoAPI().get_search_trending()

        ## Assert
        assert response == json_response

    #---------- GLOBAL ----------#

    #---------- /global ----------#
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



    # #---------- FINANCE ----------#
    #
    # #---------- /finance_platforms ----------#
    #
    # @responses.activate
    # def test_failed_get_finance_platforms(self):
    #     # Arrange
    #     responses.add(responses.GET, 'https://api.coingecko.com/api/v3/finance_platforms',
    #                       status = 404)
    #     exception = HTTPError("HTTP Error")
    #
    #     # Act Assert
    #     with pytest.raises(HTTPError) as HE:
    #         CoinGeckoAPI().get_finance_platforms()
    #
    # @responses.activate
    # def test_get_finance_platforms(self):
    #     # Arrange
    #     json_response = [{"name": "Binance Lending", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Celsius Network", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Compound Finance", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "dYdX", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Nexo", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Staked US", "facts": "", "category": "", "centralized": False, "website_url": "https://staked.us/"}, {"name": "Cobo", "facts": "", "category": "", "centralized": False, "website_url": "https://cobo.com/"}, {"name": "Crypto.com", "facts": "", "category": "", "centralized": True, "website_url": "https://crypto.com/en/"}]
    #
    #     responses.add(responses.GET, 'https://api.coingecko.com/api/v3/finance_platforms',
    #                       json = json_response, status = 200)
    #
    #     # Act
    #     response = CoinGeckoAPI().get_finance_platforms()
    #
    #     ## Assert
    #     expected_response = [{"name": "Binance Lending", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Celsius Network", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Compound Finance", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "dYdX", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Nexo", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Staked US", "facts": "", "category": "", "centralized": False, "website_url": "https://staked.us/"}, {"name": "Cobo", "facts": "", "category": "", "centralized": False, "website_url": "https://cobo.com/"}, {"name": "Crypto.com", "facts": "", "category": "", "centralized": True, "website_url": "https://crypto.com/en/"}]
    #     assert response == expected_response
    #
    # #---------- /finance_products ----------#
    #
    # @responses.activate
    # def test_failed_get_finance_products(self):
    #     # Arrange
    #     responses.add(responses.GET, 'https://api.coingecko.com/api/v3/finance_products',
    #                       status = 404)
    #     exception = HTTPError("HTTP Error")
    #
    #     # Act Assert
    #     with pytest.raises(HTTPError) as HE:
    #         CoinGeckoAPI().get_finance_products()
    #
    # @responses.activate
    # def test_get_finance_products(self):
    #     # Arrange
    #     json_response = [{"name": "Binance Lending", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Celsius Network", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Compound Finance", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "dYdX", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Nexo", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Staked US", "facts": "", "category": "", "centralized": False, "website_url": "https://staked.us/"}, {"name": "Cobo", "facts": "", "category": "", "centralized": False, "website_url": "https://cobo.com/"}, {"name": "Crypto.com", "facts": "", "category": "", "centralized": True, "website_url": "https://crypto.com/en/"}]
    #
    #     responses.add(responses.GET, 'https://api.coingecko.com/api/v3/finance_platforms',
    #                       json = json_response, status = 200)
    #
    #     # Act
    #     response = CoinGeckoAPI().get_finance_platforms()
    #
    #     ## Assert
    #     expected_response = [{"name": "Binance Lending", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Celsius Network", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Compound Finance", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "dYdX", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Nexo", "facts": "", "category": "", "centralized": False, "website_url": ""}, {"name": "Staked US", "facts": "", "category": "", "centralized": False, "website_url": "https://staked.us/"}, {"name": "Cobo", "facts": "", "category": "", "centralized": False, "website_url": "https://cobo.com/"}, {"name": "Crypto.com", "facts": "", "category": "", "centralized": True, "website_url": "https://crypto.com/en/"}]
    #     assert response == expected_response
