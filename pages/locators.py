from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REG_FORM = (By.ID, "register_form")
    LOGIN_EMAIL_INPUT = (By.NAME, "login-username")
    LOGIN_PASS_INPUT = (By.NAME, "login-password")
    SIGN_IN_BTN = (By.NAME, "login_submit")
    REG_EMAIL_INPUT = (By.NAME, "registration-email")
    REG_PASS_INPUT = (By.NAME, "registration-password1")
    REG_PASS_INPUT_REPEAT = (By.NAME, "registration-password2")

class ProductPageLocators():
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_NAME_IN_SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")
    CART_PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")



