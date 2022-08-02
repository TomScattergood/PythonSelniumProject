from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
url = "http://demostore.supersqa.com/"
driver.get(url)

#Link text
cart = driver.find_element(By.LINK_TEXT, 'Cart')
print(cart.text)
print(type(cart))

account = driver.find_element(By.LINK_TEXT, 'My account')
print(account.text)
print(type(account))

#partial link text
account_partial = driver.find_element(By.PARTIAL_LINK_TEXT, 'accou')
print(account_partial.text)
print(type(account_partial))

footer = driver.find_element(By.PARTIAL_LINK_TEXT, 'Built with ')
print(footer.text)
print(type(footer))


driver.quit()
