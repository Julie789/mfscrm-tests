import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class admin_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "SelUser"
        pwd = "admin123"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/")
        time.sleep(1)

        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        time.sleep(1)
        assert "Logged In"
        time.sleep(2)

        # xpath, clicks on Dropdown menu
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/a").click()
        # xpath, clicks on Change Password
        elem = driver.find_element_by_xpath("/html/body/nav/div/div[2]/ul[2]/li/ul/li[2]/a").click()
        time.sleep(2)

        # fill the change password form
        elem = driver.find_element_by_id("id_old_password")
        elem.send_keys("admin123")
        elem = driver.find_element_by_id("id_new_password1")
        elem.send_keys("pass1234")
        elem = driver.find_element_by_id("id_new_password2")
        elem.send_keys("pass1234")
        time.sleep(2)

        # find element by xpath, click on change password
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/p[5]/input").click()
        time.sleep(5)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

