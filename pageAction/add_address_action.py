from pageAction.actions_manager import ActionsManager


class AddAddress(ActionsManager):

    #新增地址业务组合
    def add_address_business(self):
        #在登录后的首页点击个人中心
        self.pageindex.click_personal_link()

        #在个人中心页点击我的地址链接
        self.pagepersonal.click_myaddress()
        #在个人中心页点击新增地址按钮
        self.pagepersonal.click_newaddress_button()
        #切换进新增地址的iframe中
        self.pagepersonal.switch_iframe()

        # 输入姓名
        self.pageaddaddress.input_name()
        #输入电话
        self.pageaddaddress.input_tel()
        #设置省市县
        self.pageaddaddress.select_province_city_conty()
        #输入详细地址
        self.pageaddaddress.detail_address()
        #输入别名
        self.pageaddaddress.input_alias()
        #设置是否默认地址
        self.pageaddaddress.set_isdefault()
        #点击保存按钮
        self.pageaddaddress.click_save_button()

