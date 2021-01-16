from selenium.webdriver.common.by import By
'''
各个业务用到的配置(url、元素、js等等)
'''
url = 'http://121.42.15.146:9090/mtx/'
#各个页面都可以点击首页链接
index_link = By.CSS_SELECTOR,'div#doc-topbar-collapse>ul>li:nth-child(1)>a'
'''
以下是首页的配置信息
'''
index_cart_link = (By.XPATH,'//span[text()="购物车"]')
index_login_link = (By.LINK_TEXT,'登录')
index_personal_link = (By.XPATH,'//*[text()="个人中心"]')
index_js = "window.scrollTo(0,document.body.scrollHeight)"
index_goods_link = (By.XPATH,'//a[text()="ZK星星绣花雪纺连衣裙中长款sukol裙少女心温柔超仙女chic裙子夏"]')
'''
登录用到的配置项：登录页面
'''
login_accounts = (By.NAME,'accounts')
login_pwd = (By.XPATH,'//input[@name="pwd"]')
login_button = (By.XPATH,'//form/div[3]/button')
'''
个人中心页面的元素配置，个人中心页面
'''
personal_my_address_link = (By.XPATH,'//div[@id="user-offcanvas"]/div/ul/li[4]/ul/li[2]')
personal_new_address_button = (By.XPATH,'//button[@data-popup-title="新增地址"]')
'''
新增地址用到的配置：新增地址前要进入iframe,索引是2，新增地址页面
'''
address_name = (By.XPATH,'//input[@name="name"]')
address_tel = (By.XPATH,'//input[@name="tel"]')
address_js_prov = "document.querySelectorAll('select')[0].style.display='inline'"
address_js_city = "document.querySelectorAll('select')[1].style.display='inline'"
address_js_county = "document.querySelectorAll('select')[2].style.display='inline'"
address_province = (By.XPATH,'//select[@name="province"]')
address_city = (By.XPATH,'//select[@name="city"]')
address_county = (By.XPATH,'//select[@name="county"]')
address_detail =(By.XPATH,'//input[@name="address"]')
address_alias =(By.XPATH,'//input[@name="alias"]')
address_isdefault = (By.XPATH,'//span[text()="否"]')
address_save_button = (By.XPATH,'//button[text()="保存"]')
'''
购买裙子用到的配置：商品页面
'''
goods_title = 'ZK爆款连衣裙'
goods_color = (By.XPATH,'//form[@name="loginform"]/div[1]/div[1]/ul/li[1]')
goods_size = (By.XPATH,'//li[@data-value="M"]')
goods_buy_now = (By.XPATH,'//button[text()="立即购买"]')
goods_add_cart = (By.XPATH,'//button[text()="加入购物车"]')
goods_cart_link = (By.XPATH,'//span[text()="购物车"]')
'''
购物车用到的配置：购物车页面
'''
cart_delete_goods = (By.XPATH,'(//a[text()="删除"])[1]')
cart_delete_confirm = (By.XPATH,'//span[text()="确定"]')
'''
下单用到的元素配置：结算页面
'''
order_payment = By.XPATH, '//*[text()="货到付款"]'
order_submit = By.XPATH,'//*[text()="提交订单"]'


