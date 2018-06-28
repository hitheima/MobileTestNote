from .search_page import SearchPage


class Page:

    def __init__(self, driver):
        self.driver = driver

    @property
    def search(self):
        return SearchPage(self.driver)

