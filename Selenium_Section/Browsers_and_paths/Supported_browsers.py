import time

from selenium import webdriver

# variables
url = "http://demostore.supersqa.com/product/beanie-with-logo/"

# chrome
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()
time.sleep(2)
driver.quit()

#firefox
# driver = webdriver.Firefox()
# driver.get(url)
# driver.maximize_window()
# time.sleep(2)
# driver.quit()