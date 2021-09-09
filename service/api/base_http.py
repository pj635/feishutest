import json

import requests

from feishutest.service.api.log import log

class BaseHTTP:
    def request(self, method, url, *args, **kwargs):
        input = {
            'method': method,
            'url': url,
            **kwargs
        }
        log.debug(json.dumps(input, indent=2, ensure_ascii=False))
        r = requests.request(method = method,
                             url= url,
                             **kwargs)
        log.debug(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r.json()