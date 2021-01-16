import pageObject
from base.baseApi import Base
import allure

class PageIndex(Base):

    #点击登录
    @allure.step('点击登录链接')
    def click_login_link(self):
        self.base_click(pageObject.index_login_link)
    #点击个人中心
    @allure.step('点击个人中心链接')
    def click_personal_link(self):
        self.base_click(pageObject.index_personal_link)
    @allure.step('点击页面最上面的购物车链接')
    def click_cart_link(self):
        self.base_click(pageObject.index_cart_link)
    #滚动条到最下面
    @allure.step('滚动条拉到最下面')
    def scroll_bottom(self):
        self.base_js(pageObject.index_js)
    #点击要购买的商品
    @allure.step('点击要购买的商品链接')
    def click_goods_link(self):
        self.base_click(pageObject.index_goods_link)
    #切换到商品页面的窗口
    @allure.step('切换到商品页面')
    def switch_goods_window(self):
        self.base_switch_window(pageObject.goods_title)
