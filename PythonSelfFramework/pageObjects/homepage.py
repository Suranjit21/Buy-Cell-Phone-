
from selenium.webdriver.common.by import By

from PythonSelfFramework.pageObjects.checkoutpage import Checkout


class Homepage:
    # self.driver.find_element_by_css_selector("a[href*='shop']").click()

    shopbutton = (By.CSS_SELECTOR, "a[href*='shop']")
    cardslist = (By.CSS_SELECTOR, ".card-title a")
    blackberry = (By.XPATH, "//app-card-list [@class='row']/app-card[4]/div/div[2]/button")
    # self.driver.find_element_by_xpath("//app-card-list [@class='row']/app-card[4]/div/div[2]/button").click()
    # self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
    checkoutbutton = (By.CSS_SELECTOR, "a[class*='btn-primary']")


    def __init__(self, driver):
        self.driver = driver

    def clickshopbutton(self):
        return self.driver.find_element(*Homepage.shopbutton)

    def cardscountlist(self):
        return self.driver.find_elements(*Homepage.cardslist)

    def addblackberry(self):
        return self.driver.find_element(*Homepage.blackberry)

    def clickcheckout(self):
        self.driver.find_element(*Homepage.checkoutbutton).click()
        checkoutpage = Checkout(self.driver)
        return checkoutpage



    # def blackberry

