from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()


    def alert_handler():
        wait = WebDriverWait(browser, 10, poll_frequency=1)
        alert = wait.until(EC.alert_is_present())
        browser.switch_to.alert
        alert_text = alert.text
        print(alert_text)
        alert.accept()
    browser.get("http://suninjuly.github.io/registration2.html")
    element1 = browser.find_element('xpath', '//input[@placeholder = "Input your first name"]').send_keys('first_name')
    element1 = browser.find_element('xpath', '//input[@placeholder = "Input your last name"]').send_keys('last_name')
    element1 = browser.find_element('xpath', '//input[@placeholder = "Input your email"]').send_keys('email')
    element1 = browser.find_element('xpath', '//input[@placeholder = "Input your phone:"]').send_keys('45698231')
    element1 = browser.find_element('xpath', '//input[@placeholder = "Input your address:"]').send_keys('address')
    button = browser.find_element('xpath', '//button[text() = "Submit"]')
    button.click()
    alert_handler()
finally:
    browser.quit()
