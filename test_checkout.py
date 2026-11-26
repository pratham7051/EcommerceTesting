from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_checkout():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)

    try:
        driver.get("https://www.demoblaze.com/")

        product = wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Samsung galaxy s6")
            )
        )
        product.click()

        add = wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Add to cart")
            )
        )
        add.click()

        alert = wait.until(EC.alert_is_present())
        alert.accept()

        driver.find_element(By.ID, "cartur").click()

        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "#tbodyid tr")
            )
        )

        driver.find_element(By.XPATH, "//button[text()='Place Order']").click()

        wait.until(
            EC.visibility_of_element_located(
                (By.ID, "orderModal")
            )
        )

        driver.find_element(By.ID, "name").send_keys("Pratham")
        driver.find_element(By.ID, "country").send_keys("India")
        driver.find_element(By.ID, "city").send_keys("Chandigarh")
        driver.find_element(By.ID, "card").send_keys("1234567890123456")
        driver.find_element(By.ID, "month").send_keys("November")
        driver.find_element(By.ID, "year").send_keys("2026")

        driver.find_element(
            By.XPATH, "//button[text()='Purchase']"
        ).click()

        confirmation = wait.until(
            EC.visibility_of_element_located(
                (By.CLASS_NAME, "sweet-alert")
            )
        )

        assert "Thank you for your purchase!" in confirmation.text

        print("Checkout test PASSED")

    finally:
        driver.quit()