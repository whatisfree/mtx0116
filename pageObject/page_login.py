import pageObject
from base.baseApi import Base
import allure

class PageLogin(Base):
    # 输入用户名
    @allure.step('输入用户名')
    def input_name(self, username):
        self.base_input(pageObject.login_accounts, username)

    # 输入密码
    @allure.step('输入密码')
    def input_pwd(self, pwd):
        self.base_input(pageObject.login_pwd, pwd)

    # 点击登录按钮
    @allure.step('点击登录按钮')
    def click_login_button(self):
        self.base_click(pageObject.login_button)