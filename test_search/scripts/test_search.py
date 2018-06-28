from base import init_driver
from page import Page
from base import analyze_file
import pytest

class TestSearch:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    @pytest.mark.parametrize("key_word", analyze_file()["test_search"])
    def test_search(self, key_word):
        # 点击放大镜
        self.page.search.click_search()
        # 找到输入框 输入文字
        self.page.search.input_search(key_word)
        # 点击返回
        self.page.search.click_back()
    #
    # @pytest.mark.parametrize("key_word", ["1", "hello", "你好"])
    # def test_search1(self, key_word):
    #     # 点击放大镜
    #     self.page.search.click_search()
    #     # 找到输入框 输入文字
    #     self.page.search.input_search(key_word)
    #     # 点击返回
    #     self.page.search.click_back()
