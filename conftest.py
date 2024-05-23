import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="es",
                     help="Choose language")
@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--ash-no-nudges")
    options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/115.0.0.0 Safari/537.36")
    options.add_argument('--disable-infobars')
    #options.add_argument("--headless")
    options.add_argument("--incognito")
    options.add_argument("--ignore-certificate-errors")
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()