import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://www.facebook.com")

time.sleep(2)

email_field = driver.find_element(By.ID, "email")
password_field = driver.find_element(By.ID, "pass")

email_field.send_keys("sarshaartr@gmail.com")  
password_field.send_keys("12345")        

password_field.send_keys(Keys.RETURN)


time.sleep(5)


print("Successful attempt:", driver.title)


driver.quit()
