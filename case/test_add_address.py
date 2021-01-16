import time
import allure
from base.baseApi import Base
from base.driver import Driver
from pageAction.add_address_action import AddAddress
from pageAction.login_action import Login

@allure.feature('新增地址功能')
class TestAddAddress:

    def setup_class(self):
        #创建driver
        self.driver = Driver.get_driver()
        #创建Login对象
        self.login = Login(self.driver)
        # 创建base对象，调用page_source的方法
        self.base = Base(self.driver)
        # 调用登录成功方法
        self.login.login_success()
        time.sleep(2)
        #创建AddAddress对象
        self.addaddress = AddAddress(self.driver)
    @allure.title('新增地址测试-正向测试')
    def test_add_address(self):

        self.addaddress.add_address_business()
        time.sleep(2)
        assert '布鲁克斯先生' in self.base.base_page_source

    def teardown_class(self):

        Driver.close_driver()