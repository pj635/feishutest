import pytest
import allure

from feishutest.web.page.mainPage import MainPage

@allure.feature("日历页面测试用例集")
class Test_Calendar:
    def setup_class(self):
        self.calendarPage = MainPage().goto_calendar()

    def setup(self):
        self.calendarPage.delete_all_calendar() #清理环境

    def teardown_class(self):
        self.calendarPage.driver.quit()

    @allure.story("创建日历用例")
    @pytest.mark.parametrize('calendar_name, range, description',[
        ('calendar1', 'private', 'this is a test calendar'),
        ('calendar2', 'public', 'this is a test calendar'),
        ('calendar3', 'busy', '')
    ])
    def test_create_calendar(self,calendar_name, range, description):
        calendar_list =  self.calendarPage.add_calendar(calendar_name, range, description).pause(2).get_calendar_list()
        assert calendar_name in calendar_list

    @allure.story("删除日历用例")
    def test_delete_calendar(self):
        calendar_list = self.calendarPage.add_calendar('delete1').pause(5).get_calendar_list()
        assert 'delete1' in calendar_list
        calendar_list = self.calendarPage.add_calendar('delete2').pause(5).get_calendar_list()
        assert 'delete2' in calendar_list
        calendar_list = self.calendarPage.add_calendar('delete3').pause(5).get_calendar_list()
        assert 'delete3' in calendar_list
        self.calendarPage.delete_all_calendar()

