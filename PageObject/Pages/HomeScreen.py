from selenium.webdriver.common.by import By
from PageObject import Locators


class HomeScreen:
    def __init__(self, driver):
        self.btn_con = driver.find_element(By.ID, Locators.btn_continue_id)

    # getters
    def getBtnContinue(self):
        return self.btn_con
