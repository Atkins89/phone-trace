from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def find_my_device(email, password):
    # Configure Chrome options for headless mode (running without a GUI)
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Path to the ChromeDriver binary in Replit (assume it is in the same directory as main.py)
    service = Service(executable_path='./chromedriver')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Open the Google login page
        driver.get("https://accounts.google.com/signin")

        # Enter the email
        email_input = driver.find_element(By.ID, "identifierId")
        email_input.send_keys(email)
        email_input.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for the next page to load

        # Enter the password
        password_input = driver.find_element(By.NAME, "password")
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        time.sleep(2)  # Wait for the login process to complete

        # Navigate to Find My Device
        driver.get("https://www.google.com/android/find")
        time.sleep(10)  # Allow some time for the page to load

        # At this point, the Find My Device interface should be loaded

    finally:
        # Close the browser after done
        driver.quit()

# Usage
email = "saiatkins8@gmail.com"
password = "2006ally=my"
find_my_device(email, password)
