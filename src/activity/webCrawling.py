from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome()

url = "https://vibe.naver.com/genre/OS101"

driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

print(soup)

# response = urlopen()  # 크롤링하고자하는 사이트
# soup = BeautifulSoup(response, "html.parser")  # html에 대하여 접근할 수 있도록

# print(soup)

# value = soup.find("div", {"class": "ellipses rank01"})
# print(value)

# value2 = value.soup.find("a")
# value2 = value2.title

# print(value2[0:4])


