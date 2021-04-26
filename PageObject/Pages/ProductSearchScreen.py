from selenium.webdriver.common.by import By

from PageObject import Locators


class ProductSearchScreen:
    def __init__(self, driver):
        self.btn_see = driver.find_element(By.XPATH, Locators.btn_see_more_xpath)

    def getBtnSeeMore(self):
        return self.btn_see
