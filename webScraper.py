# # EXAMPLE1 JSON DATA TO LEARN FROM 

# import requests
# from bs4 import BeautifulSoup
# import json


# url = 'https://www.cdkeys.com/pc'
# # resposnse stores the response from the request such as 200, 404 etc
# # soup stores the actual html of the webpage
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# # print (response)
# # print (soup)

# oldPrices = soup.select('span[data-price-type="oldPrice"] span')
# products = soup.select('li.product-item')
# # print(oldPrices)
# # print(products)

# for i in range(len(products)):
#    # convert the data in the html attributes to json 
#    prod = json.loads(products[i]['data-impression'])

#    # print the product info 
#    print(f"{prod['name']} - ${prod['price']} - {oldPrices[i].text}")


# # EXAMPLE 2 HTML TAGS
# Import necessary libraries
import requests  # for making HTTP requests
from bs4 import BeautifulSoup  # for web scraping

# Define the URL of the webpage you want to scrape
url = 'https://www.bbc.co.uk/news'

# Make a GET request to the URL and store the response
response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content of the webpage
soup = BeautifulSoup(response.content, 'html.parser')

# Select all <span> elements with the class 'mw-headline'
titleName = soup.select('a.nw-o-link')


# Iterate through each selected element
for title in titleName:
    # Extract the text content of each <span> element
    title_text = title.text
    
    # Print the text content
    print(title_text)


