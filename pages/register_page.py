from selenium.webdriver.common.by import By
from base_page import BasePage


class registerPage(BasePage):
    EMAIL_FIELD=(By.ID, "reg_email")
    PASSWORD_FIELD=(By.ID, "reg_password")
    register_BUTTON=(By.XPATH, "//*[@id='customer_login']/div[2]/form/p[3]/button")
    error_message_locater=(By.CLASS_NAME, 'woocommerce-error')
    username_locater=(By.XPATH, "/html/body/div/div[2]/div/div[2]/main/article/div/div/div/p[1]/strong[1]")
    def enter_email(self,email):
         self.input_text(self.EMAIL_FIELD,email)
    def enter_password(self,password):
        self.input_text(self.PASSWORD_FIELD,password)
    def click_register_button(self):
        self.click(self.register_BUTTON)

    def get_the_text_error_message(self):
       element= self.find_locater_error_message(self.error_message_locater)
       return element.text
    def get_the_username_locater(self):
        element = self.find_the_locater(self.username_locater)
        element= element.text
        return element
    def get_email(self):
        email=self.find_the_locater(self.EMAIL_FIELD)
        email=email.get_attribute('value')
        return email