from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Setup
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Create screenshots folder if not exists
if not os.path.exists("../screenshots"):
    os.makedirs("../screenshots")

try:
    # Open the registration page
    driver.get("file:///Users/jayvardhansinghnegi/Desktop/intelligent-registration-system/frontend/index.html")

    print("Page URL:", driver.current_url)
    print("Page Title:", driver.title)

    # -------- NEGATIVE SCENARIO --------
    driver.find_element(By.ID, "firstName").send_keys("Jay")
    driver.find_element(By.ID, "email").send_keys("jay@test.com")
    driver.find_element(By.ID, "phone").send_keys("9876543210")
    driver.find_elements(By.NAME, "gender")[0].click()

    driver.find_element(By.ID, "submitBtn").click()
    time.sleep(2)

    driver.save_screenshot("../screenshots/error-state.png")

    # -------- POSITIVE SCENARIO --------
    driver.find_element(By.ID, "lastName").send_keys("Negi")

    driver.find_element(By.ID, "country").send_keys("India")
    time.sleep(1)
    driver.find_element(By.ID, "state").send_keys("Uttarakhand")
    time.sleep(1)
    driver.find_element(By.ID, "city").send_keys("Haldwani")

    driver.find_element(By.ID, "password").send_keys("Test@123")
    driver.find_element(By.ID, "confirmPassword").send_keys("Test@123")

    driver.find_element(By.ID, "terms").click()
    time.sleep(1)

    driver.find_element(By.ID, "submitBtn").click()
    time.sleep(2)

    driver.save_screenshot("../screenshots/success-state.png")

    print("Automation executed successfully")

except Exception as e:
    print("Error occurred:", e)

finally:
    time.sleep(2)
    driver.quit()
