import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random


driver = webdriver.Chrome()
driver.implicitly_wait(10)

url = 'http://demostore.supersqa.com/my-account/'
driver.get(url)

# Variables
email_field_ID = 'reg_email'
password_field_ID = 'reg_password'

email_field = driver.find_element(By.ID, email_field_ID)
password_field = driver.find_element(By.ID, password_field_ID)

letters = string.ascii_lowercase
random_string = ''.join(random.choice(letters) for i in range(15))
random_email = random_string + '@supersqa.com'

# type in email and password field
email_field.send_keys(random_email)
time.sleep(1)
password_field.send_keys("2312ehwqndjkhiuenoldqw")
time.sleep(1)

# click on register button
register_button = driver.find_element(By.CSS_SELECTOR, 'button[value="Register"]')
register_button.click()

time.sleep(2)

logout_button = driver.find_element(By.CSS_SELECTOR, 'li.woocommerce-MyAccount-navigation-link--customer-logout a')

if logout_button.is_displayed():
    print("pass")
else:
    raise Exception("User not logged in after registering")
driver.quit()