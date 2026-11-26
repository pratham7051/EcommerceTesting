from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

def test_homepage():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.demoblaze.com/")

        WebDriverWait(driver, 10).until(
            lambda d: "STORE" in d.title
        )

        assert "STORE" in driver.title

        print("Homepage test PASSED")

    finally:
        driver.quit()