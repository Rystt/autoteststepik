from selenium.webdriver.common.by import By



# class MainPageLocators():
#     LOGIN_LINK = (By.ID, "registration_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_ADRESS_FIELD = (By.ID, "id_registration-email")
    PASSWORD_FIELD = (By.ID, "id_registration-password1")
    CONFIRM_PASSWORD_FIELD = (By.ID, "id_registration-password2")
    REGISTRATION_SUBMIT = (By.NAME, "registration_submit")


class ProductPageLocators():
    INPUT_ADD_TO_SHOPPING_CART = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    INPUT_PRODUCT = (By.XPATH, "//li[@class='active']")
    MASSEGE_OF_PRODUCT = (By.XPATH, "//div[@id='messages']/div[1]/div/strong")
    PRICE = (By.XPATH, "//p[@class='price_color']")
    MASSAGE_OF_PRICE = (By.XPATH, "//div[@id='messages']/div[3]/p/strong")



class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BaseCap():
    BASKET_LINK = (By.XPATH, "//span[@class='btn-group']/a")
    PRODUCT_BLOCK = (By.CLASS_NAME, "basket-items")
    TEXT_CAP_EMPTY = (By.XPATH, "//div[@id='content_inner']")