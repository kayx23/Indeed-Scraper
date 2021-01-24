# Indeed Job Scraper (Canada)

Built three scrapers to scrape Indeed jobs in Ontario, Canada, with: 
1. requests & bs4
2. selenium & bs4
3. scrapy

### How many jobs are we expecting to scrape? 

1500 jobs. Indeed displays 15 jobs a page so we have 100 pages to get through. 

As of Jan 23, 2021, around 82,000 jobs in Ontario were listed on Indeed. A lot of these posting are considered highly similar by Indeed and therefore are not displayed in a regular research: 

<div style="text-align:center"><img src="https://user-images.githubusercontent.com/39619599/105637543-2236d680-5e3c-11eb-9156-b4457da3cda0.png"></div>

I decided to not scrape these similar postings in this excercise. 

### Why are there three scrapers? 
Google reCAPTCHA throws 5 to 10 reCAPTCHAs in one setting when detecting a large amount of requests coming from the same proxy, same user agent. I first wrote the scraper with requests and bs4, which encountered by reCAPTCHA about 900 jobs into scraping. With the same bs4 code, I switched to selenium to add a logic so that when detecting Google reCAPTCHA, pause the program for user input to resolve. The program did pause when there is a reCAPTCHA (about 1000 jobs in), but for some reasons I did not spent too much time looking into, the scraper stopped after I manually resolved the blocking reCAPTCHA. 

From here, there are several solutions I thought of:      
* continue to debug the "pausing for the user to resolve reCAPTCHA" logic until it works;
* get past the reCAPTCHA by speech-to-text transcribing (abusing?) the audio file in the accessability option; 
* rotate user agents and/or proxies so that the scraper does not get reCAPTCHA blokage in the first place

Rotating user agents is the easiest option, and is probably sufficient since I only have 500 more jobs to scrape. I could have mannually set up user agent rotation with requests or selenium, which should have really served my purpose. At the same time, I started to play with [Scrapy](https://scrapy.org), liked its asynchronous design, and re-wrote my script with it. I also found a [scrapy user agent middleware](https://pypi.org/project/scrapy-user-agents/) that I can directly use, so I ended up using Scrapy which finally scraped all 1500 jobs, which took about 3 mins.

### How to use
`requests + bs4` and `selenium + bs4` scrapers are in Jupyter Notebook. 

To run the `scrapy` scraper and save output in a json file (can also be csv or xml): 
```
$ cd scrapy
$ scrapy crawl indeedSpider -O output.json
```
Make sure you have the dependencies in the `requirements.txt`

