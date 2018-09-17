import os
import smtplib
import mimetypes
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import urllib.request
import time

#获取该文件路径
def get_path():
    proDir = os.path.split(os.path.realpath(__file__))[0]
    return proDir
#运行脚本
def run_test(testcase=[],*devices):
    devices_list = list(devices)
    count_case = str(len(testcase))
    failed_case = 0
    body_html = ''
    # print(testcase)
    # print(devices_list)
    for dev in devices_list:
        for case in testcase:
            base_path = get_path()
            test_case = os.path.join(base_path,case)
            report_path = "D:\\apache-tomcat-8.5.33\\webapps\\DCH_Report" #定义Tomcat路径
            #report_path = os.path.join(base_path,'report') #获取本地测试报告路径,发送邮件时不适用
            case_name = case.split('.')[0]
            report_name = case_name+'_report'
            outfile = os.path.join(report_path,case_name) + '.html'
            implement_case = 'airtest run ' + test_case + ' --device Android:///'+ dev + ' --log ' + report_path
            implement_report = 'airtest report ' + test_case + ' --log_root ' + report_path + ' --outfile ' + outfile
            # print(implement_case)
            # print(implement_report)
            os.system(implement_case)
            os.system(implement_report)
            time.sleep(5)
            send_url = "http://192.168.13.56:8080"+outfile.split("webapps")[-1]
            open_url = "file:///"+outfile
            #print(open_url)
            respone = urllib.request.urlopen(open_url)
            respone_txt = respone.read().decode('utf-8')
            sigin = 'Null'
            if 'Passed' in respone_txt:
                sigin = 'Pass'
                tb_html = '<tr><td style="width: 150px;margin-left:180px;height:30px;text-align:center;">%s</td><td style="width: 500px;"><a href="%s" target=_blank>%s</a></td><td style="width:150px;margin-left:180px;text-align:center;"><span style="color:green;">%s</span></td></tr>' %(case_name,send_url,report_name,sigin)
                body_html += tb_html
            elif 'Failed' in respone_txt:
                sigin = 'Failed'
                tb_html = '<tr><td style="width: 150px;margin-left:180px;height:30px;text-align:center;">%s</td><td style="width: 500px;"><a href="%s" target=_blank>%s</a></td><td style="width:150px;margin-left:180px;text-align:center;"><span style="color:red;">%s</span></td></tr>' %(case_name,send_url,report_name,sigin)
                body_html += tb_html
                failed_case += 1
            else:
                tb_html = '<tr><td style="width: 150px;margin-left:180px;height:30px;text-align:center;">%s</td><td style="width: 500px;"><a href="%s" target=_blank>%s</a></td><td style="width:150px;margin-left:180px;text-align:center;"><span style="color:yellow;">%s</span></td></tr>' %(case_name,send_url,report_name,sigin)
                body_html += tb_html

    success_rate = str('%.2f'%(((float(count_case)-float(failed_case))/float(count_case))*100))+'%'
    title_html = '<tr style="text-align:center;"><td>%s</td><td>%s</td><td>%s</td></tr>' %(count_case,failed_case,success_rate)
    return title_html,body_html




#获取测试报告文件
def get_report_file():
    '''
    寻找测试报告方法，用来构建邮件附件所用
    目前报告直接以邮件html形式发送暂时不用该方法
    '''
    base_path = get_path()
    report_list = []
    report_path = os.path.join(base_path,'report')
    dir_list = os.listdir(report_path)
    file_suffix = '.html'
    for index in dir_list:
        if file_suffix in index:
            report_list.append(os.path.join(report_path,index))
    return report_list

