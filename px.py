from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up ChromeDriver using webdriver-manager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open the DemoQA Automation Practice Form page
driver.get("https://demoqa.com/automation-practice-form")

# Maximize browser window
driver.maximize_window()
time.sleep(2)  # Wait for page to load

# Fill in the First Name and Last Name
driver.find_element(By.ID, "firstName").send_keys("John")
driver.find_element(By.ID, "lastName").send_keys("Doe")

# Fill in the Email
driver.find_element(By.ID, "userEmail").send_keys("johndoe@example.com")

# Select Gender (Male, Female, or Other)
gender = driver.find_element(By.XPATH, "//label[@for='gender-radio-1']")  # Select Male
driver.execute_script("arguments[0].click();", gender)  # Click using JavaScript

# Fill in the Mobile Number
driver.find_element(By.ID, "userNumber").send_keys("9876543210")

# Select Date of Birth
dob_field = driver.find_element(By.ID, "dateOfBirthInput")
dob_field.click()
time.sleep(1)
driver.find_element(By.XPATH, "//option[@value='10']").click()  # Select November
driver.find_element(By.XPATH, "//option[@value='1995']").click()  # Select Year 1995
driver.find_element(By.XPATH, "//div[@aria-label='Choose Monday, November 6th, 1995']").click()  # Select Day

# Fill in the Subject field
subject_field = driver.find_element(By.ID, "subjectsInput")
subject_field.send_keys("Maths")
subject_field.send_keys(Keys.RETURN)  # Press Enter to select

# Select Hobbies (Sports, Reading, Music)
hobby = driver.find_element(By.XPATH, "//label[@for='hobbies-checkbox-1']")  # Select Sports
driver.execute_script("arguments[0].click();", hobby)  # Click using JavaScript

# Fill in the Address
driver.find_element(By.ID, "currentAddress").send_keys("123 Main Street, New York")

# Click the Submit button
submit_button = driver.find_element(By.ID, "submit")
driver.execute_script("arguments[0].click();", submit_button)  # Click using JavaScript

time.sleep(3)  # Wait for results to appear

# Take a Screenshot (Optional)
driver.save_screenshot("form_submission.png")

# Close the browser
driver.quit()
