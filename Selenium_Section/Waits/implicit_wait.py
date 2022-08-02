from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "file:///C:/Users/thomas.scattergood/Selenium_Section/Waits/page_with_slow_image.html"
driver.implicitly_wait(10)

driver.get(url)
image = driver.find_element(By.ID, 'the_slow_image')
image.click()
print("found image")
driver.quit()