
1.0.0 / 2019-11-17
==================

  * update tests
  * include more contract endpoints
  * include /coins/{id}/market_chart/range endpoint
  * basic methods for finance endpoints with tests
  * updated error handling
  * added check for json format in __request; coingecko returns a html string when something goes wrong in the request, which results in an error when json.loads is called on the html string.

0.4.0 / 2019-08-20
==================

  * include /exchanges/{id}/volume_chart endpoint

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
  * include /exchanges/list endpoint

0.1.0 / 2019-01-02
==================

  * add /coins/{id}/tickers endpoint
  * include events endpoints
  * include status_updates endpoints
  * update exchanges endpoints
  * update coins endpoints
  * include simple endpoints

0.0.2 / 2018-11-20
==================

  * use requests session to include retries
  * Fixed bug when querying exchanges and added more unit tests
  * First unit tests for coingecko wrappers
  * initial commit
