# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *
from dch_common import config
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
poco(text="未进").click()
custom_name = config.get_pickle_info("custom_name")
poco(text=custom_name).click()
#poco("com.iris.dch.itask:id/listview").child("android.widget.FrameLayout")[0].child("com.iris.dch.itask:id/ll_item_bg").child("android.widget.RelativeLayout").child("com.iris.dch.itask:id/ll_cus_info").click()
poco(text="销售平台").click()
txt1 = ''
try:
    txt1 = poco("com.iris.dch.itask:id/tv_add").get_text()
except BaseException as e:
    txt1 = ''
if txt1 == '':
    poco("com.iris.dch.itask:id/tv_id_card").click()
    #text("130768877665243565")
    text(config.get_id_card())
    poco("com.iris.dch.itask:id/title").child("android.widget.TextView")[1].click()
    poco("com.iris.dch.itask:id/tv_province").click()
    poco(text="北京市").click()
    poco("com.iris.dch.itask:id/tv_city").click()
    poco(text="北京市").click()
    poco("com.iris.dch.itask:id/tv_canton").click()
    poco(text="东城区").click()
    poco("com.iris.dch.itask:id/tv_address").click()
    text("jhssdferweirufidsf")
    poco("com.iris.dch.itask:id/title").child("android.widget.TextView")[1].click()
    #滑动展示出车辆信息按钮--由于手机分辨率问题这样有问题导致不同手机滑动不能展示出来
    poco.swipe([0.5, 0.8359375],[0.5, 0.145625])
    poco(text="车辆").click()
    poco(text="车辆信息").click()
    poco("com.iris.dch.itask:id/rb_intent1").click()
    poco(text="车辆信息").click()
    poco.swipe([0.5, 0.8359375],[0.5, 0.245625])
else:
    poco("com.iris.dch.itask:id/tv_add").click()
    poco("com.iris.dch.itask:id/tv_id_card").click()
    #text("130768877665243565")
    text(config.get_id_card())
    poco("com.iris.dch.itask:id/title").child("android.widget.TextView")[1].click()
    poco("com.iris.dch.itask:id/tv_province").click()
    poco(text="北京市").click()
    poco("com.iris.dch.itask:id/tv_city").click()
    poco(text="北京市").click()
    poco("com.iris.dch.itask:id/tv_canton").click()
    poco(text="东城区").click()
    poco("com.iris.dch.itask:id/tv_address").click()
    text("jhssdferweirufidsf")
    poco("com.iris.dch.itask:id/title").child("android.widget.TextView")[1].click()
    poco.swipe([0.5, 0.8359375],[0.5, 0.145625])
    poco(text="车辆").click()
    poco(text="车辆信息").click()
    poco("com.iris.dch.itask:id/rb_intent1").click()
    poco(text="车辆信息").click()
    poco.swipe([0.5, 0.8359375],[0.5, 0.245625])
    
    




    




