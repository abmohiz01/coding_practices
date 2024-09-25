import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('User-Agent: Mozilla/5.0')
driver = webdriver.Chrome(options=options)
def facebookLogin():


    driver.get('https://www.facebook.com')
    driver.find_element(By.ID, 'email').send_keys('$$$$$$$$$$$$@gmail.com')
    driver.find_element(By.ID, 'pass').send_keys('$$$$$$$$$$')
    driver.find_element(By.XPATH,
                        '/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button').click()
    time.sleep(10)

facebookLogin()