import time

from pageAction.actions_manager import ActionsManager


class Order(ActionsManager):

    #下单业务组合
    def order_business(self):
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
        #在商品页面点击立即购买
        self.pagegoods.click_buy_button()
        time.sleep(1)

        #在结算页面选择支付方式-货到付款
        self.pageorder.choose_payment()
        time.sleep(1)
        #在结算页面点击提交订单按钮
        self.pageorder.click_submit_order()
