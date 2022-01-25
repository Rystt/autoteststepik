from .base_page import BasePage
from .locators import ProductPageLocators
import time

class Product_Page(BasePage):
    def add_product(self):
        product_add = self.browser.find_element(*ProductPageLocators.INPUT_ADD_TO_SHOPPING_CART)
        product_add.click()
    #
    def checking_for_message_product(self):
        a = (self.browser.find_element(*ProductPageLocators.INPUT_PRODUCT)).text
        b = (self.browser.find_element(*ProductPageLocators.MASSEGE_OF_PRODUCT)).text
        assert a == b, "сообщение о добавлении товара о добавлении товара неправльное или его нет"

    def checing_for_massege_price(self):
        a = (self.browser.find_element(*ProductPageLocators.PRICE)).text
        b = (self.browser.find_element(*ProductPageLocators.MASSAGE_OF_PRICE)).text
        assert a == b, "стоимость корзины не совпадает с ценой товара"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MASSEGE_OF_PRODUCT), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.MASSEGE_OF_PRODUCT), \
             "Success message is presented, but should not be"


