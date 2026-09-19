
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

import os
import time
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def run_scr(digits):
    load_dotenv()
    email_text = os.getenv("EMAIL")
    password_text = os.getenv("PASSWORD")
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(options=chrome_options)
    print("hello")
    driver.get("https://www.disneyplus.com/begin")
    title = driver.title
    print(title)
    try:
        otp_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='otp']"))
        )
        otp_field.send_keys(digits)
    	buttons = driver.find_element(By.CSS_SELECTOR, "[data-testid='continue-btn']")
    	buttons.click()
    except Exception as error_msg:
        print(f"Failed to find element due to: {error_msg}")

        screenshot_path = "/home/ubuntu/rest/"
        driver.save_screenshot(f"{screenshot_path}/stage1")
        print(f"Saved a screenshot of what the server sees to: {screenshot_path}")
    finally:
        pass

    #button = driver.find_element(By.CSS_SELECTOR, "input[name='otp']")
    try:
        email =WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='email']"))
        )
        email.send_keys(email_text)

    finally:
        pass
    try:
        email_sbt = WebDriverWait(driver,10).until(
            EC.element_to_be_clickable(By.CSS_SELECTOR, "[data-testid='continue-btn']")
        )
        email_sbt.click()
    finally:
        pass
    try:
        password = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((BY.CSS_SELECTOR, "[data-testid='passwordless-login-with-pwd-btn']")))
        password.click()
    try:
        password_entry = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((BY.CSS_SELECTOR, "input[name='password']")))
        password_entry.send_keys(password_text)
    finally:
        pass
    try:
        password_buttons = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((BY.XPATH, "//button[contains(., 'Log In')]")))
        password_buttons.click()
    finally:
        pass
    flag = True
    if flag is True:
        time.sleep(10)
        driver.quit()
        return ("completed")

digits_val="87991824"
run_scr(digits_val)
