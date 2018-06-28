from selenium.webdriver.common.by import By

from base import BaseAction


class SearchPage(BaseAction):

    # 搜索按钮
    search_button = By.XPATH, "content-desc,搜索"
    search_edit_text = By.ID, "android:id/search_src_text"
    back_button = By.XPATH, "content-desc,收起"

    # 点击放大镜
    def click_search(self):
        self.click(self.search_button)

    # 找到输入框 输入文字
    def input_search(self, text):
        self.input(self.search_edit_text, text)

    # 点击返回
    def click_back(self):
        self.click(self.back_button)
