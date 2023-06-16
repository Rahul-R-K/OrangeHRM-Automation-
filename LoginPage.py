from selenium.webdriver.common.by import By


#self.driver.find_element(By.NAME,"username")
#password = self.driver.find_element(By.NAME,"password")
#submit = self.driver.find_element(By.XPATH,"//button[@type='submit']")
class HomePage:

    def __init__(self,driver):
        self.driver = driver

    Username = (By.NAME,"username")
    Password = (By.NAME,"password")
    Submit = (By.XPATH,"//button[@type='submit']")

    def enterUserName(self):
        return self.driver.find_element(*HomePage.Username)
    def enterPassword(self):
        return  self.driver.find_element(*HomePage.Password)
    def enterSubmitButton(self):
        return self.driver.find_element(*HomePage.Submit)
