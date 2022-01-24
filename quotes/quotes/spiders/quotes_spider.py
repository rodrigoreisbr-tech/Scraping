import scrapy

class QuotesSpide(scrapy.Spider):
        name = "quotes"
        start_urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/1/"
        ]

        def parse(self, response):
            for quotes in response.css('div.quote'):
               yield{
                   'text':quotes.css('span.text::text').get(),
                   'text2': quotes.css('span.text::text').get(),
                   'author3': quotes.css('small.author::text').get(),
                   'tags': quotes.css('div.tags a.tag::text').getall()
               }

