import scrapy

class Spider(scrapy.Spider):
    name = 'watchFinder'
    start_urls = ['https://www.goldsmiths.co.uk/c/Watches/Mens-Watches?q=%3Arelevance&page=1&sort=relevance']

    def parse(self, response):
        for product in response.css('div.productTile'):
            try:
                name = product.css('div.productTileName::text').get()
                price = product.css('div.productTilePrice::text').get().replace('£', '')
                link = product.css('a').attrib['href']
                
                # Perform data cleaning
                name = name.strip()  # Remove leading/trailing whitespaces
                price = price.replace(',', '')  # Remove comma from price
                
                yield {
                    'name': name,
                    'price': price,
                    'link': link,
                }
            except:
                name = product.css('div.productTileName::text').get()
                link = product.css('a').attrib['href']
                
                # Perform data cleaning
                name = name.strip()  # Remove leading/trailing whitespaces
                
                yield {
                    'name': name,
                    'price': 'SOLD OUT',
                    'link': link,
                }

        query_params = response.url.split('?')[-1]  # Extract query parameters
        next_page_number = int(response.css('#pagination-LoadMore::attr(data-next-page)').get())
        if next_page_number:
            next_page_url = f'https://www.goldsmiths.co.uk/c/Watches/Mens-Watches?{query_params}&page={next_page_number}'
            yield scrapy.Request(next_page_url, callback=self.parse)

#add the valuation of the watch relative with the value  the watch has with box + card = watchfinder = good website 