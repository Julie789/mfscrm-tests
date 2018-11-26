import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class login_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_blog(self):
       user = "user1"
       pwd = "admin1234"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/")

       elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
       time.sleep(2)
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       #driver.get("http://127.0.0.1:8000")
       assert "Logged In"
       time.sleep(2)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
