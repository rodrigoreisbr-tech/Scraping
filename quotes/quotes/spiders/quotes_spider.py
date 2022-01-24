#Comando para rodar no terminal

# Este comando ira extrair o json
#scrapy crawl quotes -o quotes.json

# Este comando permite checar os camano via terminal
#scrapy shell https://quotes.toscrape.com/page/1/


import scrapy


def limpar(text):
    text = text.strip(u'\u201c')
    text = text.strip(u'\u201d')
    return text

class QuotesSpide(scrapy.Spider):
        name = "quotes"
        #text = ""
        start_urls = [
            "https://quotes.toscrape.com/page/1/"
        ]

        def parse(self, response):

            for quotes in response.css('div.quote'):
               yield{
                   'text': limpar(quotes.css('span.text::text').get()),
                   'author': quotes.css('small.author::text').get(),
                   'tags': quotes.css('div.tags a.tag::text').getall()
               }

            next_page = response.css('li.next a::attr(href)').get()
            if next is not None:
                yield response.follow(next_page, callback=self.parse)


