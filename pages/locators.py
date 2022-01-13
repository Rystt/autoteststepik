from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.ID, "registration_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    # LOGIN_EMAIL = (By.ID, "id_registration-email")
    # LOGIN_PASS_REG1 = (By.ID, "id_registration-password1")
    # LOGIN_PASS_REG2 = (By.ID, "id_registration-password2")



