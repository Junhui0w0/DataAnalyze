from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

data_link_lst = ['https://www.overbuff.com/heroes?platform=pc&timeWindow=month', 'https://www.overbuff.com/heroes?platform=pc&timeWindow=3months', 'https://www.overbuff.com/heroes?platform=pc&timeWindow=6months', 'https://www.overbuff.com/heroes?platform=pc&timeWindow=year']
    #- 데이터는 현재 시즌 ~ 4개의 이전 시즌정보만 제공함
    #- blizzard 공식 페이지에서는 아직 유저 데이터를 제공하는 데이터, api가 없어 팬페이지를 통해 데이터 수집

for link in data_link_lst:
    file_name = link.split('=')[-1] #-> month / 3months / 6months / year

    driver.get(link)
    time.sleep(2)

    #- Overview 페이지 html 추출
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    time.sleep(2)

    with open(f'Tableau/html_parser/owbuff_{file_name}_overview.html', 'w', encoding='utf-8') as f:
        f.writelines(soup.prettify())


    #- Primary 페이지 추출
    btn_pri = driver.find_element(By.XPATH, "//button[contains(text(), 'Primary')]")
    btn_pri.click()
    time.sleep(2)

    
    # # #- Primary 페이지 html 추출
    # btn_pri_class = '.py-2.px-3.whitespace-no-wrap.font-medium.text-sm.rounded.bg-surface-500.hover\\:bg-surface-400'
    # btn_pri = driver.find_element(By.CSS_SELECTOR, btn_pri_class)
    # btn_pri.click()
    # time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # time.sleep(2)

    with open(f'Tableau/html_parser/owbuff_{file_name}_Primary.html', 'w', encoding='utf-8') as f:
        f.writelines(soup.prettify())

    btn_eli = driver.find_element(By.XPATH, "//button[contains(text(), 'Eliminations')]")
    btn_eli.click()
    time.sleep(2)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')


    # # #- Eliminations 페이지 html 추출
    # btn_eli_class = 'py-2 px-3 whitespace-no-wrap font-medium text-sm rounded bg-surface-500 hover:bg-surface-400'
    # btn_eli = driver.find_element(By.CSS_SELECTOR, btn_eli_class)
    # btn_eli.click()
    # time.sleep(2)

    # html = driver.page_source
    # soup = BeautifulSoup(html, 'html.parser')
    # time.sleep(2)

    with open(f'Tableau/html_parser/owbuff_{file_name}_Eliminations.html', 'w', encoding='utf-8') as f:
        f.writelines(soup.prettify())

driver.quit()