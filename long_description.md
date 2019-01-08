# CoinGecko API wrapper

Python3 wrapper around the [CoinGecko](https://www.coingecko.com/) API (V3)

### Installation
```
pip install pycoingecko
```

### Usage

```
from pycoingecko import CoinGeckoAPI
cg = CoinGeckoAPI()
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
