import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

url = "http://demostore.supersqa.com/"

driver.get(url)
time.sleep(2)
cart = driver.find_element(By.CSS_SELECTOR, '#site-header-cart > li:nth-child(1) > a')
cart.click()
time.sleep(1)
print(type(cart))
driver.get(url)
account = driver.find_element(By.XPATH, '//*[@id="site-navigation"]/div[1]/ul/li[4]/a')
account.click()
time.sleep(1)
print()
print(type(account))
time.sleep(2)
driver.quit()