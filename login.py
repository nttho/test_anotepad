from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException


class TestLogin:

    def __init__(self):
        self.driver = Chrome(executable_path='chromedriver.exe')

    def open_page(self, url):
        self.driver.get(url)
        self.driver.maximize_window()

    def close_all_browsers(self):
        self.driver.quit()

    def get_element(self, locator):
        by = locator.split(':')[0]
        value = ':'.join(locator.split(':')[1:])
        return self.driver.find_element(by, value)

    def input_text(self, locator, text):
        element = self.get_element(locator)
        if element:
            element.send_keys(text)

    def click(self, locator):
        element = self.get_element(locator)
        if element:
            element.click()

    def is_element_present(self, locator):
        try:
            self.get_element(locator)
        except NoSuchElementException:
            print("Element does not present")
            return False
        return True


if __name__ == '__main__':
    rs = TestLogin()

    # Login with valid credentials
    rs.open_page("https://anotepad.com/")
    rs.click("xpath://a[@href='/create_account']")
    rs.input_text("id:loginEmail", "valid_email")
    rs.input_text("xpath://input[@id='password' and @placeholder='Enter Password']", "valid_password")
    rs.click("xpath://button[text()='Login']")
    rs.is_element_present("xpath://a[@href='/logout']")
    rs.close_all_browsers()

    # Empty password
    rs.open_page("https://anotepad.com/")
    rs.click("xpath://a[@href='/create_account']")
    rs.input_text("id:loginEmail", "valid_email")
    rs.input_text("xpath://input[@id='password' and @placeholder='Enter Password']", "")
    rs.click("xpath://button[text()='Login']")
    rs.is_element_present("xpath://strong[text()='Email and password are required']")
    rs.close_all_browsers()

    # Empty username
    rs.open_page("https://anotepad.com/")
    rs.click("xpath://a[@href='/create_account']")
    rs.input_text("id:loginEmail", "")
    rs.input_text("xpath://input[@id='password' and @placeholder='Enter Password']", "valid_password")
    rs.click("xpath://button[text()='Login']")
    rs.is_element_present("xpath://strong[text()='Email and password are required']")
    rs.close_all_browsers()

    # Empty username and password
    rs.open_page("https://anotepad.com/")
    rs.click("xpath://a[@href='/create_account']")
    rs.input_text("id:loginEmail", "")
    rs.input_text("xpath://input[@id='password' and @placeholder='Enter Password']", "")
    rs.click("xpath://button[text()='Login']")
    rs.is_element_present("xpath://strong[text()='Email and password are required']")
    rs.close_all_browsers()

    # Invalid Username
    rs.open_page("https://anotepad.com/")
    rs.click("xpath://a[@href='/create_account']")
    rs.input_text("id:loginEmail", "invalid_email")
    rs.input_text("xpath://input[@id='password' and @placeholder='Enter Password']", "valid_password")
    rs.click("xpath://button[text()='Login']")
    rs.is_element_present("xpath://strong[text()='Email and password do not match']")
    rs.close_all_browsers()

    # Invalid Password
    rs.open_page("https://anotepad.com/")
    rs.click("xpath://a[@href='/create_account']")
    rs.input_text("id:loginEmail", "valid_email")
    rs.input_text("xpath://input[@id='password' and @placeholder='Enter Password']", "invalid_password")
    rs.click("xpath://button[text()='Login']")
    rs.is_element_present("xpath://strong[text()='Email and password do not match']")
    rs.close_all_browsers()

    # Invalid Username and Password
    rs.open_page("https://anotepad.com/")
    rs.click("xpath://a[@href='/create_account']")
    rs.input_text("id:loginEmail", "invalid_email")
    rs.input_text("xpath://input[@id='password' and @placeholder='Enter Password']", "invalid_password")
    rs.click("xpath://button[text()='Login']")
    rs.is_element_present("xpath://strong[text()='Email and password do not match']")
    rs.close_all_browsers()
