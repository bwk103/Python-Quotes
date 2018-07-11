import requests
from bs4 import BeautifulSoup

class Scraper:

  def __init__(self, page_number=1):
    self.base_url = "http://quotes.toscrape.com/"
    self.query = "page/"
    self.page_number = page_number
    self.quote_list = []

  def quote_list_length(self):
    return len(self.quote_list)

  def get_quote_list(self):
    return list(self.quote_list)

  def get_quotes(self):
    while self.page_number < 11:
      complete_url = self.base_url + self.query + str(self.page_number)
      response = requests.get(complete_url)
      self.page_number += 1
      self._format_response(response)

  def get_bio(self, link):
    response = requests.get(link)
    data = BeautifulSoup(response.text, 'html.parser')
    dob = data.find(class_= 'author-born-date').get_text()
    pob = data.find(class_='author-born-location').get_text()
    return f"This person was born on {dob} {pob}"

  def _format_response(self, resp):
    data = BeautifulSoup(resp.text, "html.parser")
    quotes = data.find_all(class_='quote')
    self._format_list(quotes)
  
  def _format_list(self, quotes):
    for quote in quotes:
      text = quote.find('span').get_text()
      author = quote.find(class_="author").get_text()
      link = quote.find('a')['href']
      self.quote_list.append([text, author, link])