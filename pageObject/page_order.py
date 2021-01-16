import pageObject
from base.baseApi import Base


class PageOrder(Base):

    #点击支付方式
    def choose_payment(self):
        self.base_click(pageObject.order_payment)
    #点击提交订单
    def click_submit_order(self):
        self.base_click(pageObject.order_submit)