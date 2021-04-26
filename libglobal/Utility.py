from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class Base:
    def launch_app(self):
        des_cap = {
            "deviceName": "HUAWEI Y9s",
            "platformName": "Android",
            "platformVersion": "10",
            "appPackage": "in.amazon.mShop.android.shopping",
            "appActivity": "com.amazon.mShop.home.HomeActivity"
        }
        url = "http://localhost:4723/wd/hub"
        self.driver = webdriver.Remote(desired_capabilities=des_cap, command_executor=url)
        self.driver.implicitly_wait(10)
        return self.driver

    def set_text(self, element, data):
        element.send_keys(data)

    def btn_click(self, ele):
        ele.click()

    def drag_drop(self, src, des):
        tc = TouchAction(self.driver)
        tc.long_press(el=src).move_to(el=des).release().perform()

    def scroll_down(self):
        size = self.driver.get_window_size().get('height')
        start = int(size * 0.5)
        end = int(size * 0.2)
        tc = TouchAction(self.driver)
        tc.press(x=0, y=start).wait(2000).move_to(x=0, y=end).release().perform()

    def scroll_till_locator_found(self, locator):
        while len(locator) == 0:
            self.scroll_down()
