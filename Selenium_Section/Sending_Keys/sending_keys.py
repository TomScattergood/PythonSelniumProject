from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = "http://demostore.supersqa.com/my-account/"
url2 = "http://demostore.supersqa.com"

# sending text
# driver.get(url)
# u_name = driver.find_element(By.ID, "username")
# u_name.send_keys("MyUserName")
# password = driver.find_element(By.ID, "password")
# password.send_keys("Password")
# time.sleep(3)
# submit_btn = driver.find_element(By.NAME, 'login')
# submit_btn.click()
#time.sleep(2)

# sending key input: enter
# driver.get(url2)
# search_field = driver.find_element(By.ID, 'woocommerce-product-search-field-0')
# search_field.send_keys("hoodie")
# time.sleep(2)
# search_field.send_keys(Keys.ENTER)
# time.sleep(2)
# driver.quit()

# tab example
driver.get(url)
u_name = driver.find_element(By.ID, "username")
u_name.send_keys("MyUserName")
time.sleep(2)
u_name.send_keys(Keys.TAB)
#password = driver.find_element(By.ID, "password")
# password.send_keys("Password")