def get_html(title_data,content):
    # print("title:",title_data)
    # print(type(title_data))
    # print("content_text:",content)
    # print(type(content))
    #html_text = [{"test_login":"178.3434/sadasdsadsa.html"},{"test_fin":"uiewr/ewrew/wer.html"},{"test_lin":"sdsa/asdsa/ds.html"}]
    #title_data = "<tr style="text-align:center;"><td>Row:2 Cell:1</td><td>Row:2 Cell:2</td><td>Row:2 Cell:3</td></tr>"
    #content_failed = "<tr><td style="width: 150px;margin-left:180px;height:30px;text-align:center;">测试上传Tomcat</td><td style="width: 500px;"><a href="http://www.baidu.com" target=_blank>http://www.baidu.com</a></td><td style="width:150px;margin-left:180px;text-align:center;"><span style="color:red;">Failed</span></td></tr>tr><td style="width: 150px;margin-left:180px;height:30px;text-align:center;">测试上传Tomcat</td><td style="width: 500px;"><a href="http://www.baidu.com" target=_blank>http://www.baidu.com</a></td><td style="width:150px;margin-left:180px;text-align:center;"><span style="color:red;">Failed</span></td></tr>"
    #content_pass = "<tr><td style="width: 150px;margin-left:180px;height:30px;text-align:center;">Row:1 Cell:1</td><td style="width: 500px;">Row:1 Cell:2</td><td style="width:150px;margin-left:180px;text-align:center;"><span style="color:green;">Pass</span></td></tr>"
    html1 =  """
    <html lang="zh-CN">

<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>Test_Log</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
</head>
<style type="text/css">
	.tftable {font-size:16px;color:#333333;width:80%;border-width: 1px;border-color: #729ea5;border-collapse: collapse;}
	.tftable th {font-size:16px;background-color:#acc8cc;border-width: 1px;padding-right: 8px;padding-top: 8px;padding-bottom: 8px;border-style: solid;border-color: #729ea5;}
	.tftable tr {background-color:#d4e3e5;}
	.tftable td {font-size:12px;border-width: 1px;padding: 8px;border-style: solid;border-color: #729ea5;}
	.tftable tr:hover {background-color:#ffffff;}


	.tftable1 {font-size:16px;color:#fbfbfb;width:30%;border-width: 1px;border-color: #686767;border-collapse: collapse;}
	.tftable1 th {font-size:16px;background-color:#171515;border-width: 1px;padding: 8px;border-style: solid;border-color: #686767;text-align:left;}
	.tftable1 tr {background-color:#171515;}
	.tftable1 td {font-size:12px;border-width: 1px;padding: 8px;border-style: solid;border-color: #686767;}
	<-- .tftable1 tr:hover {background-color:#666666;} -->
</style>
<body>
	<div width="100%" height="100%">
		<center>
			<div style="float:left;">
				<span style="float:left;">大家好:</span><br>
				&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<span>大昌行I_Task_APP测试报告，详情如下：</span>
			</div>
			<center><br><br><br>
				<h1>APP自动化测试报告</h1>
			</center>
			<table class="tftable1" border="1">
				<tr style="text-align:center;"><td>测试用例数</td><td>用例失败数</td><td>通过率</td></tr>"""

    html2 = """
			</table>
			<hr>
			<table class="tftable" border="1">
				<tr><th style="width: 150px;margin-left:180px;height:30px;text-align:center;">测试用例名称</th><th style="width: 500px;">测试报告</th><th style="width:150px;margin-left:180px;text-align:center;">测试结果</th></tr>
			"""

    html3 = """
			</table>
		</center>
	</div>
</body>
</html>
    """
    html = html1+title_data+html2+content+html3
    return html


#发送邮件
def send_email(text):
    report_list = get_report_file()
    mail_host = 'smtp.hostuc.com'
    sender = 'wentao.chen@iris-technologies.com.cn'
    receivers = ['wentao.chen@iris-technologies.com.cn']
    username = 'wentao.chen@iris-technologies.com.cn'
    password = 'iris123'
    mail_port = 25
    #创建一个带附件的实例
    message = MIMEMultipart()
    message['From'] = Header("APP自动化测试组", 'utf-8')
    message['To'] =  Header("各位同事及领导", 'utf-8')
    message['Subject'] = Header('APP自动化测试报告', 'utf-8')
    #邮件正文
    #message.attach(MIMEText("""Hi all:\n \t 利星行APP自动化测试结果详情见如下。""", 'plain', 'utf-8'))
    message.attach(MIMEText(text, 'html', 'utf-8'))
    #构造附件
    # for report_file in report_list:
    #     file_name = report_file.split('\\')[-1]
    #     with open(report_file,'rb') as f:
    #         att = MIMEText(f.read(), 'html','utf-8')
    #         att["Content-Type"] = 'application/octet-stream'
    #         # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    #         att["Content-Disposition"] = 'attachment; filename=%s' %file_name
    #         message.attach(att)
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, int(mail_port))    # 25 为 SMTP 端口号
        smtpObj.login(username,password)
        smtpObj.sendmail(sender,receivers, message.as_string())
        print(u"邮件发送成功")
        #f.close()
    except smtplib.SMTPException as e:
        print(u"Error: 无法发送邮件",e)


#主函数
if __name__ == "__main__":

    #print(get_path())
    testcase = ['test_dch_login.air','test_dch_mining_clues.air','test_dch_no_clue_store.air','test_dch_finance.air',
               'test_dch_insurance.air','test_dch_submit_order.air','test_dch_logout.air']
    #testcase = ['test_dch_login.air']
    #run_test(testcase,"4ae4ee5f")
    #JTJ4C15C15014538   ----   华为手机
    #4ae4ee5f   ------    vivo 手机
    tit_html,bd_html = run_test(testcase,"4ae4ee5f")
    text = get_html(tit_html,bd_html)
    send_email(text)

