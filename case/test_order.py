import time

from base.baseApi import Base
from base.driver import Driver
from pageAction.login_action import Login
import pytest
import allure
from pageAction.order_action import Order

@allure.feature('下单功能')
class TestOrder:

    def setup_class(self):
        #创建driver
        self.driver = Driver.get_driver()
        #创建Login对象
        self.login = Login(self.driver)
        #调用登录成功方法
        self.login.login_success()
        time.sleep(2)
        #创建Order对象
        self.order = Order(self.driver)
        #创建base对象，获取page_source
        self.base = Base(self.driver)

    @allure.title('下单方法测试-正向测试')
    def test_order(self):

        self.order.order_business()
        time.sleep(2)
        assert '支付成功' in self.base.base_page_source

    def teardown_class(self):

        Driver.close_driver()