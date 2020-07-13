import pytest
from .pages.product_page import ProductPage


base_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
urls_list = [pytest.param(base_url + f"?promo=offer{i}",
                          marks=pytest.mark.xfail(i==7, reason=''))
             for i in range(10)]


@pytest.mark.parametrize('link', urls_list)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    
    page.should_be_add_to_cart_button()
    page.add_product_to_cart()

    page.solve_quiz_and_get_code()
    
    page.should_be_success_message()    
    page.should_be_basket_cost_message()

    product_name = page.get_product_name()
    price = page.get_product_price()
    page.check_product_name_in_success_message_is_equal(product_name)
    page.check_basket_cost_in_message_is_equal(price)




@pytest.mark.xfail
@pytest.mark.parametrize('link', [base_url])
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_product_to_cart()
    page.should_not_be_success_message()

    
@pytest.mark.parametrize('link', [base_url])
def test_cant_see_success_message(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
@pytest.mark.parametrize('link', [base_url])
def test_message_disappeared_after_adding_product_to_basket(browser, link): 
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.should_dissapear_of_success_message()
