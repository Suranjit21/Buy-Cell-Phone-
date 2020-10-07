
from selenium.webdriver.common.by import By


class Confirmpage:
    search = (By.ID, "country")
    clickcountry = (By.LINK_TEXT, "India")
    agreebox = (By.XPATH, "//div[@class='checkbox checkbox-primary']")
    confirmpurchase = (By.CSS_SELECTOR, "[type='submit']")

    def __init__(self, driver):
        self.driver = driver

    def searchbar(self):
        return self.driver.find_element(*Confirmpage.search)
    def confirmcountry(self):
        return self.driver.find_element(*Confirmpage.clickcountry)
    def agreecheckbox(self):
        return self.driver.find_element(*Confirmpage.agreebox)
    def purchase(self):
        return self.driver.find_element(*Confirmpage.confirmpurchase)


