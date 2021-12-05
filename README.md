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
Because my initial attempts were countered by anti-scraping mechanism, such as [Google reCAPTCHA](https://www.google.com/recaptcha/about/). 

Google reCAPTCHA throws 5 to 10 reCAPTCHAs in one setting when a large amount of requests are detected from the same address, same user agent etc. 

I first wrote the scraper with **Requests** and **bs4**, which was stopped by reCAPTCHA about 900 jobs/10 mins in. Hoping to manually resolve the reCAPTCHAs, I switched to the browser automation route with **Selenium**, adding a logic so that when Google reCAPTCHA is thrown, the program pauses and waits for the user input. The program did pause about 1000 jobs in and I was able to manually resolve the reCAPTCHAs, but for some unknown reasons, the scraper always stopped after the resolution of reCAPTCHAs. 


At this stage, there are several solutions I considered:      
* Continue to debug to figure out why the scraper was stopped after the manual resolution of reCAPTCHAs;
* Get past the reCAPTCHA with speech-to-text transcribing the audio file in the accessability option (but this is clearly an abuse of features even if it works); or 
* Rotate user agents and/or proxies to avoid triggering anti-scraping mechanism 

I decided to go with the last option. 

Instead of manually setting up user agent rotation, I found out that this could be easily set up with [Scrapy](https://scrapy.org), which is also asynchronous. I refactored my script to use Scrapy and used [scrapy user agent middleware](https://pypi.org/project/scrapy-user-agents/). The script successfully scraped all 1500 job posts in Ontario and took about 3 mins.

### How to use
`requests + bs4` and `selenium + bs4` scrapers are in Jupyter Notebook. 

To run the `scrapy` scraper and save output in a json file (can also be csv or xml): 
```
$ cd scrapy
$ scrapy crawl indeedSpider -O output.json
```


