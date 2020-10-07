from selenium.webdriver.common.by import By

from PythonSelfFramework.pageObjects.confirmpage import Confirmpage


class Checkout:
        checkout = (By.XPATH, "//button[@class='btn btn-success']")

        def __init__(self,driver):
            self.driver = driver

        def clickcheckoutbutton(self):
            self.driver.find_element(*Checkout.checkout).click()
            # self.driver.find_element(*Checkout.checkoutbutton).click()
            confirmpage = Confirmpage(self.driver)
            return confirmpage


