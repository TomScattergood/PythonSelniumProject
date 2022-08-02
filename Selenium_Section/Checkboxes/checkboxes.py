import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
url = "file:///C:/Users/thomas.scattergood/PythonSeleniumMasterFolder/Selenium_Section/Checkboxes/checkbox_example.html"
driver.get(url)
time.sleep(2)

#example 1
# to_select_value = "61-80"
# locator_by_value = f'input[name="age-group-checkbox"][value="{to_select_value}"]'
#
# my_choice = driver.find_element(By.CSS_SELECTOR, locator_by_value)
# my_choice.click()

#assert my_choice.is_selected(), "After clicking value of {} it is not selected".format(to_select_value)

# if my_choice.is_selected():
#     print("value of {} is selected".format(to_select_value))
# else:
#     print("fail")

# example 2: verify number of checkboxes and if they are selectable
expected_number_of_options = 4
all_checkboxes = driver.find_elements(By.NAME, 'age-group-checkbox')
assert len(all_checkboxes) == expected_number_of_options, "Number of checkboxes is not the expected"

for checkbox in all_checkboxes:
    checkbox.click()
    value = checkbox.get_attribute('value')
    if checkbox.is_selected():
        print("Checkbox with value {} is selectable".format(value))
    else:
        raise Exception("Value {} is not selectable".format(value))
driver.quit()