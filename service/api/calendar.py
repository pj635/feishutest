from __future__ import annotations

import json

from feishutest.service.api.feishuAPI import FeiShuAPI
from feishutest.service.api.log import log


class Calendar(FeiShuAPI):
    def __init__(self, token, env = None, **kwargs):
        super().__init__(token, env)

        self.calendar_id = kwargs.get('calendar_id')
        self.color = kwargs.get('color')
        self.description = kwargs.get('description')
        self.permissions = kwargs.get('permissions')
        self.role = kwargs.get('role')
        self.summary = kwargs.get('summary')
        self.summary_alias = kwargs.get('summary_alias')
        self.type = kwargs.get('type')

    def create(self, summary, **kwargs):
        url = "https://open.feishu.cn/open-apis/calendar/v4/calendars"
        method = "post"
        kwargs["summary"] = summary

        log.debug(json.dumps(kwargs, indent=2, ensure_ascii=False))
        r = self.request(method, url, json = kwargs)
        return r

    def list(self, **kwargs) -> list[Calendar]:
        url = "https://open.feishu.cn/open-apis/calendar/v4/calendars"
        method = "GET"

        r = self.request(method, url, params=kwargs)
        calendar_list:list[Calendar] = []
        for data in r['data']['calendar_list']:
            if data['type'] != 'primary':
                calendar_list.append(Calendar(self.token, **data))
        return calendar_list

    def delete(self, calendar_id):
        url = f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}'
        method = 'delete'
        r = self.request(url=url, method=method)
        return r

    def delete_all(self):
        calendar_list = self.list()
        for calendar in calendar_list:
            calendar.delete(calendar.calendar_id)

    def update(self, calendar_id, **kwargs):
        url = f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}'
        method = 'PATCH'
        r = self.request(url = url, method = method, json = kwargs)
        return r


