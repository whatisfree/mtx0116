import time

from base.baseApi import Base
from base.driver import Driver
from pageAction.cart_action import Cart
from pageAction.login_action import Login
import pytest
import allure


@allure.feature('购物车功能')
class TestCart:

    def setup_class(self):
        #创建driver
        self.driver = Driver.get_driver()
        #创建Login对象
        self.login = Login(self.driver)
        #调用登录成功方法
        self.login.login_success()
        time.sleep(2)
        #创建Cart对象
        self.cart = Cart(self.driver)
        #创建base对象，获取page_source
        self.base = Base(self.driver)
    def teardown_method(self):
        # 第一种，在装置器，teardown_method()方法里面增加点击‘首页’链接的动作(这样前一个用例错误，也能执行第二个用例)
        self.base.base_click_index()
    @allure.title('购物车商品测试-添加商品测试')
    def test_add(self):
        try:
            self.cart.cart_add_business()
            time.sleep(1)
            assert '加入成功' in self.base.base_page_source
        except:
            self.base.base_get_image()
            assert False
    @allure.title('购物车商品测试-删除商品测试')
    def test_delete(self):
        try:
            self.cart.cart_delete_business()
            time.sleep(1)
            assert '删除成功' in self.base.base_page_source
        except:
            self.base.base_get_image()
            assert False
    def teardown_class(self):

        Driver.close_driver()