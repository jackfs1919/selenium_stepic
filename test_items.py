import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
def test_guest_should_see_btn_add_to_buscket(browser):
    browser.get(link)
    btn = ('xpath', '//button[contains(@class, "btn-add-to-basket")]')
    button = len(browser.find_elements(*btn))
    assert button > 0, '!!!НЕ НАШЕЛ!!!'

