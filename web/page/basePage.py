import yaml
from selenium import webdriver


class BasePage:
    def __init__(self, driver: webdriver=None):
        if driver:
            self.driver = driver
        else:
            # 实例化 driver
            self.driver = webdriver.Chrome()
            self.driver.get("https://feishu.cn/")
            with open("cookie_data.yaml", encoding="UTF-8") as f:
                cookies = yaml.safe_load(f)
                for cookie in cookies:
                    if cookie['domain'] in self.driver.current_url:
                        c = {
                            'name': cookie['name'],
                            'value': cookie['value'],
                            'domain': cookie['domain']
                        }
                    self.driver.add_cookie(c)
            self.driver.refresh()
            self.driver.maximize_window()
            # self.driver.get("https://e1sm0k24i2.feishu.cn/calendar/week")
            self.driver.implicitly_wait(5)