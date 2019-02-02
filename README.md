# CoinGecko API wrapper

Python3 wrapper around the [CoinGecko](https://www.coingecko.com/) API (V3)

### Installation
PyPI
```
pip install pycoingecko
```
or from source
```
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
The required parameters for each endpoint are defined as required (mandatory) parameters for the coresponding functions.
Optional parameter can be passed by just using their names, as defined in CoinGecko API doc (https://www.coingecko.com/api/docs/v3)

Usage examples:
```python
# /simple/price endpoint with the required parameters
>>> cg.get_price(ids='bitcoin', vs_currencies='usd')
{'bitcoin': {'usd': 3462.04}}

>>> cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd')
{'bitcoin': {'usd': 3461.27}, 'ethereum': {'usd': 106.92}, 'litecoin': {'usd': 32.72}}

>>> cg.get_price(ids='bitcoin,litecoin,ethereum', vs_currencies='usd,eur')
{'bitcoin': {'usd': 3459.39, 'eur': 3019.33}, 'ethereum': {'usd': 106.91, 'eur': 93.31}, 'litecoin': {'usd': 32.72, 'eur': 28.56}}

# the optional parameteres can be passed as defined in the API doc (https://www.coingecko.com/api/docs/v3)
>>> cg.get_price(ids='bitcoin', vs_currencies='usd',include_market_cap='true',include_24hr_vol='true',include_24hr_change='true',include_last_updated_at='true')
{'bitcoin': {'usd': 3458.74, 'usd_market_cap': 60574330199.29028, 'usd_24h_vol': 4182664683.6247883, 'usd_24h_change': 1.2295378479069035, 'last_updated_at': 1549071865}}
```

### API documentation
https://www.coingecko.com/api/docs/v3

### Endpoints included
- ping
  - /ping (Check API server status)
- simple
  - /simple/price (Get the current price of any cryptocurrencies in any other supported currencies that you need)
  - /simple/supported_vs_currencies (Get list of supported_vs_currencies)
- coins
  - /coins/list (List all supported coins id, name and symbol (no pagination required))
  - /coins/markets (List all supported coins price, market cap, volume, and market related data (no pagination required))
  - /coins/{id} (Get current data (name, price, market, ... including exchange tickers) for a coin)
  - /coins/{id}/tickers (Get coin tickers (paginated to 100 items))
  - /coins/{id}/history (Get historical data (name, price, market, stats) at a given date for a coin)
  - /coins/{id}/market_chart (Get historical market data include price, market cap, and 24h volume (granularity auto))
  - /coins/{id}/status_updates (Get status updates for a given coin (beta))
  - /coins/{id}/contract/{contract_address} (Get coin info from contract address)
- exchanges (beta)
  - /exchanges (List all exchanges)
  - /exchanges/list (List all supported markets id and name (no pagination required))
  - /exchanges/{id} (Get exchange volume in BTC and top 100 tickers only)
  - /exchanges/{id}/tickers (Get exchange tickers (paginated))
  - /exchanges/{id}/status_updates (Get status updates for a given exchange (beta))
- status_updates (beta)
  - /status_updates (List all status_updates with data (description, category, created_at, user, user_title and pin))
- events
  - /events (Get events, paginated by 100)
  - /events/countries (Get list of event countries)
  - /events/types (Get list of events types)
- exchange_rates
  - /exchange_rates (Get BTC-to-Currency exchange rates)
- global
  - /global (Get cryptocurrency global data)

### Test

Run unit tests with:

```
# after installing pytest using pip3
pytest tests
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
