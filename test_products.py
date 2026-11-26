from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_products():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.demoblaze.com/")

        wait = WebDriverWait(driver, 15)

        products = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".card")
            )
        )

        assert len(products) > 0

        print("Product listing test PASSED")
        print("Total products displayed:", len(products))

    finally:
        driver.quit()