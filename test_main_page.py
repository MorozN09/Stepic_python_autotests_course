from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)