from pageAction.actions_manager import ActionsManager


class Login(ActionsManager):

    #登录成功的业务
    def login_success(self):
        # 点击登录链接
        self.pageindex.click_login_link()
        #输入用户名
        self.pagelogin.input_name('Apple2020')
        #输入密码
        self.pagelogin.input_pwd('123456')
        #点击登录按钮
        self.pagelogin.click_login_button()

    #登录业务组合
    def login_business(self,username,pwd):

        # 点击登录链接
        self.pageindex.click_login_link()
        #输入用户名
        self.pagelogin.input_name(username)
        #输入密码
        self.pagelogin.input_pwd(pwd)
        #点击登录按钮
        self.pagelogin.click_login_button()