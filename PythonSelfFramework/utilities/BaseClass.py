import inspect


import pytest
import self
from selenium import webdriver
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("ourSetup")

class BaseClass:

   def waitmethod(self, text):
      WebDriverWait(self.driver, 10).until(
      expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))

   def getLogger(self):
      loggerName = inspect.stack()[1][3]
      logger = logging.getLogger(loggerName)
      fileHandler = logging.FileHandler('logfile.log')

      formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

      fileHandler.setFormatter(formatter)

      logger.addHandler(fileHandler)

      logger.setLevel(logging.INFO)

      return logger


   # logging hierchy
   # logger.debug(“a debug statement is executed”)
   #
   # logger.info(“Information statement”)
   #
   # logger.warning(“Something is in warning mode”)
   #
   # logger.error(“A major error has happened”)
   #
   # logger.critical(“Critical issues)
