from .base_page import BasePage
from .locators import ProductPageLocators as locator
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    def add_product_to_cart(self):
        button = self.browser.find_element(*locator.BUTTON_ADD_TO_CART)
        button.click()        

    def check_basket_cost_in_message_is_equal(self, price):
        cost = self.browser.find_element(*locator.MESSAGE_CART_COST__COST).text
        assert cost == price, "Basket cost is not equal product price."
        
    def check_product_name_in_success_message_is_equal(self, product_name):
        name_in_msg = self.browser.find_element(*locator.MESSAGE_SUCCESS__PRODUCT_NAME).text
        assert name_in_msg == product_name, "Name in the message does not match the product name"
    
    def get_product_name(self):
        return self.browser.find_element(*locator.PRODUCT_NAME).text
    
    def get_product_price(self):
        return self.browser.find_element(*locator.PRODUCT_PRICE).text

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*locator.BUTTON_ADD_TO_CART), "Button 'Add to basket' is not found"
        
    def should_be_basket_cost_message(self):
        assert self.is_element_present(*locator.MESSAGE_CART_COST), "Message with total basket cost is not found"

    def should_be_product_name(self):
        assert self.is_element_present(*locator.PRODUCT_NAME), "Product name is not found"
        
    def should_be_product_price(self):
        assert self.is_element_present(*locator.PRODUCT_PRICE), "Product price is not found"
        
    def should_be_success_message(self):
        assert self.is_element_present(*locator.MESSAGE_SUCCESS), "Success message is not found"
        
