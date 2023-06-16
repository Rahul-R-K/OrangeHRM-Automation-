from selenium.webdriver.common.by import By

#PIM = self.driver.find_element(By.XPATH, "//aside/nav/div[2]/ul/li[2]")
# adduserbutton = self.driver.find_element(By.XPATH,"(//button[@type='button'])[contains(.,'Add')]")
# FirstName = self.driver.find_element(By.XPATH,"//input[@placeholder='First Name']")
# MiddleName = self.driver.find_element(By.XPATH, "//input[@placeholder='Middle Name']")
# LastName = self.driver.find_element(By.XPATH, "//input[@placeholder='Last Name']")
# EmployeeId = self.driver.find_element(By.XPATH,"//label[contains(.,'Employee Id')]/following::input[1]")
# username = self.driver.find_element(By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]")
# password = self.driver.find_element(By.XPATH,"(//div/input)[8]")
# conformpassword = self.driver.find_element(By.XPATH,"(//div/input)[9]")
# Savebtn = self.driver.find_element(By.XPATH,"//button[contains(.,'Save')]").click()
# editbutton = self.driver.find_element(By.XPATH, "(//button[@type='button'])[6]")
# NickName = self.driver.find_element(By.XPATH,"(//label[normalize-space()='Nickname'])/following::input[1]")
# OtherId = self.driver.find_element(By.XPATH, "(//label[normalize-space()='Other Id'])[1]/following::input[1]")
# employeeId = self.driver.find_element(By.XPATH,"//label[contains(.,'Employee Id')]/following::input[1]")
# licensee = self.driver.find_element(By.XPATH,"(//input)[8]")
#savebtn = self.driver.find_element(By.XPATH, "(//button[@type='submit'])[1]").click()
# deletebtn = self.driver.find_element(By.XPATH,"(//button[@type='button'])[5]")
# yes = self.driver.find_element(By.XPATH,"(//button[@type='button'])[112]")


class PimPage:

    def __init__(self,driver):
        self.driver = driver


    Pim = (By.XPATH, "//aside/nav/div[2]/ul/li[2]")
    Addbutton = (By.XPATH,"(//button[@type='button'])[contains(.,'Add')]")
    FirstName = (By.XPATH,"//input[@placeholder='First Name']")
    MiddleName = (By.XPATH, "//input[@placeholder='Middle Name']")
    LastName = (By.XPATH, "//input[@placeholder='Last Name']")
    EmployeeID = (By.XPATH,"//label[contains(.,'Employee Id')]/following::input[1]")
    UserName = (By.XPATH,"(//input[@class='oxd-input oxd-input--active'])[3]")
    Password = (By.XPATH,"(//div/input)[8]")
    ConformPassword = (By.XPATH,"(//label[normalize-space()='Confirm Password'])/following::input[1]")
    SaveButton = (By.XPATH,"//button[contains(.,'Save')]")
    EditButton = (By.XPATH, "(//button[@type='button'])[6]")
    NickName = (By.XPATH,"(//label[normalize-space()='Nickname'])/following::input[1]")
    OtherID = (By.XPATH, "(//label[normalize-space()='Other Id'])[1]/following::input[1]")
    EmployeeID1 = (By.XPATH,"//label[contains(.,'Employee Id')]/following::input[1]")
    Licence = (By.XPATH,"(//input)[8]")
    EditSave = (By.XPATH, "(//button[@type='submit'])[1]")
    Delete = (By.XPATH,"(//button[@type='button'])[5]")
    Yes = (By.XPATH,"//div[@role='document']//div//button[2]")
    def ClickPIM(self):
        return self.driver.find_element(*PimPage.Pim)

    def ClickAdd(self):
        return self.driver.find_element(*PimPage.Addbutton)

    def enterFirstName(self):
        return self.driver.find_element(*PimPage.FirstName)
    def enterMiddleName(self):
        return self.driver.find_element(*PimPage.MiddleName)
    def enterLastName(self):
        return self.driver.find_element(*PimPage.LastName)
    def enterEmployeeID(self):
        return self.driver.find_element(*PimPage.EmployeeID)
    def enterUserNmae(self):
        return self.driver.find_element(*PimPage.UserName)
    def enterPassword(self):
        return self.driver.find_element(*PimPage.Password)
    def enterConformPassword(self):
        return  self.driver.find_element(*PimPage.ConformPassword)
    def ClickSaveButton(self):
        return self.driver.find_element(*PimPage.SaveButton)
    def ClickEditButton(self):
        return self.driver.find_element(*PimPage.EditButton)
    def enterNickName(self):
        return self.driver.find_element(*PimPage.NickName)
    def enterOtherID(self):
        return self.driver.find_element(*PimPage.OtherID)
    def enterEmployeeID1(self):
        return self.driver.find_element(*PimPage.EmployeeID1)
    def enterLicence(self):
        return self.driver.find_element(*PimPage.Licence)
    def ClickEditSave(self):
        return self.driver.find_element(*PimPage.EditSave)
    def ClickDelete(self):
        return self.driver.find_element(*PimPage.Delete)
    def ClickYes(self):
        return self.driver.find_element(*PimPage.Yes)

