from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        link.click()

    def should_be_product_in_basket(self):
        product_name_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET_LINK)
        name_in_basket = product_name_in_basket.text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_LINK)
        name = product_name.text
        assert name == name_in_basket, 'Product name is incorrect'

    def should_be_product_price(self):
        product_price_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET_LINK)
        price_in_basket = product_price_in_basket.text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_LINK)
        price = product_price.text
        assert price_in_basket == price, 'Price is incorrect'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET), \
           "Success message is presented, but should not be"

    def should_be_element_disappears(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET), \
           "The element is dissappears"

