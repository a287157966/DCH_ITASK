# -*- encoding=utf8 -*-
__author__ = "chenwt"
from dch_common import config
from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
try:
    poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)
except IndexError as e:
    with open("D:\\apache-tomcat-8.5.33\\webapps\\DCH_Report\\log.txt",'r+') as f:
        f.truncate()
        f.close()
    print("可能未连接到设备，请检查是否连接:",e)

auto_setup(__file__)

config.setup()
start_app("com.iris.dch.itask")
sleep(5)
txt1 = ''
try:
    txt1 = poco("com.iris.dch.itask:id/btn_login").get_text()
except BaseException as e:
    txt = ''
    print (u'未获取到元素:',e)
if txt1 == '登录':
    poco("com.iris.dch.itask:id/et_login_user").click()
    #text("auto_test")
    text(config.get_dch_config('itask_username'))
    poco("com.iris.dch.itask:id/et_login_psw").set_text(config.get_dch_config('itask_password'))
    #text("111111")
    #不同手机要用set_text 和 text() 两个方法来实现，坑爹啊
    #text(config.login_pwd())
    keyevent("Enter")
    poco("com.iris.dch.itask:id/btn_login").click()
    sleep(3)
    txt2 = poco(text="时间").get_text()
    assert_equal(txt2,'时间','登录成功')

else:
    poco("com.iris.dch.itask:id/im_circle").click()
    poco("com.iris.dch.itask:id/tv_menu_tuichu").click()
    poco("com.iris.dch.itask:id/et_login_user").click()
    #text("auto_test")
    text(config.get_dch_config('itask_username'))
    poco("com.iris.dch.itask:id/et_login_psw").set_text(config.get_dch_config('itask_password'))
    #text("111111")
    #text(config.login_pwd())
    keyevent("Enter")
    poco("com.iris.dch.itask:id/btn_login").click()
    sleep(3)
    txt2 = poco(text="时间").get_text()
    assert_equal(txt2,'时间','登录成功')









