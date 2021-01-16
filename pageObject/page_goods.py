import pageObject
from base.baseApi import Base
import allure

class PageGoods(Base):

    @allure.step('选中商品粉色')
    #选择颜色-粉色
    def choose_color(self):
        self.base_click(pageObject.goods_color)
    @allure.step('选中商品M尺码')
    #选择尺寸-M
    def choose_size(self):
        self.base_click(pageObject.goods_size)
    @allure.step('立即购买')
    #点击立即购买
    def click_buy_button(self):
        self.base_click(pageObject.goods_buy_now)
    #点击加入购物车
    @allure.step('加入购物车')
    def click_add_cart_button(self):
        self.base_click(pageObject.goods_add_cart)
    #点击上面购物车链接
    @allure.step('点击页面上面的购物车链接')
    def click_cart_link(self):
        self.base_click(pageObject.goods_cart_link)
