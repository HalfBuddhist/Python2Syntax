"""
This modules implements the CrawlSpider which is the recommended spider to use
for scraping typical web sites that requires crawling pages.

See documentation in docs/topics/spiders.rst
"""

print "dmoz_spider's name:\t", __name__
print "dmoz_spider's package:\t", __package__


import scrapy
if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    # sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
else:

# print "dmoz_spider's name:\t", __name__
# print "dmoz_spider's package:\t", __package__


class DmozSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org", "blog.dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        print 'url is:\t', response.url
        filename = response.url.split("/")[-2]
        with open(filename, 'wb') as f:
            f.write(response.body)
        #
        # print 'title'.ljust(20), 'link'.ljust(50), 'desc'.ljust(20)
        # for sel in response.xpath('//ul/li'):
        #     # title = sel.xpath('a/text()').extract()
        #     # link = sel.xpath('a/@href').extract()
        #     # desc = sel.xpath('text()').extract()
        #     # # print title, link, desc
        #     # print str(title).ljust(20), str(link).ljust(50), str(desc).ljust(20)
        #     item = DmozItem()
        #     item['title'] = sel.xpath('a/text()').extract()
        #     item['link'] = sel.xpath('a/@href').extract()
        #     item['desc'] = sel.xpath('text()').extract()
        #     yield item