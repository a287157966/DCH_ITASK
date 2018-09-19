# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *
from dch_common import config
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)
serach_name = config.get_pickle_info("custom_name")
serach_mobile = config.get_pickle_info("custom_mobile")
poco(text="线索池").click()
sleep(3)
#检查姓名搜索
poco(text="搜索").click()
input_txt = poco("com.iris.dch.itask:id/search_et_input").get_text()
for index in range(len(input_txt)):
    keyevent("DEL")
text(serach_name)
keyevent("Enter")
custom_name = poco("com.iris.dch.itask:id/tv_cus_name").get_text()
assert_equal(custom_name,serach_name,"根据姓名搜索查询成功")
poco(text="取消").click()

poco(text="搜索").click()
input_txt = poco("com.iris.dch.itask:id/search_et_input").get_text()
for index in range(len(input_txt)):
    keyevent("DEL")
text(serach_mobile)
keyevent("Enter")
custom_name = poco("com.iris.dch.itask:id/tv_cus_name").get_text()
assert_equal(custom_name,serach_name,"根据手机搜索查询成功")
poco(text="取消").click()


