from allure_commons.types import AttachmentType

from libglobal.Utility import Base
from PageObject.Pages.HomeScreen import HomeScreen
import allure


class TestMobileTesting(Base):
    @allure.severity(allure.severity_level.CRITICAL)
    def test_order(self):
        driver = self.launch_app()
        h = HomeScreen(driver)
        self.btn_click(h.getBtnContinue())
        allure.attach(self.driver.get_screenshot_as_png(), name="amzon", attachment_type=AttachmentType.PNG)
