from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import os

SCREENSHOT_DIR = "automation/screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

chrome_options = Options()
chrome_options.add_argument("--headless=new")          
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

chrome_options.binary_location = "/usr/bin/chromium"
service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # ------------------ OPEN PAGE ------------------

    driver.get("file:///app/frontend/index.html")

    print("Page URL:", driver.current_url)
    print("Page Title:", driver.title)

    time.sleep(2)

    # ------------------ NEGATIVE SCENARIO ------------------

    driver.find_element(By.ID, "firstName").send_keys("Jay")
    driver.find_element(By.ID, "email").send_keys("jay@test.com")
    driver.find_element(By.ID, "phone").send_keys("9876543210")
    driver.find_elements(By.NAME, "gender")[0].click()

    driver.find_element(By.ID, "submitBtn").click()
    time.sleep(2)

    driver.save_screenshot(f"{SCREENSHOT_DIR}/error-state.png")

    # ------------------ POSITIVE SCENARIO ------------------

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

    driver.save_screenshot(f"{SCREENSHOT_DIR}/success-state.png")

    print("Automation executed successfully")

except Exception as e:
    print("Error occurred:", e)
    driver.save_screenshot(f"{SCREENSHOT_DIR}/failure.png")

finally:
    driver.quit()
