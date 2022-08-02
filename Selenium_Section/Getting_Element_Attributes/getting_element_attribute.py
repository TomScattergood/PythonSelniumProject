from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = "http://demostore.supersqa.com/"
driver.get(url)

#example 1 is placeholder
searchbar = driver.find_element(By.ID, "woocommerce-product-search-field-0")
place_holder = searchbar.get_attribute('placeholder')
if place_holder != "Search products…":
    raise Exception("Place holder for search field is not as expected. Actual: {}".format(place_holder))
else:
    print("pass")


#example 2: see which tab is selected
# first click on my account
# account = driver.find_element(By.CSS_SELECTOR, '#site-navigation > div:nth-child(2) > ul > li.page_item.page-item-9 > a')
# account.click()
# time.sleep(2)
# nav_items = driver.find_elements(By.CSS_SELECTOR, 'ul.nav-menu li')
# for item in nav_items:
#     item_class = item.get_attribute('class')
#     if 'current_page_item' in item_class:
#         print("The selected tab is: {}".format(item.text))

#example 3: get link url
product_link = driver.find_element(By.CSS_SELECTOR, 'li.product a')
product_url = product_link.get_attribute('href')
print("The url for product is: {}".format(product_url))

driver.quit()

#import pdb; pdb.set_trace()