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


def send_mail(subject):
	#设置服务器，用户名、口令以及邮箱的后缀
	mail_host="smtp.163.com"
	mail_user="mzhugz"
	mail_pass="********"   #authorized password
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

url_search()


