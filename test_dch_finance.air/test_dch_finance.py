# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


auto_setup(__file__)
poco(text="金融").click()
# actual_value=poco("com.iris.dch.itask:id/tv_lable").get_text()
actual_value=poco("com.iris.dch.itask:id/child4").child("com.iris.dch.itask:id/ll_group").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").child("com.iris.dch.itask:id/tv_lable").get_text()
try:
    assert_equal(actual_value,"小计:￥74,184.00","金融检查成功")
except Exception as e:
    poco(text="金融").click()
else:
    poco(text="金融").click()