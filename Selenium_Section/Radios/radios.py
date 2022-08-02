import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
url = "file:///C:/Users/thomas.scattergood/PythonSeleniumMasterFolder/Selenium_Section/Radios/radios_example.html"
driver.get(url)
time.sleep(2)

expected_default_value = "21-40"
locator_by_value = f'input[name="age-group-radio"][value="{expected_default_value}"]'

# Example 1:  verify default is selected
# default_element = driver.find_element(By.CSS_SELECTOR, locator_by_value.format((expected_default_value)))
# assert default_element.is_selected(), "The default value of {} is not selected".format(expected_default_value)
# driver.quit()

# Example 2: verify all radio buttons are selectable
expected_values = ["21-40", "41-60", "61-80", "81+"]
all_radios = driver.find_elements(By.NAME, "age-group-radio")
assert len(all_radios) == len(expected_values), "the number of radios does not match the expected"

print("Expected values: {}".format(expected_values[::-1]))

for radio in all_radios:
    value = radio.get_attribute('value')
    print(value)

driver.quit()