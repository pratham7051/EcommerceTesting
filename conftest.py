import pytest
import os
from datetime import datetime
from selenium import webdriver


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()

    yield browser

    browser.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        browser = item.funcargs.get("driver")

        if browser:
            os.makedirs("screenshots", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshots/{item.name}_{timestamp}.png"

            browser.save_screenshot(filename)

            print(f"\nFailure screenshot saved: {filename}")