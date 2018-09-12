# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *
from dch_common import config

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
poco("com.iris.dch.itask:id/im_circle").click()
poco(text="退出登录").click()
txt =  ''
try:
    txt = poco(text="登 录").get_text()  
    print(u'txt:',txt)
except BaseException as e:
    txt = ''
    print (u'未获取到元素:',e)
assert_equal(txt,"登录","退出登录成功")

config.teardown()

