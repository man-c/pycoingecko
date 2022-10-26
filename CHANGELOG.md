
3.1.0 / 2022-10-26
==================

  * added nfts (beta) endpoints (/nfts/list, /nfts/{id}, /nfts/{asset_platform_id}/contract/{contract_address})
  * updated tests

3.0.0 / 2022-09-01
==================

  * removed deprecated endpoints (status_updates, finance and events):
    * /coins/{id}/status_updates -> cg.get_coin_status_updates_by_id()
    * /exchanges/{id}/status_updates -> cg.get_exchanges_status_updates_by_id()
    * /finance_platforms -> cg.get_finance_platforms()
    * /finance_products -> cg.get_finance_products()
    * /status_updates -> cg.get_status_updates()
    * /events -> cg.get_events()
    * /events/countries -> cg.get_events_countries()
    * /events/types -> cg.get_events_types()
  * removed deprecated api_base_url param from CoinGeckoAPI init

2.3.0 / 2022-08-30
==================

  * added /search endpoint
  * added CoinGecko Pro API support using api_key param in CoinGeckoAPI init (required in PRO version API calls)
  * added ability to modify how many retries to do in requests session using param retries in CoinGeckoAPI init (default: retries=5)
  * fixed session to mount retry adapter on https instead of http
  * fixed params passed in get_coin_market_chart_range_from_contract_address_by_id for /coins/{id}/contract/{contract_address}/market_chart/range endpoint

2.2.0 / 2021-06-17
==================

  * added /indexes/{market_id}/{id} and /companies/public_treasury/{coin_id} endpoints

2.1.0 / 2021-06-03
==================

  * added asset_platforms (/asset_platforms) and categories (/coins/categories/list, coins/categories) endpoints

2.0.0 / 2021-04-23
==================

  * allow Python Lists and Booleans for any endpoint parameter (list converted to comma-separated string & bool converted to lower case string)
  * removed /indexes/{id} endpoint (Get market index by id) -> cg.get_indexes_by_id()
  * improved request exceptions handling (Fixed unbound local exception on GET request failure)

1.4.1 / 2021-03-30
==================

  * fixed __api_url_params issue for optional parametes of few endpoints (such as /coins/{id}/market_chart)

1.4.0 / 2020-10-03
==================

  * added new endpoints (/coins/{id}/ohlc, /search/trending, /global/decentralized_finance_defi)
  * updated tests

1.3.0 / 2020-07-12
==================

  * allow optional arguments for **ALL** endopoints

1.2.0 / 2019-12-13
==================

  * added indexes endpoints (/indexes, /indexes/{id}, /indexes/list)

1.1.0 / 2019-12-06
==================

  * added derivatives endpoints (/derivatives, /derivatives/exchanges, /derivatives/exchanges/{id}, /derivatives/exchanges/list)

1.0.0 / 2019-11-17
==================

  * updated tests
  * included more contract endpoints
  * included /coins/{id}/market_chart/range endpoint
  * basic methods for finance endpoints with tests
  * updated error handling
  * added check for json format in __request; coingecko returns a html string when something goes wrong in the request, which results in an error when json.loads is called on the html string.

0.4.0 / 2019-08-20
==================

  * included /exchanges/{id}/volume_chart endpoint

0.3.0 / 2019-05-31
==================

  * exceptions include API error message
  * fix get_coin_market_chart_by_id test
  * Use a list or tuple for multiple-valued arguments
  * convert every list arg to comma-separated string

0.2.0 / 2019-05-17
==================

  * Fixed arguments for get_token_price
  * Added get_token_price function

0.1.6 / 2019-02-02
==================

  * README incude examples
  * included /exchanges/list endpoint

0.1.0 / 2019-01-02
==================

  * added /coins/{id}/tickers endpoint
  * included events endpoints
  * included status_updates endpoints
  * updated exchanges endpoints
  * updated coins endpoints
  * included simple endpoints

0.0.2 / 2018-11-20
==================

  * use requests session to include retries
  * fixed bug when querying exchanges and added more unit tests
  * first unit tests for coingecko wrappers
  * initial commit
