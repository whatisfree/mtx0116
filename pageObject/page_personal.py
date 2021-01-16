import pageObject
from base.baseApi import Base
import allure

class PagePersonal(Base):
    # 点击我的地址链接
    @allure.step('点击我的地址链接')
    def click_myaddress(self):
        self.base_click(pageObject.personal_my_address_link)

    #点击新增地址按钮
    @allure.step('点击新增地址按钮')
    def click_newaddress_button(self):
        self.base_click(pageObject.personal_new_address_button)

    # 切换进新增地址的iframe中
    @allure.step('切换到新增地址的iframe中')
    def switch_iframe(self):
        self.base_switch_iframe(2)