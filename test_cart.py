from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime


def test_add_to_cart():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://www.demoblaze.com/")

        wait = WebDriverWait(driver, 15)

        wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Samsung galaxy s6")
            )
        ).click()

        wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Add to cart")
            )
        ).click()

        alert = wait.until(EC.alert_is_present())
        alert.accept()

        driver.find_element(By.ID, "cartur").click()

        wait.until(
            EC.text_to_be_present_in_element(
                (By.ID, "tbodyid"), "Samsung galaxy s6"
            )
        )

        assert "Samsung galaxy s6" in driver.find_element(
            By.ID, "tbodyid"
        ).text
       #raise Exception("Testing screenshot feature")

    except Exception:
        os.makedirs("screenshots", exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        path = f"screenshots/test_cart_failure_{timestamp}.png"

        driver.save_screenshot(path)
        print(f"Failure screenshot saved: {path}")

        raise

    finally:
        driver.quit()