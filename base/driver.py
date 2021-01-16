from selenium import webdriver

import pageObject
from base.openDriver import OpenDriver


class Driver:
    """
    单例模式的driver
    """
    driver = None
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # cls.driver = webdriver.Chrome()
            cls.driver = OpenDriver().get_driver('chrome')
            cls.driver.get(pageObject.url)
            cls.driver.maximize_window()
        return cls.driver
    @classmethod
    def close_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver=None
