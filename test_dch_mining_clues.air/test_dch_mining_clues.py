# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from dch_common import config
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
poco("com.iris.dch.itask:id/fragment_btm_bt").child("android.widget.LinearLayout").child("android.widget.RelativeLayout")[2].child("android.widget.TextView").click()
poco(text="挖掘").click()
touch(Template(r"tpl1537269425805.png", record_pos=(0.435, -0.754), resolution=(1080, 1920)))

#poco("com.iris.dch.itask:id/title").child("android.widget.TextView")[1].click()

poco("com.iris.dch.itask:id/et_recommended_name").click()
#text("qwe")
custom_name = config.get_coustom_name()
config.modify_pickle("custom_name",custom_name)
text(custom_name)
poco("com.iris.dch.itask:id/et_recommended_phone").click()
#text("17766652342")
custom_mobile = config.get_coustom_mobile()
config.modify_pickle("custom_mobile",custom_mobile)
text(custom_mobile)
poco("com.iris.dch.itask:id/bt_recommended_car").click()
poco(text="一汽丰田 PbP RAV4").click()
poco(text="RAV4 2.0 新锐版").click()
poco(text="RAV4 2.0 新锐版 FDV1/2/3").click()

poco("com.iris.dch.itask:id/title").child("android.widget.TextView")[1].click()
poco("com.iris.dch.itask:id/bt_recommended_level").click()
poco(text="A:一周内订单").click()
poco("com.iris.dch.itask:id/bt_confirm").click()
sleep(3)








