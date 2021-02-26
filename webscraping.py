import time
import requests
import pandas as pd 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.opera.options import Options

url = ("http://www.buscacep.correios.com.br/sistemas/buscacep/BuscaCepEndereco.cfm")
time.sleep(10)

option = Options()
option.headless = True
driver = webdriver.Opera(options=option)

driver.get(url)

driver.quit()


# 1. Getting the HTML Content from the URL
# 2. Parsing the HTML Content with BeautifulSoup
# 3. Extructuring the content into a Data Frame - Pandas
# 4. Transforming the Data to a Dictionary.
# 5. Converting and saving the Data like a JSON Archieve




#PIP: 
    #pip install requests
    #pip install pandas 
    #pip install lxml
    #pip install beautifulsoup
    #pip install selenium

