import scrapy

class Spider(scrapy.Spider):
    name = 'watchFinder'
    start_urls = ['https://www.goldsmiths.co.uk/c/Watches/Mens-Watches']


    def parse(self, response):
        for products in response.css('div.productTile'):
            try:
                yield {
                    #these are the commands that were entered into the terminal - gets the info from the css selectors
                    #stores them within the specific variables 
                    'name': products.css('GETPRODUCTTEXTREQUEST::text').get(),
                    'price':products.css('GET PRODUCTS::text ').get(),
                    'link': products.css('GETLINKTOPROCUCSTS::text').attrib['href'],
                }
            except:
                yield{
                    'name': products.css('GETPRODUCTTEXTREQUEST::text').get(),
                    'price':products.css('GET PRODUCTS::text ').get(),
                    'link': products.css('GETLINKTOPROCUCSTS::text').attrib['href'],
                }


        #use this to scrape watches https://watchcharts.com/listings?source=forums  USE . IN BETWEEN IF THE CLASS NAME CONTAINS GAPS 
        next_page = response.css('class.name.if.space').attrib['href']
        #this will return a link for the next page which we can then use to scrape 
        #checking if ther is a next page 
        if next_page is not None:
            #follow the link - call the parse function to scrape the webpage  
            yield response.follow(next_page,callback = self.parse())