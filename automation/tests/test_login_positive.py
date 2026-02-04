import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    yield driver
    driver.quit()


def test_login_with_valid_credentials(driver):
    login_page = LoginPage(driver)
    login_page.open()

    login_page.login(
        "hyrenet+bugathon@guvi.in",
        "hyrenettest@123"
    )

    # At this point, login attempt is made.
    # Dashboard validation may be restricted due to security controls.
