from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        index = self.browser.current_url.find('basket')
        assert index != -1, "Not a basket page url (no 'basket' in url)"

    def should_not_be_basket_items(self):
        self.is_not_element_present(*BasketPageLocators.BASKET_ITEM), "The item is presented in the basket,\
         but should not be"

    def should_be_empty_basket_message(self):
        language = self.browser.execute_script(
            "return window.navigator.userLanguage || window.navigator.language")
        empty_basket_message = ""
        if language == "en":
            empty_basket_message = "Your basket is empty."
        index = self.browser.find_element(*BasketPageLocators.BASKET_CONTENT).text.find(empty_basket_message)
        assert index != -1, "The empty basket message is not presented, but should be"
