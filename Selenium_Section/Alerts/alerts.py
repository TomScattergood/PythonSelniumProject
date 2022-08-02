import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
url = "file:///C:/Users/thomas.scattergood/PythonSeleniumMasterFolder/Selenium_Section/Alerts/alerts_example.html"
driver.get(url)

time.sleep(1)
#Example 1: Button
alert1 = driver.find_element(By.CSS_SELECTOR, 'div#jsAlertExample button')
alert1.click()

time.sleep(1)

my_alert1 =driver.switch_to.alert
assert my_alert1.text == 'I am a JavaScript Alert', "Unexpected text on alert."
my_alert1.accept()
time.sleep(1)

#Example 2: Confirm button
confirm_button = driver.find_element(By.CSS_SELECTOR,'div#jsConfirmExample button')
confirm_button.click()
time.sleep(1)

confirm_alert = driver.switch_to.alert
#confirm message
confirm_alert.accept()
response_message = driver.find_element(By.ID, 'userResponse1').text
assert response_message == "Great! You will love it!", "Wrong message after accepting"
time.sleep(1)

#dismiss message
# confirm_alert.dismiss()
# response_message = driver.find_element(By.ID, 'userResponse1').text
# assert response_message == "Too bad!!! You would've loved it!", "Wrong message after accepting"
# time.sleep(1)

#Example 3 show a prompt:
prompt_button = driver.find_element(By.CSS_SELECTOR, 'div#jsPromptExample button')
prompt_button.click()
time.sleep(1)

prompt_alert = driver.switch_to.alert
time.sleep(1)
name = "Thomas"
prompt_alert.send_keys(name)
time.sleep(1)
prompt_alert.accept()
response_message = driver.find_element(By.ID, 'userResponse2').text
assert response_message == "You have entered: {}".format(name), "Wrong message after accepting"

time.sleep(1)

driver.quit()
