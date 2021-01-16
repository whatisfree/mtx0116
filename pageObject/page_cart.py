import pageObject
from base.baseApi import Base
import allure

class PageCart(Base):
    # 点击第一个商品的删除链接
    @allure.step('点击第一个商品的删除链接')
    def click_delete_link(self):
        self.base_click(pageObject.cart_delete_goods)

    #点击删除确认框上面的确定
    @allure.step('点击确认删除按钮')
    def click_delete_confirm_button(self):
        self.base_click(pageObject.cart_delete_confirm)

