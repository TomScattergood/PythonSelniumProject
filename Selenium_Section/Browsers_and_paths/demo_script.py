from selenium import webdriver
import time

#open chrome driver
#option1 (selenium 3 only)
#driver = webdriver.Chrome(executable_path=r'C:\Users\thomas.scattergood\Selenium_Section\chromedriver.exe')
#driver.implicitly_wait(5)

#option2 adding the executable into system path
driver = webdriver.Chrome()
driver.implicitly_wait(5)


#go to url
url = "http://demostore.supersqa.com"
driver.get(url)
driver.maximize_window()
time.sleep(3)
driver.quit()