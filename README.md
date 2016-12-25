# hemnet-scraper

Scrape hemnet final prices. Uses postgres as a backend to manage state of the currently scraped items. The spider will skip items that have already been processed.

To simply scrape some items:
* Install project requirements, i.e. create a virtual env and do `pip install -r requirements.txt`
* Have a postgres server running and change `hemnet/settings.py` to match your setup. A table called hemnet_items will be created.
* Run the command `scrapy crawl hemnetspider -a start=1 -a stop=10`. This will scrape the first 10 pages from the list of final prices from hemnet.
* Check the table in postgres for the scraped data. `queries.sql` has some example queries that can be run.
