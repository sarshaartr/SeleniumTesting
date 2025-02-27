from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.get("https://demoqa.com/automation-practice-form")


driver.maximize_window()
time.sleep(2)  

driver.find_element(By.ID, "firstName").send_keys("Sarshaar")
driver.find_element(By.ID, "lastName").send_keys("Moazzam")
driver.find_element(By.ID, "userEmail").send_keys("sarshaartr@gmail.com")

gender = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")
driver.execute_script("arguments[0].click();", gender)  


driver.find_element(By.ID, "userNumber").send_keys("3472520863")


dob_field = driver.find_element(By.ID, "dateOfBirthInput")
dob_field.click()
time.sleep(1)
driver.find_element(By.XPATH, "//select[@class='react-datepicker__month-select']/option[text()='June']").click() 
driver.find_element(By.XPATH, "//select[@class='react-datepicker__year-select']/option[text()='2000']").click() 

date_27 = driver.find_element(By.XPATH, "//div[@aria-label='Choose Tuesday, June 27th, 2000']")
date_27.click()  


subject_field = driver.find_element(By.ID, "subjectsInput")
subject_field.send_keys("Maths")
subject_field.send_keys(Keys.RETURN) 


hobby = driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']") 
driver.execute_script("arguments[0].click();", hobby)  


driver.find_element(By.ID, "currentAddress").send_keys("Johar")


submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].click();", submit_button)  

time.sleep(3)  


driver.save_screenshot("form_submission.png")


driver.quit()
