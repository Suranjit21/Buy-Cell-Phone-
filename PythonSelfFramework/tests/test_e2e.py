from PythonSelfFramework.pageObjects.homepage import Homepage
from PythonSelfFramework.utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("ourSetup")
class TestTwo(BaseClass):

   def tests_e2e(self):

       home = Homepage(self.driver)

       home.clickshopbutton().click()


       cards = home.cardscountlist()







       i = -1
       for card in cards:
           i = i + 1
           cardText = card.text


           if cardText == "Blackberry":

                home.addblackberry().click()




       checkoutpage = home.clickcheckout()
       confirmpage = checkoutpage.clickcheckoutbutton()

       confirmpage.searchbar().send_keys("ind")

       self.waitmethod("India")

       confirmpage.confirmcountry().click()

       confirmpage.agreecheckbox().click()

       confirmpage.purchase().click()


