from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
from .locators import BasePageLocators
from .locators import BaseCap
from .login_page import LoginPage
from .product_page import Product_Page
from .base_page import BasePage
import time
import pytest



class BasketPage(BasePage):
    def transition_in_cap(self):
        cap = self.browser.find_element(*BaseCap.BASKET_LINK)
        cap.click(), "Не нажалась кнопка перехода в корзину"

    def not_product_in_cap(self):
        assert self.is_not_element_present(*BaseCap.PRODUCT_BLOCK), "Есть блок с товарами в пустой корзине"

#данная проверка так реализваона из за комментария преподавателя, что достаточно проверки на английском
    def text_not_product_empty(self):
        a = (self.browser.find_element(*BaseCap.TEXT_CAP_EMPTY)).text
        assert "Your basket is empty" in a, "Нет текста 'Your basket is empty' в пустой корзине"



