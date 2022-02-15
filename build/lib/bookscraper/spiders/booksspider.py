import scrapy
import shub


class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = ['http://books.toscrape.com/index.html']
    #
    base_site_url = 'http://books.toscrape.com/'
    baste_site_catalogue_url = 'http://books.toscrape.com/catalogue/'

    def parse(self, response):
        category_links = response.css('div.side_categories ::attr(href)')
        category_links.pop(0)
        for link in category_links:
            print(link)
        for link in category_links:
            yield response.follow(link.get(), callback=self.parse_category)

    def parse_category(self, response):
        for book in response.css('article.product_pod'):
            yield {
                'title': book.css('h3 ::attr(title)').get(),
                'price_in_pounds': book.css('p.price_color::text').get().replace('£', ''),
                'img_url': self.base_site_url + book.css('div.image_container ::attr(src)').get().replace('../', ''),
                'details_url:': self.baste_site_catalogue_url + book.css('div.image_container ::attr(href)').get().replace('../', '')
            }

        try:
            next_page_url = response.url.rsplit('/', 1)[0] + '/' + response.css('li.next ::attr(href)').get()
        except TypeError:
            print('Reached last page')
            next_page_url = None
        if next_page_url is not None:
            yield response.follow(next_page_url, callback=self.parse_category)
