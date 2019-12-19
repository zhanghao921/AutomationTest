#-*- coding:utf8 -*-
# 作者 yanchunhuo
# 创建时间 2018/01/19 22:36
# 文件名 tee.py
# github https://github.com/yanchunhuo
from assertpy import assert_that
from base.api.demoProject.api_demoProject_client import API_DemoProject_Client

class TestLogin:

    def setup_class(self):
        self._api_demoProject_client=API_DemoProject_Client()
        self._login_path='/horizon/auth/login/'

    def test_get_index(self):
        httpResponse=self._api_demoProject_client.doRequest.get(self._login_path)
        assert_that(200).is_equal_to(httpResponse.status_code)

    def test_search_kw(self):
        params={'wd':'apitest'}
        httpResponse = self._api_demoProject_client.doRequest.get(self._login_path,params)
        assert_that(200).is_equal_to(httpResponse.status_code)
