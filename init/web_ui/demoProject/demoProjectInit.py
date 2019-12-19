#-*- coding:utf8 -*-
# 作者 yanchunhuo
# 创建时间 2018/01/19 22:36
# 文件名 tee.py
# github https://github.com/yanchunhuo
from base.web_ui.demoProject.web_ui_demoProject_read_config import WEB_UI_DemoProject_Read_Config

class DemoProjectInit:
    def __init__(self):
        self._web_ui_demoProject_read_config=WEB_UI_DemoProject_Read_Config().config

    def init(self):
        if int(self._web_ui_demoProject_read_config.init)==0:
            return

        #每次测试前先清除上次构造的数据
        self._deinit()
        #初始化必要的数据，如在数据库中构建多种类型的账号，
        pass

    def _deinit(self):
        #清除构造的数据
        pass