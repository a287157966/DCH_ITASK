# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
#keyevent("3")
#poco.swipe([0.5,0.8],[0.5,0.2])
# keyevent("POWER")
# poco.swipe([0.5,0.8],[0.5,0.2])
# keyevent("DPAD_UP")
poco("com.iris.dch.itask:id/title").child("android.widget.TextView")[0].click()
poco("com.iris.dch.itask:id/open").click()
touch(Template(r"tpl1537414963336.png", record_pos=(-0.444, -0.787), resolution=(720, 1280)))
poco("com.iris.dch.itask:id/et_login_user").click()
text("hjhjhj")


