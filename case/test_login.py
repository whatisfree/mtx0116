import time

from base.baseApi import Base
from base.driver import Driver
from pageAction.login_action import Login
import pytest
import allure
from tool.readData import ReadData

data = ReadData().get_yaml('login_data','test_login')
@allure.feature('登录功能')
class TestLogin:

    def setup_class(self):
        #创建driver
        self.driver = Driver.get_driver()
        #创建Login对象
        self.login = Login(self.driver)
        # 创建base对象，调用page_source的方法
        self.base = Base(self.driver)
    # def test_login(self):
    #     self.login.login_success()
    #     time.sleep(2)
    #     assert 'Apple2020，欢迎来到' in self.driver.page_source
    @pytest.mark.parametrize('args',data)
    @allure.title('登录测试-参数化测试4个异常1个正常')
    def test_login(self,args):
        self.login.login_business(args['accounts'],args['pwd'])
        time.sleep(2)
        assert args['assert'] in self.base.base_page_source

    def teardown_class(self):
        Driver.close_driver()

