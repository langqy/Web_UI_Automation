#coding=utf-8
from framework.base_page import  BasePage


class SportNewsHomePage(BasePage):
    #NBA入口
    nba_libk = "xpath=>//*[@id=]channel-submenu']/div/span[2]/a[1]"

    def click_nba_link(self):
        self.click(self.nba_libk)
        self.sleep(2)
