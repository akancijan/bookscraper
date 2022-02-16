# Scrapy spider
Testing out Scrapy package for gathering data from sites.

Site for scraping is : http://books.toscrape.com/

# Workflow
Spider starts at the homepage : 
1. Grabs the list of all categories for books and visits the links once
2. Scrapes title, price, img_url and details_url for each book
3. If a next page button is present it visits the next page and repeats step 2
4. After all categories are scrapped the program stops

# How to run the Spider
Execute the following command in cmd : 
> scrapy crawl spidernamehere -o file_name_to_save.csv

You can also output .csv or .json file
