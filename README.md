# watchfinder
WatchFinder
This is a Python script that uses the Scrapy library to scrape watch data from the Goldsmiths website. It retrieves information about men's watches, including their names, prices, and links.

Installation
To run this script, you need to have Python and Scrapy installed on your machine. Follow these steps to set up the project:

Clone the repository:
shell
Copy code
git clone <repository_url>
Navigate to the project directory:
shell
Copy code
cd watch-finder
Install the required dependencies using pip:
shell
Copy code
pip install scrapy
Usage
To start the scraping process, run the following command:

shell
Copy code
scrapy runspider spider.py
The script will start scraping the Goldsmiths website and retrieve watch data. The scraped data will be displayed in the console.

Script Overview
The script defines a Spider class that extends the scrapy.Spider class. Here's an overview of the script's structure and functionality:

The name attribute of the Spider class is set to 'watchFinder', and the start_urls list contains the initial URL to start scraping.

The parse method is the callback function that handles the response from the website. It extracts data from the HTML using CSS selectors.

Inside the parse method, the script loops through each product tile on the page and extracts the name, price, and link of the watch.

Data cleaning is performed to remove any unnecessary characters or formatting. The watch name is stripped of leading/trailing whitespaces, and the price is cleaned by removing commas.

The scraped data is then yielded as a dictionary containing the watch's name, price, and link. If an exception occurs while retrieving the price (indicating that the watch is sold out), the price is set to 'SOLD OUT'.

The script also handles pagination by extracting the query parameters from the current URL and determining the next page number. If a next page exists, a new request is made to scrape the next page.

The scraped data is displayed in the console. You can modify the script to save the data to a file or perform any other desired actions.

Additional Information
This script scrapes watch data from the Goldsmiths website. If you're interested in getting a valuation of a watch, the script currently does not include that functionality. However, you can consider using WatchFinder, a good website for watch valuations. They provide valuations based on the watch's condition, including whether it has the original box and card.

Please note that scraping websites may be subject to legal restrictions and terms of service. Ensure that you comply with the website's policies and obtain proper authorization before scraping any data.

**Disclaimer: This script is provided as-is and is for educational purposes only. Use it responsibly and respect the website's terms of service.
