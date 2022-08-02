from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# open chrome driver
driver = webdriver.Chrome()
driver.implicitly_wait(5)

# go to url
driver.get("http://demostore.supersqa.com/")
time.sleep(3)

# click on 'My Account' tab
my_acct_tab = driver.find_element(By.LINK_TEXT, "My account")
my_acct_tab.click()
time.sleep(3)

# scroll the page up
driver.execute_script("window.scrollBy(0,300)")

# find username field and input username
u_name_field = driver.find_element(By.ID, "username")
u_name_field.send_keys("fakename")

# find password field and input username
p_field = driver.find_element("id", "password")
p_field.send_keys("aaaaaaa")

# click login button
login_btn = driver.find_element(By.NAME,'login')
login_btn.click()
time.sleep(3)

# get displayed error
errors_list_elm = driver.find_elements(By.CSS_SELECTOR, 'ul.woocommerce-error li')
first_error_elm = errors_list_elm[0]
displayed_error_text = first_error_elm.text

# verify the displayed error is as expected
expected_error = "Error: The password you entered for the username fakename is incorrect. Lost your password?"
assert expected_error == displayed_error_text, "Displayed error is not as expected."
print("Success.")

# close the browser
driver.quit()
