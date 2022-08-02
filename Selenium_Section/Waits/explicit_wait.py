from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
url = "file:///C:/Users/thomas.scattergood/Selenium_Section/Waits/page_with_slow_image.html"
driver.get(url)

#image = driver.find_element(By.ID, 'the_slow_image')
image = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'the_slow_image')))

if image.is_displayed():
    print("found image")
else:
    print("image not found")

driver.quit()