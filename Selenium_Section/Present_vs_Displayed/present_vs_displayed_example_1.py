from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = "file:///C:/Users/thomas.scattergood/PythonSeleniumMasterFolder/Selenium_Section/Present_vs_Displayed/present_vs_displayed.html"
driver.get(url)

button1 = driver.find_element(By.ID, 'btn1')
#button1 = driver.find_element('id', 'btn1')
print("First button text is: {}".format(button1.text))

button2 = driver.find_element(By.ID, 'btn2')
print("Second button text is: {}".format(button2.text))

button3 = driver.find_element(By.ID, 'btn3')
print("Third button text is: {}".format(button3.text))

button4 = driver.find_element(By.ID, 'btn4')
print("Fourth button text is: {}".format(button4.text))

if button4.is_displayed():
    button4.click()
else:
    raise Exception("Button 4 is not displayed")

driver.quit()

