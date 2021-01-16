import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

import pageObject
from setting import DIR_NAME
from tool.logger import GetLogger
log = GetLogger().get_logger()
class Base():
    def __init__(self,driver):
        log.info("开始初始化driver对象()".format(driver))
        self.driver = driver
    def base_click_index(self):
        '''
        点击mtx商城的首页
        :return:
        '''
        self.base_click(pageObject.index_link)
    #封装打开页面
    def base_open(self,url):
        log.info('打开页面url:%s' % url)
        self.driver.get(url)
    #最大化页面
    def base_max_window(self):
        self.driver.maximize_window()
        log.info("Set browser window maximized")
    #封装查找元素方法
    def base_find_element(self, loc, timeout=30, poll_frequency=0.5):
        log.info('正在查找元素:{}元素，最多等待:{}秒'.format(loc,timeout))
        el = WebDriverWait(self.driver,timeout=timeout,poll_frequency=poll_frequency).until(lambda x:x.find_element(*loc))
        return el
    #封装点击
    def base_click(self,loc):
        log.info('正在点击:{}元素'.format(loc))
        self.base_find_element(loc).click()
    #封装输入
    def base_input(self,loc,content):
        log.info('正在对:{}元素进行输入操作'.format(loc))
        el = self.base_find_element(loc)
        el.clear()
        el.send_keys(content)
        log.info('输入：{}'.format(content))
    #封装窗口切换:通过窗口title进行切换
    def base_switch_window(self,title):
        log.info('切换到目标窗口，标题为：{}'.format(title))
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                break
    #封装对iframe的切换
    def base_switch_iframe(self,frame):
        '''
        3种用法:
            driver.switch_to.frame('frame_name')
            driver.switch_to.frame(1)
            driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
        '''
        log.info('正在进入iframe:{}'.format(frame))
        self.driver.switch_to.frame(frame)
    #封装iframe切换回之前的窗口
    def base_default_iframe(self):
        log.info('从iframe切换到之前窗口')
        self.driver.switch_to.default_content()
    # 截图操作
    def base_get_image(self):
        log.info('开始截图====')
        self.driver.get_screenshot_as_file(DIR_NAME+'/image/{}.png'.format(time.strftime('%Y-%m-%d_%H_%M_%S')))

    # 添加cookie
    def base_add_cookie(self,name,value):
        '''
        添加cookie
        :param name:
        :param value:
        :return:
        '''
        log.info('正在添加cookie=====')
        self.driver.add_cookie({'name': name, 'value': value})

    # 判断元素是否存在
    def base_if_is_exist(self,loc):
        '''
        如果可以找到元素，那么就返回True，找不到就返回False
        :param loc:
        :return:
        '''
        try:
            log.info(f'判断{loc}元素是否存在')
            self.base_find_element(loc)
            log.info(f'{loc}元素是存在的')
            return True
        except:
            log.error(f'{loc}元素不存在')
            return False

    # @property 加上这个就会把函数变成属性-前提是你的函数是不需要传参数的
    @property
    def base_page_source(self):
        return self.driver.page_source

    def base_js(self, script):
        '''
        Execute JavaScript scripts.

        Usage:
        driver.base_js("window.scrollTo(200,1000);")
        '''
        self.driver.execute_script(script)
        log.info("Execute JavaScript scripts. %s" % script)
    # 获取文本内容
    def base_get_text(self,loc):
        log.info(f'定位到元素{loc}')
        return self.base_find_element(loc).text
    def base_set_window(self, wide, high):
        '''
        Set browser window wide and high.

        Usage:
        driver.base_set_window(wide,high)
        '''
        self.driver.set_window_size(wide, high)
        log.info(" Set browser window %s wide and  %s high." % (wide, high))

    def base_get_attribute(self,loc, attribute):
        '''
        Gets the value of an element attribute.

        Usage:
        driver.base_get_attribute(By.CLASS_NAME, 'btn-go',"value")
        '''
        el = self.base_find_element(loc)
        log.info("Gets the value %s of an element attribute %s" % (attribute, loc))
        return el.get_attribute(attribute)

    def base_get_display(self, loc):
        '''
        Gets the element to display,The return result is true or false.

        Usage:
        driver.base_get_display(By.CLASS_NAME, 'btn-go')
        '''
        el = self.base_find_element(loc)
        log.info("The %s element is exits or not" % loc)
        return el.is_displayed()

    def base_get_title(self):
        '''
        Get window title.
        Usage:
        driver.base_get_title()
        '''
        log.info("Get window title.")
        return self.driver.title

    def base_select_value(self, loc, value):
        '''
        Constructor. A check is made that the given element is, indeed, a SELECT tag. If it is not,
        then an UnexpectedTagNameException is thrown.

        :Args:
         - css - element SELECT element to wrap
         - value - The value to match against

        Usage:
            <select name="NR" id="nr">
                <option value="10" selected="">每页显示10条</option>
                <option value="20">每页显示20条</option>
                <option value="50">每页显示50条</option>
            </select>
            driver.base_select("#nr", '20')
            loc = By.CLASS_NAME, 'btn-go'
            driver.base_select(By.CLASS_NAME, 'btn-go', '20')
        '''
        # 先找到元素
        el = self.base_find_element(loc)
        #实例化下拉框，获取select下拉框里面option的值

        Select(el).select_by_value(value)

    def base_select_index(self, loc, index):
        '''
        '''
        # 先找到元素
        el = self.base_find_element(loc)
        # 实例化下拉框，获取select下拉框里面option的值

        Select(el).select_by_index(index)

    def base_select_visible_text(self, loc, text):
        '''
        '''
        # 先找到元素
        el = self.base_find_element(loc)
        # 实例化下拉框，获取select下拉框里面option的值

        Select(el).select_by_visible_text(text)

    def base_forward(self):
        self.driver.forward()
        log.info("Click forward on current pageObject.")

    def base_back(self):
        self.driver.back()
        log.info("Click back on current pageObject.")

    def base_get_alert_text(self):
        '''
        Gets the text of the Alert.

        Usage:
        driver.base_get_alert_text()
        '''
        log.info("Gets the text of the Alert.")
        return self.driver.switch_to.alert.text

    def base_implicitly_wait(self, secs):
        '''
        Implicitly wait.All elements on the pageObject.
        Usage:
        driver.base_implicitly_wait(10)
        '''
        self.driver.implicitly_wait(secs)
        log.info("wait for %d seconds." % secs)

    def base_accept_alert(self):
        '''
        确定alert弹窗
        Accept warning box.

        Usage:
        driver.base_accept_alert()
        '''
        self.driver.switch_to.alert.accept()
        log.info("Accept warning box.")

    def base_dismiss_alert(self):
        '''
        取消alert弹窗
        Dismisses the alert available.

        Usage:
        driver.base_dismiss_alert()
        '''
        self.driver.switch_to.alert.dismiss()
        log.info("Dismisses the alert available.")