import pytest
import self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("ourSetup")
class BaseClass:

   def waitmethod(self, text):
      WebDriverWait(self.driver, 10).until(
      expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

