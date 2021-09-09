from feishutest.service.api.base_http import BaseHTTP


class FeiShu(BaseHTTP):
    def __init__(self, appid = "cli_a1a5c6a761b89013", app_secret = "fwZtzrORunv2Oi4k4F5r3cHbQdSj6PZh"):
        self.token = None
        self._app_id = appid
        self._app_secret = app_secret

    def get_token(self):
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        method = "post"

        if self.token is None:
            r = self.request(method, url,
                json = {
                    'app_id': self._app_id,
                    'app_secret': self._app_secret
                }
            )
            self.token = r["tenant_access_token"]

        return self.token