import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    service_obj = Service("C:\\chromedriver.exe")
    driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(5)

    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.quit()