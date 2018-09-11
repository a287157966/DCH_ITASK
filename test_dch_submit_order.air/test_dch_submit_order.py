# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


auto_setup(__file__)
poco(text="订单").click()
poco.swipe([0.5,0.8],[0.5,0,2])
poco("com.iris.dch.itask:id/tv_input_jine").click()
text("15700")
poco("com.iris.dch.itask:id/title").child("android.widget.TextView")[1].click()
poco("com.iris.dch.itask:id/tv_input_tuikuan_tianshu").click()
text("1")
poco("com.iris.dch.itask:id/title").child("android.widget.TextView")[1].click()
poco("com.iris.dch.itask:id/tv_input_yujikaipiaoriqi").click()
poco("com.iris.dch.itask:id/btnSubmit").click()
poco("com.iris.dch.itask:id/tv_tijiao").click()
poco("com.iris.dch.itask:id/open").click()

