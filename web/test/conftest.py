from selenium import webdriver
import yaml

#获取页面cookies
def test_get_cookies():
    driver = webdriver.Chrome()
    driver.get('https://e1sm0k24i2.feishu.cn/calendar/week')
    input("please input enter to continue")
    cookie = driver.get_cookies()
    with open("cookie_data.yaml", "w", encoding="UTF-8") as f:
        yaml.dump(cookie, f)