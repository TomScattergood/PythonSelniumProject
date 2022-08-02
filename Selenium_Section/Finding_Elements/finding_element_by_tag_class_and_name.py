from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

url = "http://demostore.supersqa.com/"

driver.get(url)

# finding by 'class name' example
product = driver.find_element(By.CLASS_NAME, 'product') #finds 1 element with class name of product
products = driver.find_elements(By.CLASS_NAME, 'product') # finds all elements with class name of product

# print(product)
# print("=========")
# print(len(products))


# finding by 'name' example
orderby = driver.find_element(By.NAME, 'orderby')
# print(orderby.text)


# finding by 'tag' example
all_a_links = driver.find_elements(By.TAG_NAME, 'a')
print(f"Found number of 'a' tag: {len(all_a_links)}")
all_li_links = driver.find_elements(By.TAG_NAME, 'li')
print(f"Found number of 'a' tag: {len(all_li_links)}")
driver.quit()