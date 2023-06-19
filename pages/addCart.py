from selenium.common import NoSuchElementException
from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    add_to_cart_button = (By.LINK_TEXT,"Add to cart")

    def add_first_n_items_to_cart(self, n=4):
        items_added = 0  # Track the number of items added to the cart
        while items_added < n:
            try:
                product_link = self.find_the_locater(self.add_to_cart_button)
                self.click(product_link)  # Click on the individual item
                self.wait.until(EC.staleness_of(product_link))  # Wait for the product link to disappear after the click
                items_added += 1  # Increment the counter
            except NoSuchElementException:
                pass
