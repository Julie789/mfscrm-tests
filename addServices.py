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


        # xpath, clicks on services button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[2]/div/div/div/div/div[2]/div/div/p[2]/a").click()
        time.sleep(2)

        # xpath, clicks on add service button
        elem = driver.find_element_by_xpath("/html/body/div/div/div/div[3]/div/a/span").click()
        time.sleep(2)

        #Add service details
        elem = driver.find_element_by_id("id_cust_name")
        elem.send_keys("Susan Mendiola")
        elem = driver.find_element_by_id("id_service_category")
        elem.send_keys("Food Prep/Delivery")
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("Lunch and Breverages : 100 guests ")

        elem = driver.find_element_by_id("id_location")
        elem.send_keys("PKI Room 158")
        elem = driver.find_element_by_id("id_setup_time")
        elem.clear()
        elem.send_keys("2018-12-25 12:00:00")
        elem = driver.find_element_by_id("id_cleanup_time")
        elem.clear()
        elem.send_keys("2018-12-25 17:00:00")
        elem = driver.find_element_by_id("id_service_charge")
        elem.send_keys("500")
        time.sleep(1)



        #xpath, clicks on save button for add service
        elem = driver.find_element_by_xpath("/html/body/div/div/div/form/button").click()
        time.sleep(5)



    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

