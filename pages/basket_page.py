from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_goods(self):
        assert self.is_not_element_present(
            *BasketPageLocators.GOODS_IN_BASKET), "В корзине есть товары, но их быть не должно"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), "Нет сообщения о пустой корзине"