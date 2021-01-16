from selenium import webdriver

class OpenDriver:
    def get_driver(self, browser):
        '''
        对具体创建哪一个浏览器driver的封装
        :param browser: 浏览器的名字，比如ie，firefox，chrome
        :return: 指定浏览器的driver对象
        '''
        browser = browser.lower()
        if browser == 'firefox' or browser =='ff':
            driver = webdriver.Firefox()
            return driver
        elif browser == 'chrome' or browser =='ch' or browser =='谷歌':
            driver = webdriver.Chrome()
            return driver
        elif browser == 'ie':
            driver = webdriver.Ie()
            return driver
        elif browser == '360':
            return webdriver.Ie()
        else:
            raise NameError('Not found {} browser,you can make sure it'.format(browser))