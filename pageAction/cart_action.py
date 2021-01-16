import time

from pageAction.actions_manager import ActionsManager


class Cart(ActionsManager):

    #从首页点击商品后加入购物车，
    def cart_add_business(self):
        #在登录后首页下拉滚动条
        self.pageindex.scroll_bottom()
        #在首页找到商品并点击链接
        self.pageindex.click_goods_link()
        #先切换到商品页面的窗口
        self.pageindex.switch_goods_window()
        #在商品页面选择商品颜色粉色
        self.pagegoods.choose_color()
        time.sleep(2)
        # 在商品页面选择商品尺码M
        self.pagegoods.choose_size()
        time.sleep(2)
        #在商品页面点击加入购物车按钮
        self.pagegoods.click_add_cart_button()
        time.sleep(1)
    #在购物车中删除商品的业务组合
    def cart_delete_business(self):
        '''
        功能测试 手动如何操作 -----自动化动作就如何操作
            删除商品之前我们要确保购物车里面有商品
        (推荐)  1. action层，先调用添加购物车这个业务（确保购物车里面有商品），再调用删除业务
               1.1 动作能关联上
               2. case层，调整顺序，插件pytest-ordering (不推荐：测试用例和测试用例之间是相互独立，不依赖)
        '''
        #调用添加购物车业务
        self.cart_add_business()
        # 点击购物车链接
        self.pagegoods.click_cart_link()
        time.sleep(1)
        # 在购物车页面点击第一个商品的删除链接
        self.pagecart.click_delete_link()
        # 在购物车页面删除商品确认框点确定
        self.pagecart.click_delete_confirm_button()

