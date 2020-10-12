from PythonSelfFramework.pageObjects.homepage import Homepage
from PythonSelfFramework.utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("ourSetup")
class TestTwo(BaseClass):

   def tests_e2e(self):
       log = self.getLogger()

       home = Homepage(self.driver)

       home.clickshopbutton().click()


       cards = home.cardscountlist()


       log.info("here, we are getting all the card titles")
       # self.log.info(cardText)
       # log.info("getting all the card titles")
       # log.info("Entering country name")
       # log.info("Entering country name")

       i = -1
       for card in cards:
           i = i + 1
           cardText = card.text
           log.info(cardText)


           if cardText == "Blackberry":
            log.info("Confirming phone type")

            home.addblackberry().click()




       checkoutpage = home.clickcheckout()
       confirmpage = checkoutpage.clickcheckoutbutton()

       confirmpage.searchbar().send_keys("ind")
       log.info("Picking country")


       self.waitmethod("India")



       confirmpage.confirmcountry().click()

       confirmpage.agreecheckbox().click()

       confirmpage.purchase().click()




