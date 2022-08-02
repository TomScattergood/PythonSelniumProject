import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def add_item_to_cart():
    driver.find_element(By.CLASS_NAME, 'add_to_cart_button').click()
    wait.until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="site-header-cart"]/li[1]/a/span[2]'), '1 item')
    )


def click_cart():
    driver.find_element(By.XPATH, '//*[@id="site-header-cart"]/li[1]/a').click()
    time.sleep(1)


def input_coupon_and_hit_enter():
    coupon_field = wait.until(EC.visibility_of_element_located((By.ID, 'coupon_code'))) #waits for coupon element to be visible
    coupon_field.send_keys(coupon) # sends coupon variable to element
    coupon_field.send_keys(Keys.ENTER)


def verify_total_is_0():
    wait.until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="post-7"]/div/div/div[2]/div/table/tbody/tr[3]/td/strong/span'), '$0.00'))


if __name__ == '__main__':
    coupon = "SSQA100"

    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    url = "http://demostore.supersqa.com/"
    driver.get(url)

    add_item_to_cart()
    click_cart()
    input_coupon_and_hit_enter()
    verify_total_is_0()
    print("PASS")
    driver.quit()
