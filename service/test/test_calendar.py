from time import sleep

import pytest
import yaml

from feishutest.service.api.calendar import Calendar
from feishutest.service.api.feishu import FeiShu
from feishutest.service.api.log import log


class TestCalendar:
    s_time = 5
    def setup_class(self):
        self.token = FeiShu().get_token()
        log.debug(self.token)
        self.calendar = Calendar(self.token)

    def setup(self):
        self.calendar.delete_all() #删除所有日历，清理环境


    @pytest.mark.parametrize('summary', yaml.safe_load(open('./create_calendar.yaml', encoding='UTF-8'))[0])
    @pytest.mark.parametrize('description', yaml.safe_load(open('./create_calendar.yaml', encoding='UTF-8'))[1])
    @pytest.mark.parametrize('permissions', yaml.safe_load(open('./create_calendar.yaml', encoding='UTF-8'))[2])
    @pytest.mark.parametrize('color', yaml.safe_load(open('./create_calendar.yaml', encoding='UTF-8'))[3])
    @pytest.mark.parametrize('summary_alias', yaml.safe_load(open('./create_calendar.yaml', encoding='UTF-8'))[4])
    def test_create(self, summary, description, permissions, color, summary_alias):
        sleep(TestCalendar.s_time) #限制创建频率,防止报190005
        r = self.calendar.create(summary, description = description, \
                                 permissions = permissions, color = color, summary_alias = summary_alias)

        # 如果传入参数是None，则返回对应结果是空字符串
        summary = '' if not summary else summary
        description = '' if not description else description
        permissions = '' if not permissions else permissions
        color = '' if not color else color
        summary_alias = '' if not summary_alias else summary_alias

        assert r["code"] == 0
        assert r["msg"] == "success"
        assert r['data']['calendar']['summary'] == summary
        assert r['data']['calendar']['description'] == description
        assert r['data']['calendar']['permissions'] == permissions
        assert r['data']['calendar']['color'] == color
        assert r['data']['calendar']['summary_alias'] == summary_alias

    def test_delete_exits(self):
        r = self.calendar.create("test_demo")
        assert r["code"] == 0
        assert r["msg"] == "success"

        r = self.calendar.delete(r['data']['calendar']['calendar_id'])
        assert r["code"] == 0
        assert r["msg"] == "success"

    @pytest.mark.parametrize('not_exits_ID', [('feishu.cn_xxxxxxxxxx@group.calendar.feishu.cn'), ('1')])
    def test_delete_not_exits(self, not_exits_ID):
        r = self.calendar.delete(not_exits_ID)
        assert r["code"] == 191001
        assert r["msg"] == "invalid calendar_id"

    @pytest.mark.parametrize('summary', yaml.safe_load(open('./create_calendar.yaml', encoding='UTF-8'))[0])
    @pytest.mark.parametrize('description', yaml.safe_load(open('./create_calendar.yaml', encoding='UTF-8'))[1])
    @pytest.mark.parametrize('permissions', yaml.safe_load(open('./create_calendar.yaml', encoding='UTF-8'))[2])
    @pytest.mark.parametrize('color', yaml.safe_load(open('./create_calendar.yaml', encoding='UTF-8'))[3])
    @pytest.mark.parametrize('summary_alias', yaml.safe_load(open('./create_calendar.yaml', encoding='UTF-8'))[4])
    def test_update(self, summary, description, permissions, color, summary_alias):
        sleep(TestCalendar.s_time)  # 限制创建频率,防止报190005
        r = self.calendar.create("test_demo")
        assert r["code"] == 0
        assert r["msg"] == "success"

        r = self.calendar.update(r['data']['calendar']['calendar_id'], summary = summary, description = description, \
                                 permissions = permissions, color = color, summary_alias = summary_alias)

        #如果传入参数为None ，则原来的内容不更新
        summary = r['data']['calendar']['summary'] if summary is None else summary
        description = r['data']['calendar']['description'] if description is None else description
        permissions = r['data']['calendar']['permissions'] if permissions is None else permissions
        color = r['data']['calendar']['color'] if color is None else color
        summary_alias = r['data']['calendar']['summary_alias'] if summary_alias is None else summary_alias

        assert r["code"] == 0
        assert r["msg"] == "success"
        assert r['data']['calendar']['summary'] == summary
        assert r['data']['calendar']['description'] == description
        assert r['data']['calendar']['permissions'] == permissions
        assert r['data']['calendar']['color'] == color
        assert r['data']['calendar']['summary_alias'] == summary_alias


    def test_list(self):
        for i in range(10):
            sleep(TestCalendar.s_time)  # 限制创建频率,防止报190005
            r = self.calendar.create(f"test_demo{i}")
            assert r["code"] == 0
            assert r["msg"] == "success"
        list = self.calendar.list()
        for calendar in list:
            log.debug(calendar.summary)
        assert len(list) == 10






