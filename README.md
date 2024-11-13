# CoinGecko API wrapper
[![PyPi Version](https://img.shields.io/pypi/v/pycoingecko.svg)](https://pypi.python.org/pypi/pycoingecko/)
![GitHub](https://img.shields.io/github/license/man-c/pycoingecko)

Python3 wrapper around the [CoinGecko](https://www.coingecko.com/) API (V3) 🦎<br> Supports both Public and Pro API:
 * [Public API v3.0.1](https://docs.coingecko.com/v3.0.1/reference/introduction)
 * [Pro API v3.1.1](https://docs.coingecko.com/v3.1.1/reference/introduction)

### Installation
PyPI
```bash
pip install -U pycoingecko
```
or from source
```bash
git clone https://github.com/man-c/pycoingecko.git
cd pycoingecko
python3 setup.py install
```

### Usage

For free **Public API**:

 * without any demo api key (x-cg-demo-api-key):
    ```python
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI()
    ```
 * 🔑 with a <ins>demo api key</ins>:
    ```python
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI(demo_api_key='YOUR_DEMO_API_KEY')
    ```

For **Pro API**:
 * 🔑 with a <ins>pro api key</ins>:
    ```python
    from pycoingecko import CoinGeckoAPI
    cg = CoinGeckoAPI(api_key='YOUR_PRO_API_KEY')
    ```

### Examples
The required parameters for each endpoint are defined as required (mandatory) parameters for the corresponding functions.\
**Any optional parameters** can be passed using same names, as defined in CoinGecko API doc (https://www.coingecko.com/en/api/documentation).

For any parameter:
- ***Lists** are supported as input for multiple-valued comma-separated parameters\
  (e.g. see /simple/price usage examples).*
- ***Booleans** are supported as input for boolean type parameters; they can be `str` ('true', 'false'') or `bool` (`True`, `False`)\
  (e.g. see /simple/price usage examples).*

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
# OR (also booleans can be used for boolean type arguments)
>>> cg.get_price(ids='bitcoin', vs_currencies='usd', include_market_cap=True, include_24hr_vol=True, include_24hr_change=True, include_last_updated_at=True)
{'bitcoin': {'usd': 3458.74, 'usd_market_cap': 60574330199.29028, 'usd_24h_vol': 4182664683.6247883, 'usd_24h_change': 1.2295378479069035, 'last_updated_at': 1549071865}}
```

### API documentation
https://www.coingecko.com/en/api/documentation

### 📡 Endpoints included
> :warning: **Endpoints documentation**: To make sure that you are using properly each endpoint you should check the [API documentation](https://www.coingecko.com/en/api/documentation). Return behaviour and parameters of the endpoints, such as *pagination*, might have changed. <br> Any **optional parameters** defined in CoinGecko API doc can be passed as function parameters using same parameters names with the API *(see Examples above)*.
<details><summary>ping</summary>
<p>

* **/ping** 
  
   _Check API server status_
  ```python
  cg.ping()
  ```
</details>

<details><summary>key</summary>
<p>

* [Pro API] 💼 **/key**  
  
   _Monitor your account's API usage, including rate limits, monthly total credits, remaining credits, and more_
  ```python
  cg.key()
  ```
</details>

<details><summary>simple</summary>
<p>

* **/simple/price** 
  
   _Get the current price of any cryptocurrencies in any other supported currencies that you need_
  ```python
  cg.get_price()
  ```
* **/simple/token_price/{id}** 
  
   _Get current price of tokens (using contract addresses) for a given platform in any other currency that you need_
  ```python
  cg.get_token_price()
  ```
* **/simple/supported_vs_currencies** 
  
   _Get list of supported_vs_currencies_
  ```python
  cg.get_supported_vs_currencies()
  ```
</details>

<details><summary>coins</summary>
<p>

* **/coins/list** 
  
   _List all supported coins id, name and symbol (no pagination required)_
  ```python
  cg.get_coins_list()
  ```

* [Pro API] 💼 **/coins/top_gainers_losers**  
  
   _Query the top 30 coins with largest price gain and loss by a specific time duration_
  ```python
  cg.get_coin_top_gainers_losers()
  ```

* [Pro API] 💼 **/coins/list/new**  
  
   _Query the latest 200 coins that recently listed on CoinGecko_
  ```python
  cg.get_coins_list_new()
  ```

* **/coins/markets**  
  
   _List all supported coins price, market cap, volume, and market related data_
  ```python 
  cg.get_coins_markets()
  ```
* **/coins/{id}**  
  
   _Get current data (name, price, market, ... including exchange tickers) for a coin_
  ```python 
  cg.get_coin_by_id()
  ```
* **/coins/{id}/tickers**  
  
   _Get coin tickers (paginated to 100 items)_
  ```python 
  cg.get_coin_ticker_by_id()
  ```
* **/coins/{id}/history**  
  
   _Get historical data (name, price, market, stats) at a given date for a coin_
  ```python 
  cg.get_coin_history_by_id()
  ```
* **/coins/{id}/market_chart**  
  
   _Get historical market data include price, market cap, and 24h volume (granularity auto)_
  ```python 
  cg.get_coin_market_chart_by_id()
  ```
* **/coins/{id}/market_chart/range**  
  
   _Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto)_
  ```python 
  cg.get_coin_market_chart_range_by_id()
  ```

[//]: # (* **/coins/{id}/status_updates** &#40;Get status updates for a given coin &#40;beta&#41;&#41;)

[//]: # (  ```python)

[//]: # (  cg.get_coin_status_updates_by_id&#40;&#41;)

[//]: # (  ```)
* **/coins/{id}/ohlc**  
  
   _Get the OHLC chart (Open, High, Low, Close) of a coin based on particular coin id_
  ```python
  cg.get_coin_ohlc_by_id()
  ```

* [Pro API] 💼 **/coins/{id}/ohlc/range**  
  
   _Get the OHLC chart (Open, High, Low, Close) of a coin within a range of timestamp based on particular coin id_
  ```python
  cg.get_coin_ohlc_by_id_range()
  ```

* [Pro API] 👑 **/coins/{id}/circulating_supply_chart**  
  
   _Query historical circulating supply of a coin by number of days away from now based on provided coin id_
  ```python
  cg.get_coin_circulating_supply_chart()
  ```

* [Pro API] 👑 **/coins/{id}/circulating_supply_chart/range**  
  
   _Query historical circulating supply of a coin, within a range of timestamp based on the provided coin id_
  ```python
  cg.get_coin_circulating_supply_chart_range()
  ```

* [Pro API] 👑 **/coins/{id}/total_supply_chart**  
  
   _Query historical total supply of a coin by number of days away from now based on provided coin id_
  ```python
  cg.get_coin_total_supply_chart()
  ```

* [Pro API] 👑 **/coins/{id}/total_supply_chart/range**  
  
   _Query historical total supply of a coin, within a range of timestamp based on the provided coin id_
  ```python
  cg.get_coin_total_supply_chart_range()
  ```

</details>


<details><summary>contract</summary>
<p>

* **/coins/{id}/contract/{contract_address}**  
  
   _Get coin info from contract address_
  ```python
  cg.get_coin_info_from_contract_address_by_id()
  ```
* **/coins/{id}/contract/{contract_address}/market_chart/**  
  
   _Get historical market data include price, market cap, and 24h volume (granularity auto) from a contract address_
  ```python
  cg.get_coin_market_chart_from_contract_address_by_id()
  ```
* **/coins/{id}/contract/{contract_address}/market_chart/range**  
  
   _Get historical market data include price, market cap, and 24h volume within a range of timestamp (granularity auto) from a contract address_
  ```python
  cg.get_coin_market_chart_range_from_contract_address_by_id()
  ```
</details>

<details><summary>asset_platforms</summary>
<p>

* **/asset_platforms**  
  
   _List all asset platforms (Blockchain networks)_
  ```python
  cg.get_asset_platforms()
  ```

* [Pro API] 👑 **/token_lists/{asset_platform_id}/all.json**  
  
   _Get full list of tokens of a blockchain network (asset platform) that is supported by Ethereum token list standard_
  ```python
  cg.get_asset_platform_by_id()
  ```

</details>

<details><summary>categories</summary>
<p>

* **/coins/categories/list**  
  
   _List all categories_
  ```python
  cg.get_coins_categories_list()
  ```
* **coins/categories**  
  
   _List all categories with market data_
  ```python
  cg.get_coins_categories()
  ```
</details>

<details><summary>exchanges</summary>
<p>

* **/exchanges**  
  
   _List all exchanges_
  ```python
  cg.get_exchanges_list()
  ```
* **/exchanges/list**  
  
   _List all supported markets id and name (no pagination required)_
  ```python
  cg.get_exchanges_id_name_list()
  ```
* **/exchanges/{id}**  
  
   _Get exchange volume in BTC and top 100 tickers only_
  ```python
  cg.get_exchanges_by_id()
  ```
* **/exchanges/{id}/tickers**  
  
   _Get exchange tickers (paginated, 100 tickers per page)_
  ```python
  cg.get_exchanges_tickers_by_id()
  ```

[//]: # (* **/exchanges/{id}/status_updates** &#40;Get status updates for a given exchange &#40;beta&#41;&#41;)

[//]: # (  ```python)

[//]: # (  cg.get_exchanges_status_updates_by_id&#40;&#41;)

[//]: # (  ```)
* **/exchanges/{id}/volume_chart**  
  
   _Get volume_chart data for a given exchange_
  ```python
  cg.get_exchanges_volume_chart_by_id()
  ```

* [Pro API] 💼 **/exchanges/{id}/volume_chart/range**  
  
   _Query the historical volume chart data in BTC by specifying date range in UNIX based on exchange’s id_
  ```python
  cg.get_exchanges_volume_chart_by_id_within_time_range()
  ```  

</details>

[//]: # (<details><summary>finance</summary>)

[//]: # (<p>)

[//]: # ()
[//]: # (* **/finance_platforms** &#40;List all finance platforms&#41;)

[//]: # (  ```python)

[//]: # (  cg.get_finance_platforms&#40;&#41;)

[//]: # (  ```)

[//]: # (* **/finance_products** &#40;List all finance products&#41;)

[//]: # (  ```python)

[//]: # (  cg.get_finance_products&#40;&#41;)

[//]: # (  ```)

[//]: # (</details>)

<details><summary>indexes</summary>
<p>

* **/indexes**  
  
   _List all market indexes_
```python
cg.get_indexes()
```
* **/indexes/{market_id}/{id}**  
  
   _Get market index by market id and index id_
```python
cg.get_indexes_by_market_id_and_index_id()
```
* **/indexes/list**  
  
   _List market indexes id and name_
```python
cg.get_indexes_list()
```
</details>

<details><summary>derivatives</summary>
<p>

* **/derivatives**  
  
   _List all derivative tickers_
  ```python
  cg.get_derivatives()
  ```
* **/derivatives/exchanges**  
  
   _List all derivative exchanges_
  ```python
  cg.get_derivatives_exchanges()
  ```
* **/derivatives/exchanges/{id}** 
  
   _Show derivative exchange data_
  ```python
  cg.get_derivatives_exchanges_by_id()
  ```
* **/derivatives/exchanges/list** 
  
   _List all derivative exchanges name and identifier_
  ```python
  cg.get_derivatives_exchanges_list()
  ```
</details>

<details><summary>nfts (beta)</summary>
<p>

* **/nfts/list** 
  
   _List all supported NFT ids, paginated by 100 items per page, paginated to 100 items_
  ```python
  cg.get_nfts_list()
  ```
* **/nfts/{id}** 
  
   _Get current data (name, price_floor, volume_24h ...) for an NFT collection. native_currency (string) is only a representative of the currency_
  ```python
  cg.get_nfts_by_id()
  ```
* **/nfts/{asset_platform_id}/contract/{contract_address}** 
  
   _Get current data (name, price_floor, volume_24h ...) for an NFT collection. native_currency (string) is only a representative of the currency_
  ```python
  cg.get_nfts_collection_by_asset_platform_id_and_contract_address()
  ```

* [Pro API] 💼 **/nfts/markets** 
  
   _Query all the supported NFT collections with floor price, market cap, volume and market related data on CoinGecko_
  ```python
  cg.get_nfts_markets()
  ```

* [Pro API] 💼 **/nfts/{id}/market_chart** 
  
   _Query historical market data of a NFT collection, including floor price, market cap, and 24h volume, by number of days away from now_
  ```python
  cg.get_nfts_market_chart_by_id()
  ```

* [Pro API] 💼 **/nfts/{asset_platform_id}/contract/{contract_address}/market_chart** 
  
   _Query historical market data of a NFT collection, including floor price, market cap, and 24h volume, by number of days away from now based on the provided contract address_
  ```python
  cg.get_ntfs_market_chart_by_asset_platform_id_and_contract_address()
  ```

* [Pro API] 💼 **/nfts/{id}/tickers** 
  
   _Query the latest floor price and 24h volume of a NFT collection, on each NFT marketplace, e.g. OpenSea and LooksRare_
  ```python
  cg.get_nfts_tickers_by_id()
  ```

</details>

[//]: # (<details><summary>status_updates</summary>)

[//]: # (<p>)

[//]: # ()
[//]: # (* **/status_updates** &#40;List all status_updates with data &#40;description, category, created_at, user, user_title and pin&#41;&#41;)

[//]: # (  ```python)

[//]: # (  cg.get_status_updates&#40;&#41;)

[//]: # (  ```)

[//]: # (</details>)

[//]: # (<details><summary>events</summary>)

[//]: # (<p>)

[//]: # ()
[//]: # (* **/events** &#40;Get events, paginated by 100&#41;)

[//]: # (  ```python)

[//]: # (  cg.get_events&#40;&#41;)

[//]: # (  ```)

[//]: # (* **/events/countries** &#40;Get list of event countries&#41;)

[//]: # (  ```python)

[//]: # (  cg.get_events_countries&#40;&#41;)

[//]: # (  ```)

[//]: # (* **/events/types** &#40;Get list of events types&#41;)

[//]: # (  ```python)

[//]: # (  cg.get_events_types&#40;&#41;)

[//]: # (  ```)

[//]: # (</details>)

<details><summary>exchange_rates</summary>
<p>

* **/exchange_rates** 
  
   _Get BTC-to-Currency exchange rates_
  ```python
  cg.get_exchange_rates()
  ```
</details>

<details><summary>search</summary>
<p>

* **/search** 
  
   _Search for coins, categories and markets on CoinGecko_
  ```python
  cg.search()
  ```
</details>

<details><summary>trending</summary>
<p>

* **/search/trending** 
  
   _Get trending search coins (Top-7) on CoinGecko in the last 24 hours_
  ```python
  cg.get_search_trending()
  ```
</details>

<details><summary>global</summary>
<p>

* **/global** 
  
   _Get cryptocurrency global data_
    ```python
    cg.get_global()
    ```
* **/global/decentralized_finance_defi** 
  
   _Get cryptocurrency global decentralized finance(defi) data_
    ```python
    cg.get_global_decentralized_finance_defi()
    ```

* [Pro API] 💼 **/global/market_cap_chart**

  _Query historical global market cap and volume data by number of days away from now)_
  ```python
  cg.get_global_market_cap_chart()
  ```

</details>

<details><summary>companies (beta)</summary>
<p>

* **/companies/public_treasury/{coin_id}** 
  
   _Query public companies’ bitcoin or ethereum holdings_
    ```python
    cg.get_companies_public_treasury_by_coin_id()
    ```
</details>

### Test

#### Installation
Install required packages for testing using:
```bash
pip install pytest responses
```

#### Usage

Run unit tests with:

```
# after installing pytest and responses using pip3
pytest tests
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
