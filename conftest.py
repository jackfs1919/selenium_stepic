import pytest
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait

@pytest.fixture(scope="function")
def browser():
    pref = {
        "download.default_directory": os.getcwd()
    }
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ash-no-nudges")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/115.0.0.0 Safari/537.36")
    options.add_argument('--disable-infobars')
    options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--ignore-certificate-errors")
    options.add_experimental_option("prefs", pref)
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    # browser.execute_script("window.stop();")
    yield browser
    print("\nquit browser..")
    browser.quit()