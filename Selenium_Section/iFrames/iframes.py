import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
url = "file:///C:/Users/thomas.scattergood/PythonSeleniumMasterFolder/Selenium_Section/iFrames/iFrames_example.html"
driver.get(url)

# example of basic button out of frame
driver.find_element(By.ID, 'btnOutFrame').click()
time.sleep(1)
my_alert = driver.switch_to.alert
my_alert_text = my_alert.text
assert my_alert_text == "Just Clicked Outside iFrame", "Should've gotten outside message"
my_alert.dismiss()
time.sleep(1)

#example of iFrame, button in a frame
#using 'WebElement'
# my_frame = driver.find_element(By.ID, 'myFrame1')
# driver.switch_to.frame(my_frame)
# driver.find_element(By.ID, 'btnInFrame').click()
# print(driver.switch_to.alert.text)
# time.sleep(1)
# driver.switch_to.alert.dismiss()
# time.sleep(1)

#Using 'ID'
# driver.switch_to.frame('myFrame1')
# driver.find_element(By.ID, 'btnInFrame').click()
# print(driver.switch_to.alert.text)
# time.sleep(1)
# driver.switch_to.alert.dismiss()
# time.sleep(1)

#Using 'index'
driver.switch_to.frame(0)
driver.find_element(By.ID, 'btnInFrame').click()
print(driver.switch_to.alert.text)
time.sleep(1)
driver.switch_to.alert.dismiss()
time.sleep(1)

# must switch back to click on button not in frame
driver.switch_to.default_content()
driver.find_element(By.ID, 'btnOutFrame').click()
time.sleep(1)
driver.switch_to.alert.dismiss()

driver.quit()
