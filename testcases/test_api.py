import requests


class TestCase:
    session = requests.session()

    def test_send_request(self):
        url = 'http://www,baidu.com'
        data = {
            "username": "zhangsan",
            "password": "123"
        }
        res = TestCase.session.request(method='get', url=url, params=data)
        print(res)
