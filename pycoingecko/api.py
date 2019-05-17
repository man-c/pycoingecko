import json
import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from .utils import get_comma_separated_values


class CoinGeckoAPI:

    __API_URL_BASE = 'https://api.coingecko.com/api/v3/'

    def __init__(self, api_base_url = __API_URL_BASE):
        self.api_base_url = api_base_url
        self.request_timeout = 120

        self.session = requests.Session()
        retries = Retry(total=5, backoff_factor=0.5, status_forcelist=[ 502, 503, 504 ])
        self.session.mount('http://', HTTPAdapter(max_retries=retries))


    def __request(self, url, params=None):
        try:
            response = self.session.get(url, params=params, timeout=self.request_timeout)
            response.raise_for_status()
            content = json.loads(response.content.decode('utf-8'))
            return content
        except Exception as e:
            raise


    #---------- PING ----------#
    def ping(self):
        """Check API server status"""

        api_url = '{0}ping'.format(self.api_base_url)
        return self.__request(api_url)


    #---------- SIMPLE ----------#
    def get_price(self, ids, vs_currencies, **params):
        """Get the current price of any cryptocurrencies in any other supported currencies that you need"""

        params.update({
            'ids': get_comma_separated_values(ids),
            'vs_currencies': get_comma_separated_values(vs_currencies),
        })

        api_url = '{0}simple/price'.format(self.api_base_url)

        return self.__request(api_url, params)

    def get_token_price(self, id, contract_addresses, vs_currencies, **params):
        """Get the current price of any tokens on this coin (ETH only at this stage as per api docs) in any other supported currencies that you need"""

        params.update({
            'contract_addresses': get_comma_separated_values(contract_addresses),
            'vs_currencies': get_comma_separated_values(vs_currencies),
        })

        api_url = '{0}simple/token_price/{1}'.format(self.api_base_url, id)
        return self.__request(api_url, params)


    def get_supported_vs_currencies(self, **params):
        """Get list of supported_vs_currencies"""

        api_url = '{0}simple/supported_vs_currencies'.format(self.api_base_url)
        return self.__request(api_url, params)


    #---------- COINS ----------#
    def get_coins(self, **params):
        """List all coins with data (name, price, market, developer, community, etc)"""

        api_url = '{0}coins'.format(self.api_base_url)
        #['order', 'per_page', 'page', 'localization']

        return self.__request(api_url, params)


    def get_coins_list(self, **params):
        """List all supported coins id, name and symbol (no pagination required)"""

        api_url = '{0}coins/list'.format(self.api_base_url)
        return self.__request(api_url, params)


    def get_coins_markets(self, vs_currency, **params):
        """List all supported coins price, market cap, volume, and market related data (no pagination required)"""

        params.update({'vs_currency': vs_currency})

        api_url = '{0}coins/markets'.format(self.api_base_url)
        return self.__request(api_url, params)


    def get_coin_by_id(self, id, **params):
        """Get current data (name, price, market, ... including exchange tickers) for a coin"""

        api_url = '{0}coins/{1}/'.format(self.api_base_url, id)
        return self.__request(api_url, params)


    def get_coin_ticker_by_id(self, id, **params):
        """Get coin tickers (paginated to 100 items)"""

        api_url = '{0}coins/{1}/tickers'.format(self.api_base_url, id)
        return self.__request(api_url, params)


    def get_coin_history_by_id(self, id, date, **params):
        """Get historical data (name, price, market, stats) at a given date for a coin"""

        params.update({'date': date})

        api_url = '{0}coins/{1}/history'.format(self.api_base_url, id)
        return self.__request(api_url, params)


    def get_coin_market_chart_by_id(self, id, vs_currency, days, **params):
        """Get historical market data include price, market cap, and 24h volume (granularity auto)"""

        params.update({
            "vs_currency": vs_currency,
            "days": days,
        })
        api_url = '{0}coins/{1}/market_chart'.format(self.api_base_url, id)

        return self.__request(api_url, params)


    def get_coin_status_updates_by_id(self, id, **params):
        """Get status updates for a given coin"""

        api_url = '{0}coins/{1}/status_updates'.format(self.api_base_url, id)

        return self.__request(api_url, params)


    def get_coin_info_from_contract_address_by_id(self, id, contract_address, **params):
        """Get coin info from contract address"""

        api_url = '{0}coins/{1}/contract/{2}'.format(self.api_base_url, id, contract_address)

        return self.__request(api_url, params)


    #---------- EXCHANGES ----------#
    def get_exchanges_list(self, **params):
        """List all exchanges"""

        api_url = '{0}exchanges'.format(self.api_base_url)
        return self.__request(api_url, params)


    def get_exchanges_id_name_list(self, **params):
        """List all supported markets id and name (no pagination required)"""

        api_url = '{0}exchanges/list'.format(self.api_base_url)
        return self.__request(api_url, params)


    def get_exchanges_by_id(self, id, **params):
        """Get exchange volume in BTC and tickers"""

        api_url = '{0}exchanges/{1}'.format(self.api_base_url, id)
        return self.__request(api_url, params)


    def get_exchanges_tickers_by_id(self, id, **params):
        """Get exchange tickers (paginated)"""

        api_url = '{0}exchanges/{1}/tickers'.format(self.api_base_url, id)
        return self.__request(api_url, params)


    def get_exchanges_status_updates_by_id(self, id, **params):
        """Get status updates for a given exchange"""

        api_url = '{0}exchanges/{1}/status_updates'.format(self.api_base_url, id)
        return self.__request(api_url, params)


    #---------- STATUS UPDATES ----------#
    def get_status_updates(self, **params):
        """List all status_updates with data (description, category, created_at, user, user_title and pin)"""

        api_url = '{0}status_updates'.format(self.api_base_url)
        return self.__request(api_url, params)


    #---------- EVENTS ----------#
    def get_events(self, **params):
        """Get events, paginated by 100"""

        api_url = '{0}events'.format(self.api_base_url)
        return self.__request(api_url, params)


    def get_events_countries(self, **params):
        """Get list of event countries"""

        api_url = '{0}events/countries'.format(self.api_base_url)
        return self.__request(api_url, params)


    def get_events_types(self, **params):
        """Get list of event types"""

        api_url = '{0}events/types'.format(self.api_base_url)
        return self.__request(api_url, params)


    #---------- EXCHANGE-RATES ----------#
    def get_exchange_rates(self, **params):
        """Get BTC-to-Currency exchange rates"""

        api_url = '{0}exchange_rates'.format(self.api_base_url)
        return self.__request(api_url, params)


    #---------- GLOBAL ----------#
    def get_global(self, **params):
        """Get cryptocurrency global data"""

        api_url = '{0}global'.format(self.api_base_url)
        return self.__request(api_url, params)['data']
