from selenium.common import NoSuchElementException

from pages.register_page import LoginPage
# def test_successful_login(driver):
#     login_page=LoginPage(driver)
#     login_page.enter_email("w@gmail.com")
#     login_page.enter_password("gftrebch")
#     login_page.click_login_button()


def test_failed_email(driver):
        try:
            login_page = LoginPage(driver)
            login_page.enter_email("qq@aseel")
            login_page.enter_password("aseelQ@@1359")
            login_page.click_login_button()
            assert "Please provide a valid email address." in login_page.get_the_text_error_message()
        except NoSuchElementException:
            return False
def test_existing_email(driver):
    login_page = LoginPage(driver)
    login_page.enter_email("aseelqtait@gmail.com")
    login_page.enter_password("aseelqtait1359")
    login_page.click_login_button()
    assert "An account is already registered with your email address. Please log in." in login_page.get_the_text_error_message()


def test_empty(driver):
    login_page = LoginPage(driver)
    login_page.enter_email("")
    login_page.enter_password("")
    login_page.click_login_button()
    assert "Please provide a valid email address" in login_page.get_the_text_error_message()


def test_weak_password(driver):
    login_page = LoginPage(driver)
    login_page.enter_email("yafaaaq92000@gmail.com")
    login_page.enter_password("13565")
    login_page.click_login_button()
    assert "weak - please enter a stronger password." == login_page.get_the_text_error_message()


def test_successful_registration(driver):
    login_page = LoginPage(driver)
    login_page.enter_email("rasha05109@gmail.com")
    actual_email=login_page.get_email()
    login_page.enter_password("rashtait766g@#")
    login_page.click_login_button()
    expected_username = login_page.get_the_username_locater()
    actual_username = actual_email.split('@')[0]
    assert expected_username == actual_username, "not matching"





