import sys,time
sys.stdout.reconfigure(encoding='utf-8')


from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
options = Options()
#options.add_argument('--headless')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('https://shopee.tw/%E5%B1%85%E5%AE%B6%E7%94%9F%E6%B4%BB-cat.11040925')
time.sleep(5)

cards= driver.find_elements(By.CSS_SELECTOR,"li[class='col-xs-2-4 shopee-search-item-result__item']")
items = []
for card in cards:
    title = card.find_element(By.CSS_SELECTOR,"div[class='DgXDzJ rolr6k Zvjf4O']").text
    price = card.find_element(By.CSS_SELECTOR,"div[class='bPcAVl IWBsMB']").text
    link = card.find_element(By.TAG_NAME,"a").get_attribute('href')
    items.append((title,price,link))

print(items)


