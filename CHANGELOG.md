
2.2.0 / 2021-06-17
==================

  * Added /indexes/{market_id}/{id} and /companies/public_treasury/{coin_id} endpoints

2.1.0 / 2021-06-03
==================

  * Added asset_platforms (/asset_platforms) and categories (/coins/categories/list, coins/categories) endpoints

2.0.0 / 2021-04-23
==================

  * Allow Python Lists and Booleans for any endpoint parameter (list converted to comma-separated string & bool converted to lower case string)
  * Removed /indexes/{id} endpoint (Get market index by id) -> cg.get_indexes_by_id()
  * Improved request exceptions handling (Fixed unbound local exception on GET request failure)

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
  * Fixed bug when querying exchanges and added more unit tests
  * First unit tests for coingecko wrappers
  * initial commit
