from feishutest.web.page.basePage import BasePage
from feishutest.web.page.calendarPage import CalendarPage


class MainPage(BasePage):
    def __init__(self, driver = None):
        super().__init__(driver)

    def goto_calendar(self):
        self.driver.find_element_by_xpath('//*[@class="_pp-product-container"]').click()
        self.driver.find_element_by_xpath('//*[@title="日历"]').click()
        self.driver.switch_to.window(self.driver.window_handles[-1])
        return CalendarPage(self.driver)