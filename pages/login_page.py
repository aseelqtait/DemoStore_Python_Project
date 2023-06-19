from base_page import BasePage
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    Email_FIELD=(By.ID,"username")
    PASSWORD_FIELD=(By.ID,"password")
    CLICK_BUTTON=(By.NAME,"login")
    error_message_locater=(By.CLASS_NAME,"woocommerce-error")
    def enter_email(self,text):
        self.input_text(self.Email_FIELD,text)
    def enter_password(self,text):
        self.input_text(self.PASSWORD_FIELD,text)
    def click_login_button(self):
        self.click(self.CLICK_BUTTON)
    def get_the_text_error_message(self):
        message=self.find_locater_error_message(self.error_message_locater)
        return message.text

