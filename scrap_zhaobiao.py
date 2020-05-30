import time
import datetime
import requests
from lxml import etree
from pyquery import PyQuery as pq
import yagmail
import email
from email.mime.text import MIMEText
from email.header import Header
import smtplib


def get_time():

	t = datetime.datetime.now()
	if int(t.hour)<10:
		th = '0'+str(t.hour)
	else:
		th = t.hour
	if int(t.minute) < 10:
		tm = '0' + str(t.minute)
	else:
		tm = t.minute
	if int(t.second)<10:
		ts = '0'+str(t.second)
	else:
		ts = t.second

	t_send ='（{}年{}月{}日 {}:{}:{}）'.format(t.year,t.month,t.day,th,tm,ts)
	return t_send


def url_search():
	time_send = get_time()
	print("0000")
	url = 'https://www.bidcenter.com.cn/zhaobiao/zbkeyw-50072-520000.html'
	r = requests.get(url)

	doc = pq(r.text)
	print(type(doc))
	title = doc('#content div div:nth-child(1) a').text()
	print(type(title),title)
	t = title.split(' ')
	print(type(t),t)
	str_search = '信息化'
	ctrl = False
	for i in t:
		if i.count(str_search) >0:
			print(i)
			send_mail(i+time_send)
			ctrl = True
	if not ctrl:
		send_mail('检索 '+str_search+" 的结果为 0")


def sendmail():
	mail_host = "smtp.21cn.com"
	mail_user = "mzhu@21cn.com"
	mail_password = "3931"

	sender = 'mzhu@21cn.com'
	mail_to = ['mzhu@21cn.com']

	message = MIMEText('python testing of sending mail','plain','utf-8')
	message['From'] = Header("mzhu@21cn.com",'utf-8')
	message['To'] = Header("test",'utf-8')

	subject = 'Python smtp mail test'
	message['Subject'] = Header(subject,'utf-8')

	try:
		smtpobj = smtplib.SMTP()
		smtpobj.connect(mail_host,25)
		smtpobj.login(mail_user,mail_password)
		smtpobj.sendmail(sender,mail_to,message.as_string())
		print("邮件发送成功")

	except:
		print("无法发送邮件")


def send_mail(subject):
	#设置服务器，用户名、口令以及邮箱的后缀
	mail_host="smtp.163.com"
	mail_user="mzhugz"
	mail_pass="GYQCRTRWIYWBOFXJ"
	mail_postfix="163.com"
	me = mail_user+"<"+mail_user+"@"+mail_postfix+">"

	msg = MIMEText("hello world mail 2222")
	msg['Subject'] = subject
	msg['From'] = me
	# msg['To'] = mail_user+"<"+mail_user+"@"+mail_postfix+">"
	to_list = ['zhuysh@bingosoft.net','38945677@qq.com','mzhugz@163.com']

	# print('11: ',me)
	try:
		s = smtplib.SMTP()
		s.connect(mail_host)
		s.login(mail_user,mail_pass)
		s.sendmail(me, to_list, msg.as_string())
		s.close()
		print('true')
		# return True
	except:
		#print '2'
		print('failed')
		# return False


def to_mail():
	import smtplib
	from email.mime.text import MIMEText
	from email.header import Header
	 
	# 第三方 SMTP 服务
	mail_host="smtp.21cn.com"  #设置服务器
	mail_user="mzhu@21cn.com"    #用户名
	mail_pass="3931"   #口令
	 
	 
	sender = 'mzhu@21cn.com'
	receivers = ['38945677@qq.com','mzhu@21cn.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
	 
	message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
	# message['From'] = Header("菜鸟教程", 'utf-8')
	# message['To'] =  Header("测试", 'utf-8')
	 
	subject = 'Python SMTP 邮件测试'
	message['Subject'] = Header(subject, 'utf-8')
	 
	 
	try:
		smtpObj = smtplib.SMTP(mail_host,25)
		smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
		smtpObj.login(mail_user,mail_pass)
		smtpObj.sendmail(sender, receivers, message.as_string())
		print("邮件发送成功")
	except smtplib.SMTPException:
		print("Error: 无法发送邮件")



def mail():
	try:

		yag = yagmail.SMTP(user='mzhu@21cn.com', password='3931', host='smtp.21cn.com')
		contents = 'this is a mail send by phthon.'  # 正文内容
		mail_to = 'mzhu@21cn.com'
		yag.send(mail_to, 'subject：hello World', contents)
		print('success')
	except:
		print('failed')

url_search()


