# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

poco(text="保险").click()


actual_value=poco("com.iris.dch.itask:id/child5").child("com.iris.dch.itask:id/ll_group").child("android.widget.LinearLayout").child("android.widget.RelativeLayout").child("com.iris.dch.itask:id/tv_lable").get_text()

#actual_value = poco("com.iris.lshitaskse:id/tv_lable").get_text()
try:
    assert_equal(actual_value,"(交强险+商业险)小计:12,500.00","保险验证成功")
except Exception as e:
    poco(text="保险").click()
else:
    poco(text="保险").click()