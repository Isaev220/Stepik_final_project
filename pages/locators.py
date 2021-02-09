from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    EMAIL_REGISTRATION_LINK = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_REGISTRATION_LINK = (By.CSS_SELECTOR, "#id_registration-password1")
    REPASSWORD_REGISTRATION_LINK = (By.CSS_SELECTOR, "#id_registration-password2")
    EMAIL_LOGIN_LINK = (By.CSS_SELECTOR, "#id_login-username")
    PASSWORD_LOGIN_LINK = (By.CSS_SELECTOR, "#id_login-password")

class ProductPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PRODUCT_NAME_IN_BASKET_LINK = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_NAME_LINK = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    PRODUCT_PRICE_IN_BASKET_LINK = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRODUCT_PRICE_LINK = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
