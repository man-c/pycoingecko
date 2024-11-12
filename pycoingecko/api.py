import json
import requests

from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

from .utils import func_args_preprocessing


class CoinGeckoAPI:
    __API_URL_BASE = 'https://api.coingecko.com/api/v3/'
    __PRO_API_URL_BASE = 'https://pro-api.coingecko.com/api/v3/'

    def __init__(self, api_key: str = '', retries=5, demo_api_key: str = ''):

        self.extra_params = None
        # self.headers = None
        if api_key:
            self.api_base_url = self.__PRO_API_URL_BASE
            self.extra_params = {'x_cg_pro_api_key': api_key}
            # self.headers = {"accept": "application/json",
            #                 "x-cg-pro-api-key": api_key}
        else:
            self.api_base_url = self.__API_URL_BASE
            if demo_api_key:
                self.extra_params = {'x_cg_demo_api_key': demo_api_key}
                # self.headers = {"accept": "application/json",
                #                 "x-cg-demo-api-key": demo_api_key}

        self.request_timeout = 120

        self.session = requests.Session()
        retries = Retry(total=retries, backoff_factor=0.5, status_forcelist=[502, 503, 504])
        self.session.mount('https://', HTTPAdapter(max_retries=retries))

        # self.session.headers = self.headers

    def __request(self, url, params):
        # if using pro or demo version of CoinGecko with api key, inject key in every call
        if self.extra_params is not None:
            params.update(self.extra_params)

        try:
            response = self.session.get(url, params=params, timeout=self.request_timeout)
        except requests.exceptions.RequestException:
            raise

        try:
            response.raise_for_status()
            # self._headers = response.headers
            content = json.loads(response.content.decode('utf-8'))
            return content
        except Exception as e:
            # check if json (with error message) is returned
            try:
                content = json.loads(response.content.decode('utf-8'))
                raise ValueError(content)
            # if no json
            except json.decoder.JSONDecodeError:
                pass

            raise

    # def __api_url_params(self, api_url, params, api_url_has_params=False):
    #     # if using pro version of CoinGecko, inject key in every call
    #     if self.api_key:
    #         params['x_cg_pro_api_key'] = self.api_key
    #
    #     if params:
    #         # if api_url contains already params and there is already a '?' avoid
    #         # adding second '?' (api_url += '&' if '?' in api_url else '?'); causes
    #         # issues with request parametes (usually for endpoints with required
    #         # arguments passed as parameters)
    #         api_url += '&' if api_url_has_params else '?'
    #         for key, value in params.items():
    #             if type(value) == bool:
    #                 value = str(value).lower()
    #
    #             api_url += "{0}={1}&".format(key, value)
    #         api_url = api_url[:-1]
    #     return api_url

    # ---------- PING ----------#
    def ping(self, **kwargs):
        """Check API server status"""

        api_url = '{0}ping'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- KEY ----------#
    def key(self, **kwargs):
        """Monitor your account's API usage, including rate limits, monthly total credits, remaining credits, and more"""

        api_url = '{0}key'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- SIMPLE ----------#
    @func_args_preprocessing
    def get_price(self, ids, vs_currencies, **kwargs):
        """Get the current price of any cryptocurrencies in any other supported currencies that you need"""

        ids = ids.replace(' ', '')
        kwargs['ids'] = ids
        vs_currencies = vs_currencies.replace(' ', '')
        kwargs['vs_currencies'] = vs_currencies

        api_url = '{0}simple/price'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_token_price(self, id, contract_addresses, vs_currencies, **kwargs):
        """Get the current price of any tokens on this coin (ETH only at this stage as per api docs) in any other supported currencies that you need"""

        contract_addresses = contract_addresses.replace(' ', '')
        kwargs['contract_addresses'] = contract_addresses
        vs_currencies = vs_currencies.replace(' ', '')
        kwargs['vs_currencies'] = vs_currencies

        api_url = '{0}simple/token_price/{1}'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)
        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_supported_vs_currencies(self, **kwargs):
        """Get list of supported_vs_currencies"""

        api_url = '{0}simple/supported_vs_currencies'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- COINS ----------#
    @func_args_preprocessing
    def get_coins(self, **kwargs):
        """List all coins with data (name, price, market, developer, community, etc)"""

        api_url = '{0}coins'.format(self.api_base_url)
        # ['order', 'per_page', 'page', 'localization']
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_top_gainers_losers(self, vs_currency, **kwargs):
        """Get top gainers and losers"""

        kwargs['vs_currency'] = vs_currency

        api_url = '{0}coins/top_gainers_losers'.format(self.api_base_url)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coins_list_new(self, **kwargs):
        """This endpoint allows you to query the latest 200 coins that recently listed on CoinGecko"""

        api_url = '{0}coins/list/new'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coins_list(self, **kwargs):
        """List all supported coins id, name and symbol (no pagination required)"""

        api_url = '{0}coins/list'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coins_markets(self, vs_currency, **kwargs):
        """List all supported coins price, market cap, volume, and market related data"""

        kwargs['vs_currency'] = vs_currency

        api_url = '{0}coins/markets'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_by_id(self, id, **kwargs):
        """Get current data (name, price, market, ... including exchange tickers) for a coin"""

        api_url = '{0}coins/{1}/'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_ticker_by_id(self, id, **kwargs):
        """Get coin tickers (paginated to 100 items)"""

        api_url = '{0}coins/{1}/tickers'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_history_by_id(self, id, date, **kwargs):
        """Get historical data (name, price, market, stats) at a given date for a coin"""

        kwargs['date'] = date

        api_url = '{0}coins/{1}/history'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_market_chart_by_id(self, id, vs_currency, days, **kwargs):
        """Get historical market data include price, market cap, and 24h volume (granularity auto)"""

        # api_url = '{0}coins/{1}/market_chart?vs_currency={2}&days={3}'.format(self.api_base_url, id, vs_currency, days)
        # api_url = self.__api_url_params(api_url, kwargs, api_url_has_params=True)
        api_url = '{0}coins/{1}/market_chart'.format(self.api_base_url, id, vs_currency, days)
        kwargs['vs_currency'] = vs_currency
        kwargs['days'] = days

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_market_chart_range_by_id(self, id, vs_currency, from_timestamp, to_timestamp, **kwargs):
        """Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto)"""

        # api_url = '{0}coins/{1}/market_chart/range?vs_currency={2}&from={3}&to={4}'.format(self.api_base_url, id,
        #                                                                                    vs_currency, from_timestamp,
        #                                                                                    to_timestamp)
        # api_url = self.__api_url_params(api_url, kwargs, api_url_has_params=True)
        api_url = '{0}coins/{1}/market_chart/range'.format(self.api_base_url, id)
        kwargs['vs_currency'] = vs_currency
        kwargs['from'] = from_timestamp
        kwargs['to'] = to_timestamp

        return self.__request(api_url, kwargs)

    # @func_args_preprocessing
    # def get_coin_status_updates_by_id(self, id, **kwargs):
    #     """Get status updates for a given coin"""
    #
    #     api_url = '{0}coins/{1}/status_updates'.format(self.api_base_url, id)
    #     api_url = self.__api_url_params(api_url, kwargs)
    #
    #     return self.__request(api_url)

    @func_args_preprocessing
    def get_coin_ohlc_by_id(self, id, vs_currency, days, **kwargs):
        """Get coin's OHLC"""

        # api_url = '{0}coins/{1}/ohlc?vs_currency={2}&days={3}'.format(self.api_base_url, id, vs_currency, days)
        # api_url = self.__api_url_params(api_url, kwargs, api_url_has_params=True)
        api_url = '{0}coins/{1}/ohlc'.format(self.api_base_url, id)
        kwargs['vs_currency'] = vs_currency
        kwargs['days'] = days

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_ohlc_by_id_range(self, id, vs_currency, from_timestamp, to_timestamp, interval, **kwargs):
        """Get coin's OHLC within a range of timestamp"""

        kwargs['vs_currency'] = vs_currency
        kwargs['from'] = from_timestamp
        kwargs['to'] = to_timestamp
        kwargs['interval'] = interval

        api_url = '{0}coins/{1}/ohlc/range'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_circulating_supply_chart(self, id, days, **kwargs):
        """Get coin's circulating supply chart"""

        kwargs['days'] = days

        api_url = '{0}coins/{1}/circulating_supply_chart'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_circulating_supply_chart_range(self, id, from_timestamp, to_timestamp, **kwargs):
        """Get coin's circulating supply chart within a range of timestamp"""

        kwargs['from'] = from_timestamp
        kwargs['to'] = to_timestamp

        api_url = '{0}coins/{1}/circulating_supply_chart/range'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_total_supply_chart(self, id, days, **kwargs):
        """Get coin's total supply chart"""

        kwargs['days'] = days

        api_url = '{0}coins/{1}/total_supply_chart'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_total_supply_chart_range(self, id, from_timestamp, to_timestamp, **kwargs):
        """Get coin's total supply chart within a range of timestamp"""

        kwargs['from'] = from_timestamp
        kwargs['to'] = to_timestamp

        api_url = '{0}coins/{1}/total_supply_chart/range'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- Contract ----------#
    @func_args_preprocessing
    def get_coin_info_from_contract_address_by_id(self, id, contract_address, **kwargs):
        """Get coin info from contract address"""

        api_url = '{0}coins/{1}/contract/{2}'.format(self.api_base_url, id, contract_address)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_market_chart_from_contract_address_by_id(self, id, contract_address, vs_currency, days, **kwargs):
        """Get historical market data include price, market cap, and 24h volume (granularity auto) from a contract address"""

        # api_url = '{0}coins/{1}/contract/{2}/market_chart/?vs_currency={3}&days={4}'.format(self.api_base_url, id,
        #                                                                                     contract_address,
        #                                                                                     vs_currency, days)
        # api_url = self.__api_url_params(api_url, kwargs, api_url_has_params=True)
        api_url = '{0}coins/{1}/contract/{2}/market_chart'.format(self.api_base_url, id, contract_address)
        kwargs['vs_currency'] = vs_currency
        kwargs['days'] = days

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coin_market_chart_range_from_contract_address_by_id(self, id, contract_address, vs_currency, from_timestamp,
                                                                to_timestamp, **kwargs):
        """Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto) from a contract address"""

        # api_url = '{0}coins/{1}/contract/{2}/market_chart/range?vs_currency={3}&from={4}&to={5}'.format(
        #     self.api_base_url, id, contract_address, vs_currency, from_timestamp, to_timestamp)
        # api_url = self.__api_url_params(api_url, kwargs, api_url_has_params=True)
        api_url = '{0}coins/{1}/contract/{2}/market_chart/range'.format(self.api_base_url, id, contract_address)
        kwargs['vs_currency'] = vs_currency
        kwargs['from'] = from_timestamp
        kwargs['to'] = to_timestamp

        return self.__request(api_url, kwargs)

    # ---------- ASSET PLATFORMS ----------#
    @func_args_preprocessing
    def get_asset_platforms(self, **kwargs):
        """List all asset platforms (Blockchain networks)"""

        api_url = '{0}asset_platforms'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_asset_platform_by_id(self, asset_platform_id, **kwargs):
        """ List all asset platforms (Blockchain networks) by platform id """

        api_url = '{0}token_lists/{1}/all.json'.format(self.api_base_url, asset_platform_id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- CATEGORIES ----------#
    @func_args_preprocessing
    def get_coins_categories_list(self, **kwargs):
        """List all categories"""

        api_url = '{0}coins/categories/list'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_coins_categories(self, **kwargs):
        """List all categories with market data"""

        api_url = '{0}coins/categories'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- EXCHANGES ----------#
    @func_args_preprocessing
    def get_exchanges_list(self, **kwargs):
        """List all exchanges"""

        api_url = '{0}exchanges'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_exchanges_id_name_list(self, **kwargs):
        """List all supported markets id and name (no pagination required)"""

        api_url = '{0}exchanges/list'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_exchanges_by_id(self, id, **kwargs):
        """Get exchange volume in BTC and tickers"""

        api_url = '{0}exchanges/{1}'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_exchanges_tickers_by_id(self, id, **kwargs):
        """Get exchange tickers (paginated, 100 tickers per page)"""

        api_url = '{0}exchanges/{1}/tickers'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # @func_args_preprocessing
    # def get_exchanges_status_updates_by_id(self, id, **kwargs):
    #     """Get status updates for a given exchange"""
    #
    #     api_url = '{0}exchanges/{1}/status_updates'.format(self.api_base_url, id)
    #     api_url = self.__api_url_params(api_url, kwargs)
    #
    #     return self.__request(api_url)

    @func_args_preprocessing
    def get_exchanges_volume_chart_by_id(self, id, days, **kwargs):
        """Get volume chart data for a given exchange"""

        kwargs['days'] = days

        api_url = '{0}exchanges/{1}/volume_chart'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_exchanges_volume_chart_by_id_within_time_range(self, id, from_timestamp, to_timestamp, **kwargs):
        """Get volume chart data for a given exchange within a time range"""

        kwargs['from'] = from_timestamp
        kwargs['to'] = to_timestamp

        api_url = '{0}exchanges/{1}/volume_chart/range'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # # ---------- FINANCE ----------#
    # @func_args_preprocessing
    # def get_finance_platforms(self, **kwargs):
    #     """Get cryptocurrency finance platforms data"""
    #
    #     api_url = '{0}finance_platforms'.format(self.api_base_url)
    #     api_url = self.__api_url_params(api_url, kwargs)
    #
    #     return self.__request(api_url)
    #
    # @func_args_preprocessing
    # def get_finance_products(self, **kwargs):
    #     """Get cryptocurrency finance products data"""
    #
    #     api_url = '{0}finance_products'.format(self.api_base_url)
    #     api_url = self.__api_url_params(api_url, kwargs)
    #
    #     return self.__request(api_url)

    # ---------- INDEXES ----------#
    @func_args_preprocessing
    def get_indexes(self, **kwargs):
        """List all market indexes"""

        api_url = '{0}indexes'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # @func_args_preprocessing
    # def get_indexes_by_id(self, id, **kwargs):
    #    """Get market index by id"""
    #
    #    api_url = '{0}indexes/{1}'.format(self.api_base_url, id)
    #    api_url = self.__api_url_params(api_url, kwargs)
    #
    #    return self.__request(api_url)

    @func_args_preprocessing
    def get_indexes_by_market_id_and_index_id(self, market_id, id, **kwargs):
        """Get market index by market id and index id"""

        api_url = '{0}indexes/{1}/{2}'.format(self.api_base_url, market_id, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_indexes_list(self, **kwargs):
        """List market indexes id and name"""

        api_url = '{0}indexes/list'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- DERIVATIVES ----------#
    @func_args_preprocessing
    def get_derivatives(self, **kwargs):
        """List all derivative tickers"""

        api_url = '{0}derivatives'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_derivatives_exchanges(self, **kwargs):
        """List all derivative tickers"""

        api_url = '{0}derivatives/exchanges'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_derivatives_exchanges_by_id(self, id, **kwargs):
        """List all derivative tickers"""

        api_url = '{0}derivatives/exchanges/{1}'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_derivatives_exchanges_list(self, **kwargs):
        """List all derivative tickers"""

        api_url = '{0}derivatives/exchanges/list'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- NFTS (BETA) ----------#
    @func_args_preprocessing
    def get_nfts_list(self, **kwargs):
        """List all supported NFT ids, paginated by 100 items per page, paginated to 100 items"""

        api_url = '{0}nfts/list'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_nfts_by_id(self, id, **kwargs):
        """Get current data (name, price_floor, volume_24h ...) for an NFT collection. native_currency (string) is only a representative of the currency"""

        api_url = '{0}nfts/{1}'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_nfts_by_asset_platform_id_and_contract_address(self, asset_platform_id, contract_address, **kwargs):
        """Get current data (name, price_floor, volume_24h ...) for an NFT collection. native_currency (string) is only a representative of the currency"""

        api_url = '{0}nfts/{1}/contract/{2}'.format(self.api_base_url, asset_platform_id, contract_address)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_nfts_markets(self, **kwargs):
        """This endpoint allows you to query all the supported NFT collections with floor price, market cap, volume and market related data on CoinGecko"""

        api_url = '{0}nfts/markets'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_nfts_market_chart_by_id(self, id, days, **kwargs):
        """This endpoint allows you query historical market data of a NFT collection, including floor price, market cap, and 24h volume, by number of days away from now"""

        kwargs['days'] = days

        api_url = '{0}nfts/{1}/market_chart'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_ntfs_market_chart_by_asset_platform_id_and_contract_address(self, asset_platform_id, contract_address, days, **kwargs):
        """This endpoint allows you query historical market data of a NFT collection, including floor price, market cap, and 24h volume, by number of days away from now based on the provided contract address"""

        kwargs['days'] = days

        api_url = '{0}nfts/{1}/contract/{2}/market_chart'.format(self.api_base_url, asset_platform_id, contract_address)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    @func_args_preprocessing
    def get_nfts_tickers_by_id(self, id, **kwargs):
        """This endpoint allows you to query the latest floor price and 24h volume of a NFT collection, on each NFT marketplace, e.g. OpenSea and LooksRare"""

        api_url = '{0}nfts/{1}/tickers'.format(self.api_base_url, id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # # ---------- STATUS UPDATES ----------#
    # @func_args_preprocessing
    # def get_status_updates(self, **kwargs):
    #     """List all status_updates with data (description, category, created_at, user, user_title and pin)"""
    #
    #     api_url = '{0}status_updates'.format(self.api_base_url)
    #     api_url = self.__api_url_params(api_url, kwargs)
    #
    #     return self.__request(api_url)

    # # ---------- EVENTS ----------#
    # @func_args_preprocessing
    # def get_events(self, **kwargs):
    #     """Get events, paginated by 100"""
    #
    #     api_url = '{0}events'.format(self.api_base_url)
    #     api_url = self.__api_url_params(api_url, kwargs)
    #
    #     return self.__request(api_url)
    #
    # @func_args_preprocessing
    # def get_events_countries(self, **kwargs):
    #     """Get list of event countries"""
    #
    #     api_url = '{0}events/countries'.format(self.api_base_url)
    #     api_url = self.__api_url_params(api_url, kwargs)
    #
    #     return self.__request(api_url)
    #
    # @func_args_preprocessing
    # def get_events_types(self, **kwargs):
    #     """Get list of event types"""
    #
    #     api_url = '{0}events/types'.format(self.api_base_url)
    #     api_url = self.__api_url_params(api_url, kwargs)
    #
    #     return self.__request(api_url)

    # ---------- EXCHANGE-RATES ----------#
    @func_args_preprocessing
    def get_exchange_rates(self, **kwargs):
        """Get BTC-to-Currency exchange rates"""

        api_url = '{0}exchange_rates'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- SEARCH ----------#
    @func_args_preprocessing
    def search(self, query, **kwargs):
        """Search for coins, categories and markets on CoinGecko"""

        # api_url = '{0}search?query={1}'.format(self.api_base_url, query)
        # api_url = self.__api_url_params(api_url, kwargs, api_url_has_params=True)
        api_url = '{0}search'.format(self.api_base_url)
        kwargs['query'] = query

        return self.__request(api_url, kwargs)

    # ---------- TRENDING ----------#
    @func_args_preprocessing
    def get_search_trending(self, **kwargs):
        """Get top 7 trending coin searches"""

        api_url = '{0}search/trending'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- GLOBAL ----------#
    @func_args_preprocessing
    def get_global(self, **kwargs):
        """Get cryptocurrency global data"""

        api_url = '{0}global'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)['data']

    @func_args_preprocessing
    def get_global_decentralized_finance_defi(self, **kwargs):
        """Get cryptocurrency global decentralized finance(defi) data"""

        api_url = '{0}global/decentralized_finance_defi'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)['data']

    @func_args_preprocessing
    def get_global_market_cap_chart(self, days, **kwargs):
        """Get cryptocurrency global market cap chart data"""

        kwargs['days'] = days

        api_url = '{0}global/market_cap_chart'.format(self.api_base_url)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)

    # ---------- COMPANIES ----------#
    @func_args_preprocessing
    def get_companies_public_treasury_by_coin_id(self, coin_id, **kwargs):
        """Get public companies data"""

        api_url = '{0}companies/public_treasury/{1}'.format(self.api_base_url, coin_id)
        # api_url = self.__api_url_params(api_url, kwargs)

        return self.__request(api_url, kwargs)
