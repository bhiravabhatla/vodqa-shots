from selenium import webdriver
from pyvirtualdisplay import Display
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.keys import Keys

display = Display(visible=0, size=(800, 600))
display.start()

driver = webdriver.Firefox()
driver.get("http://spree:3000/login")

email = driver.find_element_by_id("spree_user_email")
password = driver.find_element_by_id("spree_user_password")

email.clear()
password.clear()
email.send_keys("spree@example.com")
password.send_keys("spree123")
password.send_keys(Keys.RETURN)

WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "info"))
    )
products = driver.find_elements_by_class_name("info")
print(f"No.of Products in first page is {products.__len__()} \n")
product_names = [ prod.get_attribute("title")  for prod in products ]
print(" List of Products in the first page : \n ################################### \n")
print("\n".join(product_names))