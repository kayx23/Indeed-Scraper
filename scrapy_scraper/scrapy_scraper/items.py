import scrapy

class jobItem(scrapy.Item):
    jobTitle = scrapy.Field()
    jobCompany = scrapy.Field()
    jobLocation = scrapy.Field()
    jobPostDate = scrapy.Field()
    today = scrapy.Field()
    jobSalary = scrapy.Field()
    jobSummary = scrapy.Field()
    jobURL = scrapy.Field()