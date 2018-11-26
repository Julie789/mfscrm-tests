import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class admin_login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "user1"
        pwd = "admin1234"
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


        # xpath, clicks on product button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[3]/div/div/p[2]/a").click()
        time.sleep(2)

        # xpath, clicks on delete product button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/table/tbody/tr[4]/td[8]/a").click()
        time.sleep(2)

        driver.switch_to.alert.accept()
        time.sleep(5)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

