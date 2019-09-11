# coding=utf-8
from framework.base_page import BasePage


class HomePage(BasePage):

    input_box = "id=>kw"
    search_sumbit_btn = "xpath=>//*[@id='su']"
    # 百度新闻入口
    news_link = "xpath=>//*[@id='u1']/a[@name='tj_trnews']"
    def typer_search(self,text):
        self.type(self.input_box,text)

    def send_sumbit_btn(self):
        self.click(self.search_sumbit_btn)

    def click_news(self):
        self.click(self.news_link)
        self.sleep(2)
