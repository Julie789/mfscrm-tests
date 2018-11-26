import unittest
import time
import xlrd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ReadExcel(unittest.TestCase):

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

        #Login to admin and add customers
       driver.get("http://127.0.0.1:8000/admin")

       workbook = xlrd.open_workbook("Sample_Data.xlsx")
       sheet = workbook.sheet_by_name("Customers")
       rowcnt = sheet.nrows
       #colcnt = sheet.ncols

       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[1]/a").click()
       time.sleep(2)

       for row in range(1, rowcnt):
           elem = driver.find_element_by_id("id_cust_name")
           elem.send_keys(sheet.cell_value(row, 0))
           elem = driver.find_element_by_id("id_organization")
           elem.send_keys(sheet.cell_value(row, 1))
           time.sleep(2)
           elem = driver.find_element_by_id("id_role")
           elem.send_keys(sheet.cell_value(row, 2))
           elem = driver.find_element_by_id("id_email")
           elem.send_keys(sheet.cell_value(row, 3))
           time.sleep(2)
           elem = driver.find_element_by_id("id_bldgroom")
           elem.send_keys(sheet.cell_value(row, 4))
           elem = driver.find_element_by_id("id_address")
           elem.send_keys(sheet.cell_value(row, 5))
           time.sleep(2)
           elem = driver.find_element_by_id("id_account_number")
           elem.send_keys(int(sheet.cell_value(row, 6)))
           elem = driver.find_element_by_id("id_city")
           elem.send_keys(sheet.cell_value(row, 7))
           time.sleep(2)
           elem = driver.find_element_by_id("id_state")
           elem.send_keys(sheet.cell_value(row, 8))
           elem = driver.find_element_by_id("id_zipcode")
           elem.send_keys(str(sheet.cell_value(row, 9)).rstrip('0').rstrip('.'))
           time.sleep(2)
           elem = driver.find_element_by_id("id_phone_number")
           elem.send_keys(str(sheet.cell_value(row, 10)))
           time.sleep(1)

           if row < rowcnt-1:
               elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[2]").click()
               time.sleep(2)
           else:
               elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
               time.sleep(5)

   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()
