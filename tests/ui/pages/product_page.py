from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add_to_basket_button()
        self.should_be_product_name()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "Add to basket button is not " \
                                                                                   "presented"

    def should_be_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"

    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_product_name_in_success_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        WebDriverWait(self.browser, 10).until(ec.text_to_be_present_in_element(ProductPageLocators.SUCCESS_MESSAGE,
                                                                               product_name))
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        print(success_message.text)
        print(product_name)
        assert product_name == success_message.text, "The product name is not presented in add to basked succeed " \
                                                     "message "

    def should_be_product_price_in_basket_value_message(self):
        basket_value_message_text = self.browser.find_element(*ProductPageLocators.BASKET_VALUE_MESSAGE).text
        product_price_text = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        index = basket_value_message_text.find(product_price_text)
        assert index != -1, "The product price is not equal to the price in basket value message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_success_message_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should be disappeared"
