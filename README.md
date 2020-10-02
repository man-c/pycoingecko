# CoinGecko API wrapper
[![PyPi Version](https://img.shields.io/pypi/v/pycoingecko.svg)](https://pypi.python.org/pypi/pycoingecko/)

Python3 wrapper around the [CoinGecko](https://www.coingecko.com/) API (V3)

### Installation
PyPI
```bash
pip install pycoingecko
```
or from source
```bash
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
```

### Usage

```python
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
```

### Examples
The required parameters for each endpoint are defined as required (mandatory) parameters for the corresponding functions.
**Any optional parameters** can be also passed using same names, as defined in CoinGecko API doc (https://www.coingecko.com/api/docs/v3)

*Lists are also supported as input for multiple-valued comma-separated parameters (e.g. see /simple/price usage examples).*

Usage examples:
```python
# /simple/price endpoint with the required parameters
>>> cg.get_price(ids='bitcoin', vs_currencies='usd')
{'bitcoin': {'usd': 3462.04}}

>>> cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd')
# OR (lists can be used for multiple-valued arguments)
>>> cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum'], vs_currencies='usd')
{'bitcoin': {'usd': 3461.27}, 'ethereum': {'usd': 106.92}, 'litecoin': {'usd': 32.72}}

>>> cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd,eur')
# OR (lists can be used for multiple-valued arguments)
>>> cg.get_price(ids=['bitcoin', 'litecoin', 'ethereum'], vs_currencies=['usd', 'eur'])
{'bitcoin': {'usd': 3459.39, 'eur': 3019.33}, 'ethereum': {'usd': 106.91, 'eur': 93.31}, 'litecoin': {'usd': 32.72, 'eur': 28.56}}

# optional parameters can be passed as defined in the API doc (https://www.coingecko.com/api/docs/v3)
>>> cg.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap='true', include_24hr_vol='true', include_24hr_change='true', include_last_updated_at='true')
{'bitcoin': {'usd': 3458.74, 'usd_market_cap': 60574330199.29028, 'usd_24h_vol': 4182664683.6247883, 'usd_24h_change': 1.2295378479069035, 'last_updated_at': 1549071865}}
```

### API documentation
https://www.coingecko.com/api/docs/v3

### Endpoints included
> :warning: **Endpoints documentation**: To make sure that your are using properly each endpoint you should check the [API documentation](https://www.coingecko.com/api/docs/v3). Return behaviour and parameters of the endpoints, such as *pagination*, might have changed. <br> Any **optional parameters** defined in CoinGecko API doc can be passed as function parameters using same parameters names with the API *(see Examples above)*.
- *ping*
  - **/ping** (Check API server status)
    ```python 
    cg.ping()
    ```
- *simple*
  - **/simple/price** (Get the current price of any cryptocurrencies in any other supported currencies that you need)
    ```python 
    cg.get_price()
    ```
  - **/simple/token_price/{id}** (Get current price of tokens (using contract addresses) for a given platform in any other currency that you need)
    ```python 
    cg.get_token_price()
    ```  
  - **/simple/supported_vs_currencies** (Get list of supported_vs_currencies)
    ```python 
    cg.get_supported_vs_currencies()
    ```
- *coins*
  - **/coins/list** (List all supported coins id, name and symbol (no pagination required))
    ```python 
    cg.get_coins_list()
    ```
  - **/coins/markets** (List all supported coins price, market cap, volume, and market related data)
    ```python 
    cg.get_coins_markets()
    ```
  - **/coins/{id}** (Get current data (name, price, market, ... including exchange tickers) for a coin)
    ```python 
    cg.get_coin_by_id()
    ```
  - **/coins/{id}/tickers** (Get coin tickers (paginated to 100 items))
    ```python 
    cg.get_coin_ticker_by_id()
    ```
  - **/coins/{id}/history** (Get historical data (name, price, market, stats) at a given date for a coin)
    ```python 
    cg.get_coin_history_by_id()
    ```
  - **/coins/{id}/market_chart** (Get historical market data include price, market cap, and 24h volume (granularity auto))
    ```python 
    cg.get_coin_market_chart_by_id()
    ```
  - **/coins/{id}/market_chart/range** (Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto))
    ```python 
    cg.get_coin_market_chart_range_by_id()
    ```
  - **/coins/{id}/status_updates** (Get status updates for a given coin (beta))
    ```python
    cg.get_coin_status_updates_by_id()
    ```
  - **/coins/{id}/ohlc** (Get coin's OHLC (beta))
    ```python
    cg.get_coin_ohlc_by_id()
    ```
- *contract*
  - **/coins/{id}/contract/{contract_address}** (Get coin info from contract address)
    ```python
    cg.get_coin_info_from_contract_address_by_id()
    ```
  - **/coins/{id}/contract/{contract_address}/market_chart/** (Get historical market data include price, market cap, and 24h volume (granularity auto) from a contract address)
    ```python
    cg.get_coin_market_chart_from_contract_address_by_id()
    ```
  - **/coins/{id}/contract/{contract_address}/market_chart/range** (Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto) from a contract address)
    ```python
    cg.get_coin_market_chart_range_from_contract_address_by_id()
    ```
- *exchanges (beta)*
  - **/exchanges** (List all exchanges)
    ```python
    cg.get_exchanges_list()
    ```
  - **/exchanges/list** (List all supported markets id and name (no pagination required))
    ```python
    cg.get_exchanges_id_name_list()
    ```
  - **/exchanges/{id}** (Get exchange volume in BTC and top 100 tickers only)
    ```python
    cg.get_exchanges_by_id()
    ```
  - **/exchanges/{id}/tickers** (Get exchange tickers (paginated, 100 tickers per page))
    ```python
    cg.get_exchanges_tickers_by_id()
    ```
  - **/exchanges/{id}/status_updates** (Get status updates for a given exchange (beta))
    ```python
    cg.get_exchanges_status_updates_by_id()
    ```
  - **/exchanges/{id}/volume_chart** (Get volume_chart data for a given exchange (beta))
    ```python
    cg.get_exchanges_volume_chart_by_id()
    ```
- *finance (beta)*
  - **/finance_platforms** (List all finance platforms)
    ```python
    cg.get_finance_platforms()
    ```
  - **/finance_products** (List all finance products)
    ```python
    cg.get_finance_products()
    ```
- *indexes (beta)*
  - **/indexes** (List all market indexes)
    ```python
    cg.get_indexes()
    ```
  - **/indexes/{id}** (Get market index by id)
    ```python
    cg.get_indexes_by_id()
    ```
  - **/indexes/list** (List market indexes id and name)
    ```python
    cg.get_indexes_list()
    ```
- *derivatives (beta)*
  - **/derivatives** (List all derivative tickers)
    ```python
    cg.get_derivatives()
    ```
  - **/derivatives/exchanges** (List all derivative exchanges)
    ```python
    cg.get_derivatives_exchanges()
    ```
  - **/derivatives/exchanges/{id}** (Show derivative exchange data)
    ```python
    cg.get_derivatives_exchanges_by_id()
    ```
  - **/derivatives/exchanges/list** (List all derivative exchanges name and identifier)
    ```python
    cg.get_derivatives_exchanges_list()
    ```
- status_updates (beta)
  - **/status_updates** (List all status_updates with data (description, category, created_at, user, user_title and pin))
    ```python
    cg.get_status_updates()
    ```
- *events*
  - **/events** (Get events, paginated by 100)
    ```python
    cg.get_events()
    ```
  - **/events/countries** (Get list of event countries)
    ```python
    cg.get_events_countries()
    ```
  - **/events/types** (Get list of events types)
    ```python
    cg.get_events_types()
    ```
- *exchange_rates*
  - **/exchange_rates** (Get BTC-to-Currency exchange rates)
    ```python
    cg.get_exchange_rates()
    ```
- *trending*
  - **/search/trending** (Get trending search coins (Top-7) on CoinGecko in the last 24 hours)
    ```python
    cg.get_search_trending()
    ```
- *global*
  - **/global** (Get cryptocurrency global data)
    ```python
    cg.get_global()
    ```
  - **/global/decentralized_finance_defi** (Get cryptocurrency global decentralized finance(defi) data)
    ```python
    cg.get_global_decentralized_finance_defi()
    ```

### Test

Run unit tests with:

```
# after installing pytest using pip3
pytest tests
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
