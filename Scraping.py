from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
def scrolling(url):
    driver.get(url)
    time.sleep(5)

    element = driver.find_element(By.TAG_NAME, "body")
    while True:
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(4)
        print(driver.page_source)
        driver.close()

scrolling("https://eshop.macsales.com/upgrades/macbook-12-inch-mid-2017-1.4-ghz-m7/external-storage")

'''Scraping multiple sites '''

for i in range(1,20):
    driver.get(f"https://eshop.macsales.com/upgrades/macbook-12-inch-mid-2017-1.4-ghz-m7/external-storage&query={i}")
    