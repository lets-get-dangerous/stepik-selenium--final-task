import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('promo_offer',
                         [pytest.param(i, marks=pytest.mark.xfail(i==7, reason=''))
                          for i in range(10)])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    
    page = ProductPage(browser, link)
    page.open()
    
    page.should_be_add_to_cart_button()
    page.add_product_to_cart()

    page.solve_quiz_and_get_code()
    #import time;time.sleep(30)
    
    page.should_be_success_message()    
    page.should_be_basket_cost_message()

    product_name = page.get_product_name()
    price = page.get_product_price()
    page.check_product_name_in_success_message_is_equal(product_name)
    page.check_basket_cost_in_message_is_equal(price)
