from pageObject.page_cart import PageCart
from pageObject.page_order import PageOrder
from pageObject.page_add_address import PageAddAddress
from pageObject.page_goods import PageGoods
from pageObject.page_personal import PagePersonal
from pageObject.page_index import PageIndex
from pageObject.page_login import PageLogin


class ActionsManager:
    '''
    管理页面对象的
    有多少个页面对象，就实例化多少个，然后其他的业务就继承ActionsManager这个类
    '''
    def __init__(self, driver):
        self.pagelogin = PageLogin(driver)
        self.pageindex = PageIndex(driver)
        self.pagepersonal = PagePersonal(driver)
        self.pageaddaddress = PageAddAddress(driver)
        self.pagegoods = PageGoods(driver)
        self.pageorder = PageOrder(driver)
        self.pagecart = PageCart(driver)