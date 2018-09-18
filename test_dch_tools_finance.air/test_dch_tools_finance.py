# -*- encoding=utf8 -*-
__author__ = "chenwt"

from airtest.core.api import *
from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

auto_setup(__file__)
poco("com.iris.dch.itask:id/fragment_btm_bt").child("android.widget.LinearLayout").child("android.widget.RelativeLayout")[1].child("android.widget.TextView").click()
poco(text="金融").click()
poco("com.iris.dch.itask:id/tv_select_model").click()
poco(text="一汽丰田 PbP RAV4").click()
poco(text="RAV4 2.0 新锐版").click()
poco(text="RAV4 2.0 新锐版 FDV1/2/3").click()
poco("com.iris.dch.itask:id/title").child("android.widget.TextView")[1].click()
#保证金额 6744.00
guaranteedAmount = poco("com.iris.dch.itask:id/tv_guarantee_payment").get_text()
#首付金额
downPayment = poco("com.iris.dch.itask:id/tv_down_payment").get_text()
#月供
monthly = poco("com.iris.dch.itask:id/tv_monthly").get_text()
assert_equal(guaranteedAmount,"6744.00","保证金校验通过")
assert_equal(downPayment,"67,440.00","首付金额校验通过")
assert_equal(monthly,"6884.50","月供金额校验通过")





