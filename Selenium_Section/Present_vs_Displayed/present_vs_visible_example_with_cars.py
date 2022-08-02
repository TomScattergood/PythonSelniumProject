from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 5)

url = "file:///C:/Users/thomas.scattergood/PythonSeleniumMasterFolder/Selenium_Section/Present_vs_Displayed/present_vs_visible_example_with_cars.html"
driver.get(url)

# bmw = driver.find_element(By.ID, 'bmw')
# bmw.click()
#
# series_6 = driver.find_element(By.CSS_SELECTOR, '#bmw-models > input[type=checkbox]:nth-child(7)')
# series_6.click()

# series_6 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#bmw-models > input[type=checkbox]:nth-child(7)')))

driver.find_element(By.ID, 'bmw').click()
series_6 = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#bmw-models > input[type=checkbox]:nth-child(7)')))
time.sleep(2)
driver.quit()
