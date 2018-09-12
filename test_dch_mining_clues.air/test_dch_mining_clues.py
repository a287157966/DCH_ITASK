# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
from dch_common import config
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
poco("com.iris.dch.itask:id/fragment_btm_bt").child("android.widget.LinearLayout").child("android.widget.RelativeLayout")[2].child("android.widget.TextView").click()
poco(text="挖掘").click()
poco("com.iris.dch.itask:id/title").child("android.widget.TextView")[3].click()

#touch(Template(r"tpl1536574335547.png", record_pos=(0.433, -0.756), resolution=(1440, 2560)))
#touch([1360.5, 171.8])

poco("com.iris.dch.itask:id/et_recommended_name").click()
#text("qwe")
text(config.get_coustom_name())
poco("com.iris.dch.itask:id/et_recommended_phone").click()
#text("17766652342")
text(config.get_coustom_mobile())
poco("com.iris.dch.itask:id/bt_recommended_car").click()
poco(text="一汽丰田 PbP RAV4").click()
poco(text="RAV4 2.0 新锐版").click()
poco(text="RAV4 2.0 新锐版 FDV1/2/3").click()
# touch(Template(r"tpl1536553450997.png", record_pos=(-0.031, 0.412), resolution=(720, 1280)))
# touch(Template(r"tpl1536553488439.png", record_pos=(-0.033, 0.412), resolution=(720, 1280)))
# touch(Template(r"tpl1536553504156.png", record_pos=(-0.033, 0.414), resolution=(720, 1280)))
poco("com.iris.dch.itask:id/title").child("android.widget.TextView")[1].click()
poco("com.iris.dch.itask:id/bt_recommended_level").click()
#touch(Template(r"tpl1536558757592.png", record_pos=(0.078, 0.233), resolution=(720, 1280)))
poco(text="A:一周内订单").click()
poco("com.iris.dch.itask:id/bt_confirm").click()
sleep(3)








