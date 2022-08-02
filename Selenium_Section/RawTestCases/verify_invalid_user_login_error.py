import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class InvalidUserLoginError:
    invalid_email = 'abc@supersqa.com'
    url = "http://demostore.supersqa.com/my-account/"
    expected_message = "Unknown email address. Check again or try your username."

    def go_to_my_account(self):
        self.driver.get(self.url)

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        time.sleep(2)

    def input_email(self):
        field = self.driver.find_element(By.ID, 'username')
        field.send_keys(self.invalid_email)
        # field.send_keys(InvalidUserLoginError.invalid_email)

    def input_password(self):
        field = self.driver.find_element(By.ID, 'password')
        field.send_keys('abcedfg')

    def click_login(self):
        self.driver.find_element(By.NAME, "login").click()

    def verify_error_message(self):
        error_element = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul/li')
        displayed_error = error_element.text
        assert displayed_error == self.expected_message, "The displayed error is not expected"
        print("pass")

    def main(self):
        self.go_to_my_account()
        self.input_email()
        self.input_password()
        time.sleep(2)
        self.click_login()
        self.verify_error_message()
        self.driver.quit()


if __name__ == '__main__':
    obj = InvalidUserLoginError()
    obj.main()
