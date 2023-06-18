#all file in tests directory can show this file => because in the same package
import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Create and configure the driver object
    driver = webdriver.Chrome()
    yield driver
    # Teardown - quit the driver after the test finishes
    driver.quit()
@pytest.fixture(scope="function", autouse=True)
def open_url(driver):
    driver.get("http://demostore.supersqa.com/my-account/")
