import pytest
from selenium import webdriver








def pytest_addoption(parser):
   parser.addoption(
      "--browser_name", action="store", default="chrome", help="this is just friendly desc."
   )

@pytest.fixture(scope = "class")
def ourSetup(request):
   browser_name = request.config.getoption("browser_name")

   if browser_name == "chrome":

      driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
      # driver.get("https://rahulshettyacademy.com/angularpractice/")
      # driver.maximize_window()

   elif browser_name == "microsoft edge":
      print("hi")
   elif browser_name == "firefox":
      print("hello")


   driver.get("https://rahulshettyacademy.com/angularpractice/")
   driver.maximize_window()

   # driver.get("https://rahulshettyacademy.com/angularpractice/")
   #




   request.cls.driver = driver
   yield
   # driver.close()





   # microdoft invocation code

