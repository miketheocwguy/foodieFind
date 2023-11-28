from bs4 import BeautifulSoup
import requests

source = requests.get("https://www.walmart.ca/en/shop/cyber-week/0017056968655?catId=10011&icid=home_page_gifts_and_seasonal_toys_58168_RXPPI5JLJE").text

soup = BeautifulSoup(source, "lxml")

print(soup.prettify())