from bs4 import BeautifulSoup
from selenium import webdriver
import time

driver = webdriver.Chrome()
link = 'https://www.overbuff.com/heroes?platform=pc&timeWindow=month'
driver.get(link)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
time.sleep(2)

with open('Tableau/owbuff_this_month.html', 'w', encoding='utf-8') as f:
    f.writelines(soup.prettify())

    driver.quit()