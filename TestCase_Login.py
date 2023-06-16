import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BaseClass import BaseClass
from LoginPage import HomePage

class Testcase_Login(BaseClass):
    def test_TC_Login_01(self):
        try:
            self.verifythePresence("username")
            username = HomePage(self.driver)
            username.enterUserName().send_keys("Admin")
            password = HomePage(self.driver)
            password.enterPassword().send_keys("admin123")
            submit = HomePage(self.driver)
            submit.enterSubmitButton().click()
        except Exception as e:
            print(f"Caught exception: {type(e).__name__}: {e}")

    def test_TC_Login_02(self):
        try:
            self.verifythePresence("username")
            username = HomePage(self.driver)
            username.enterUserName().send_keys("Admin")
            password = HomePage(self.driver)
            password.enterPassword().send_keys("InvalidPasword")
            submit = HomePage(self.driver)
            submit.enterSubmitButton().click()
        except Exception as e:
            print(f"Caught exception: {type(e).__name__}: {e}")



