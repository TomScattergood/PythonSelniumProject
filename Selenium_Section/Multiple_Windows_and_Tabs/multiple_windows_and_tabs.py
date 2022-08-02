import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()
url = "file:///C:/Users/thomas.scattergood/PythonSeleniumMasterFolder/Selenium_Section/Multiple_Windows_and_Tabs/windows-and_tabs_example.html"
driver.get(url)

time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="windows"]/a[1]').click()
time.sleep(2)

print("Before switching focus: " + driver.title)

all_window_handles = driver.window_handles
original_window = all_window_handles[0]
new_window = all_window_handles[1]

driver.switch_to.window(new_window) # switching to new window
print("After switching focus: " + driver.title)
my_heading = driver.find_element(By.XPATH, '/html/body/h1').text
driver.close() # closing new window tab

driver.switch_to.window(original_window) # switching back to original window

time.sleep(1)

driver.quit()
