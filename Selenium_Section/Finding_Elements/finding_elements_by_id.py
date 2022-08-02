import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pdb

url = "http://demostore.supersqa.com"
url2 = "http://demostore.supersqa.com/my-account/"
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

cart = driver.find_element(By.ID,"site-header-cart")
cart.click()
time.sleep(2)
driver.back()
time.sleep(2)

driver.get(url2)
time.sleep(2)
u_name = driver.find_element(By.ID, "username")
u_name.send_keys("MyUserName")
password = driver.find_element(By.ID, "password")
password.send_keys("Password")
time.sleep(3)
driver.quit()
