import time
import allure
import pageObject
from base.baseApi import Base


class PageAddAddress(Base):

    #输入姓名
    @allure.step('输入姓名')
    def input_name(self):
        self.base_input(pageObject.address_name,'布鲁克斯先生')
    #输入电话
    @allure.step('输入电话')
    def input_tel(self):
        self.base_input(pageObject.address_tel,'01088365249')
    #设置省市县
    @allure.step('设置省市县')
    def select_province_city_conty(self):
        # 1.让三个select显示出来 2.依次对三个select进行选择
        self.base_js(pageObject.address_js_prov)
        # 根据索引选择省份
        self.base_select_index(pageObject.address_province,'9')
        time.sleep(1)
        self.base_js(pageObject.address_js_city)
        # 根据text选择城市
        self.base_select_visible_text(pageObject.address_city,'长宁区')
        time.sleep(1)
        self.base_js(pageObject.address_js_county)
        # 根据value选择区县
        self.base_select_value(pageObject.address_county,'1838')
        time.sleep(1)
    #输入详细地址
    @allure.step('输入详细地址')
    def detail_address(self):
        self.base_input(pageObject.address_detail,'大富豪花园123')
    #输入别名
    @allure.step('输入别名')
    def input_alias(self):
        self.base_input(pageObject.address_alias,'小区')
    #设置是否默认地址
    @allure.step('设置默认地址')
    def set_isdefault(self):
        self.base_click(pageObject.address_isdefault)
    #点击保存
    @allure.step('点击保存按钮')
    def click_save_button(self):
        self.base_click(pageObject.address_save_button)