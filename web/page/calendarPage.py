from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from feishutest.web.page.basePage import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CalendarPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def add_calendar(self, calendar_name, range = None, description = None):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "今天")]')))
        self.driver.find_element_by_xpath('//*[@class="sidebar-more-trigger"]').click()
        self.driver.find_element_by_xpath('//*[text()="新建日历"]').click()
        sleep(5)
        self.driver.find_element_by_xpath('//*[@placeholder="日历名称"]').send_keys(calendar_name)
        self.driver.find_element_by_xpath('//*[@class="info-wrapper"]').click()
        if range == "private":
            self.driver.find_element_by_xpath('//*[text()="私密"]').click()
        elif range == "busy":
            self.driver.find_element_by_xpath('//*[text()="仅显示忙碌"]').click()
        elif range == "public":
            self.driver.find_element_by_xpath('//*[text()="公开"]').click()
            self.driver.find_element_by_xpath('//*[text()="确定"]').click()
        if description:
            self.driver.find_element_by_xpath('//*[@placeholder="添加描述"]').send_keys(description)
        self.driver.find_element_by_xpath('//*[text()="创建"]').click()
        return self

    def get_calendar_list(self):
        calendar_list = []
        elements = self.driver.find_elements_by_xpath('//*[@class="calendars"]//*[@class="summary"]')
        for e in elements:
            calendar_list.append(e.text)
        return calendar_list

    def pause(self, time: int):
        sleep(time)
        return self

    def delete_all_calendar(self):
        elements = self.driver.find_elements_by_xpath('//*[@class="calendars"]//*[@class="summary"]')
        for i in range(len(elements) - 1):
            c = self.driver.find_element_by_xpath('//*[@class="calendars"]//*[@class="calendar-item"][2]')
            e = self.driver.find_element_by_xpath('//*[@class="calendars"]//*[@class="calendar-item"][2]//*[contains(@class, "larkc-svg-icon setting")]')
            ActionChains(self.driver).move_to_element(c).move_to_element(e).click().perform()
            self.driver.find_element_by_xpath('//*[@class="delete-item"]//*[text()="删除日历"]').click()
            self.driver.find_element_by_xpath('//*[text()="确定"]').click()
        return self




