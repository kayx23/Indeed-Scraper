import scrapy
from ..items import jobItem
from datetime import datetime

today = datetime.today().strftime('%Y-%m-%d')

class indeedSpider(scrapy.Spider): 
    name = 'indeedSpider'
    start_urls = ['https://ca.indeed.com/jobs-in-ontario']

    def parse(self, response):

        # response.xpath("//div[contains(@class, 'jobsearch-SerpJobCard')]")
        for card in response.css('div.jobsearch-SerpJobCard'):

            job = jobItem()

            job['jobTitle'] = card.css("h2 a::attr(title)").get()

            # sometimes there's a <a> tag within the <span>
            if card.css("span.company a"):
                job['jobCompany'] = card.css("span.company a::text").get().strip()
            else:
                job['jobCompany'] = card.css("span.company ::text").get().strip()
            # job['jobCompany'] = card.xpath(".//span[@class='company']//text()").get().strip() doesn't work

            if card.css('div.location'):
                job['jobLocation'] = card.css('div.location ::text').get()   # get() is the same as extract_first() 
            else:
                job['jobLocation'] = card.css('span.location ::text').get()

            job['jobPostDate'] = card.css("span.date ::text").get()
            
            job['today'] = today

            if card.css('div.salaryText'):
                job['jobSalary'] = card.css("span.salaryText ::text").get()
            else:
                job['jobSalary'] = ''

            # concatenate into one string
            # because when there could be <b> tags in text for keywords
            # which causes one sentence to break into multiple lines
            job['jobSummary'] = " ".join(card.css("div.summary ul li ::text").getall())

            job['jobURL'] = "https://ca.indeed.com" + card.css("h2 a::attr(href)").get()

            yield job
        
        # going to the next page
        next_page = response.css("a[aria-label='Next']::attr(href)").get()
        if next_page is not None:
            # can directly use the relative url with response.follow
            yield response.follow(next_page, callback=self.parse)