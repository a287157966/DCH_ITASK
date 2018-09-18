# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
auto_setup(__file__)

poco("com.iris.dch.itask:id/fragment_btm_bt").child("android.widget.LinearLayout").child("android.widget.RelativeLayout")[1].child("android.widget.TextView").click()
poco(text="保险").click()
poco("com.iris.dch.itask:id/tv_model_car").click()
poco(text="一汽丰田 PbP RAV4").click()
poco(text="RAV4 2.0 新锐版").click()
poco(text="RAV4 2.0 新锐版 FDV1/2/3").click()
poco("com.iris.dch.itask:id/title").child("android.widget.TextView")[1].click()
#交强险总价
jiaoqiangxian_zongjia = poco("com.iris.dch.itask:id/tv_input_jiaoqiangxian_zongjia").get_text()
#首年商业险总价
sounian_shangyexian_zongjia = poco("com.iris.dch.itask:id/tv_input_sounian_shangyexian_zongjia").get_text()
assert_equal(jiaoqiangxian_zongjia,"5,100.00","交强险金额校验通过")
assert_equal(sounian_shangyexian_zongjia,"7,500.00","商业险总价校验通过")




