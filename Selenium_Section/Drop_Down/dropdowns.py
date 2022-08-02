import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
url = "file:///C:/Users/thomas.scattergood/PythonSeleniumMasterFolder/Selenium_Section/Drop_Down/drop_down_example.html"
driver.get(url)

# Option 1: using select class
dropdown = driver.find_element(By.ID, 'age-range-select')
dropdown_object = Select(dropdown) # assigning variable
dropdown_object.select_by_index(3) # select by index in list
dropdown_object.select_by_value('21-40') # select by a value
all_options = dropdown_object.options # selecting all options in the dropdown box

for option in all_options: # printing all options in the dropdown box
    print(option.text)

# Option 2:
button = driver.find_element(By.ID, 'dropdownMenuButton')
button.click()
time.sleep(2)
my_option = driver.find_element(By.CSS_SELECTOR, '#dropdowns > div:nth-child(3) > div > ul > li:nth-child(1) > a')
my_option.click()


driver.quit()