from feishutest.service.api.base_http import BaseHTTP


class FeiShuAPI(BaseHTTP):
    def __init__(self, token, env = None):
        self._host = 'https://open.feishu.cn'
        self.token = token
        self.env = env


    def request(self, method, url, **kwargs):
        if 'headers' in kwargs.keys():
            kwargs['headers']['Authorization'] = f'Bearer {self.token}'
        else:
            kwargs['headers'] = {'Authorization': f'Bearer {self.token}'}

        if url.startswith('/'):
            url = self._host + url

        r = super().request(
            method=method,
            url=url,
            **kwargs
        )
        return r
