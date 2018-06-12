import scrapy


class SriLankaTravelSpder(scrapy.Spider):
    name = "SL_Travel"

    def start_requests(self):
        base_url = "http://www.srilanka.travel/tourist-guides?page="
        urls = []
        for i in range(120,121):
            urls.append(base_url+str(i))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("=")[-1]
        filename = 'data/sltravel/sltravel-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)