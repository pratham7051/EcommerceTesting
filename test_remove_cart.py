from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_remove_cart():
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
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#tbodyid tr")
            )
        )

        delete = wait.until(
            EC.element_to_be_clickable(
                (By.LINK_TEXT, "Delete")
            )
        )
        delete.click()

        wait.until(
            lambda d: len(d.find_elements(
                By.CSS_SELECTOR, "#tbodyid tr"
            )) == 0
        )

        print("Remove cart test PASSED")

    finally:
        driver.quit()