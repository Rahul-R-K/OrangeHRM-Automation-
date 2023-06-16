import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from BaseClass import BaseClass
from LoginPage import HomePage
from PIM_Page import PimPage



class Testcase_PIM(BaseClass):
    def test_TC_PIM_01(self):
        try:
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
            self.verythePresence2("//aside/nav/div[2]/ul/li[2]")
            PIM = PimPage(self.driver)
            PIM.ClickPIM().click()
            self.verifyaddpresence("(//button[@type='button'])[contains(.,'Add')]")
            adduser = PimPage(self.driver)
            adduser.ClickAdd().click()
            time.sleep(2)
            firstname = PimPage(self.driver)
            firstname.enterFirstName().send_keys("Rahul")
            middlename = PimPage(self.driver)
            middlename.enterMiddleName().send_keys("R")
            lastname = PimPage(self.driver)
            lastname.enterLastName().send_keys("K")
            employeeID = PimPage(self.driver)
            employeeID.enterEmployeeID().send_keys("1234")
            Img = self.driver.find_element(By.XPATH,"//input[@class='oxd-file-input']")
            Img.send_keys('C:/Users/rahul.rk.REDIM.001/PycharmProjects/Guvi1/image1.jpg')
            element = self.driver.find_element(By.XPATH, "//input[@type='checkbox']")
            action = ActionChains(self.driver)
            action.click(on_element=element)
            action.perform()
            time.sleep(1)
            username = PimPage(self.driver)
            username.enterUserNmae().send_keys("rahul1597")
            time.sleep(1)
            password = PimPage(self.driver)
            password.enterPassword().send_keys("guvi1234")
            time.sleep(1)
            confrimpassword = PimPage(self.driver)
            confrimpassword.enterConformPassword().send_keys("guvi1234")
            time.sleep(1)
            save = PimPage(self.driver)
            save.ClickSaveButton().click()
        except Exception as e:
            print(f"Caught exception: {type(e).__name__}: {e}")



    def test_TC_PIM_02(self):
        try:
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
            self.verythePresence2("//aside/nav/div[2]/ul/li[2]")
            PIM = PimPage(self.driver)
            PIM.ClickPIM().click()
            self.verifyeditpresence("(//button[@type='button'])[6]")
            editbutton = PimPage(self.driver)
            editbutton.ClickEditButton().click()
            self.verifyNmaePresence("firstName")
            time.sleep(1)
            nickname = PimPage(self.driver)
            nickname.enterNickName().send_keys("MyNickNmae")
            time.sleep(1)
            otherID = PimPage(self.driver)
            otherID.enterOtherID().send_keys("12345")
            time.sleep(1)
            employeeID1 = PimPage(self.driver)
            employeeID1.enterEmployeeID1().send_keys("1")
            time.sleep(1)
            licence =PimPage(self.driver)
            licence.enterLicence().send_keys("TN19-20")
            time.sleep(2)
            gender = self.driver.find_element(By.XPATH, "//input[@value='2']")
            action = ActionChains(self.driver)
            action.click(on_element=gender)
            action.perform()
            try:
               # savebtn = self.driver.find_element(By.XPATH,"(//button[@type='submit'])[1]").click()
                editsave = PimPage(self.driver)
                editsave.ClickEditSave().click()
            except:
                savebtn = self.driver.find_element(By.XPATH, "(//button[@type='submit'])[1]")
                action = ActionChains(self.driver)
                action.click(on_element=savebtn)
                action.perform()
        except Exception as e:
            print(f"Caught exception: {type(e).__name__}: {e}")
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((By.ID, "//img[@alt='profile picture']/parent::div")))
            image = self.driver.find_element(By.XPATH, "//img[@alt='profile picture']/parent::div").click()
            action = ActionChains(self.driver)
            action.click(on_element=image)
            action.perform()
            time.sleep(3)
            Img = self.driver.find_element(By.XPATH, "//input[@class='oxd-file-input']")
            Img.send_keys('C:/Users/rahul.rk.REDIM.001/PycharmProjects/Guvi1/image2.jpg')
            time.sleep(3)
            try:
                savebtn = self.driver.find_element(By.XPATH, "(//button[@type='submit'])[1]").click()
            except:
                savebtn = self.driver.find_element(By.XPATH, "(//button[@type='submit'])[1]").click()
                action = ActionChains(self.driver)
                action.click(on_element=savebtn)
                action.perform()


    def test_TC_PIM_03(self):
        try:
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
            self.verythePresence2("//aside/nav/div[2]/ul/li[2]")
            PIM = PimPage(self.driver)
            PIM.ClickPIM().click()
            self.verifydeletePresence("(//button[@type='button'])[6]")
            delete = PimPage(self.driver)
            delete.ClickDelete().click()
            time.sleep(3)
            yes = PimPage(self.driver)
            yes.ClickYes().click()
        except Exception as e:
            print(f"Caught exception: {type(e).__name__}: {e}")
