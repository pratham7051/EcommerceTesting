from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_invalid_login():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://www.demoblaze.com/")

        wait = WebDriverWait(driver, 15)

        wait.until(
            EC.element_to_be_clickable((By.ID, "login2"))
        ).click()

        username = wait.until(
            EC.visibility_of_element_located((By.ID, "loginusername"))
        )

        password = driver.find_element(By.ID, "loginpassword")

        username.send_keys("wrong_user_123")
        password.send_keys("wrong_password_123")

        driver.find_element(
            By.XPATH, "//button[text()='Log in']"
        ).click()

        alert = wait.until(EC.alert_is_present())

        alert_text = alert.text
        print("\nActual error displayed:", alert_text)

        assert (
            "Wrong password" in alert_text
            or "User does not exist" in alert_text
        )

        print("\nShowing error alert for 5 seconds...")
        time.sleep(5)

        alert.accept()

    finally:
        driver.quit()