from bs4 import BeautifulSoup
import urllib2
import smtplib
import datetime
import time
from apscheduler.scheduler import Scheduler

sched = Scheduler()
sched.daemonic=False
sched.start()

def scrape():
	search_url="http://www.surfline.com/surf-report/pleasure-point-central-california_4190/"
	search_page=urllib2.urlopen(search_url)
	soup=BeautifulSoup(search_page)

	wave_range=soup.find('h2',{'id': 'observed-wave-range'})
	wave_height=wave_range.text
	spot_conditions=soup.find('div',{'id': 'observed-spot-conditions'})
	conditions=spot_conditions.text

	if wave_height[:1]>=5:
		return True, conditions, wave_height
	if "good" in conditions:
		return True, conditions, wave_height
	if "fair" in conditions and wave_height[:1]>=3:
		return True, conditions, wave_height
	return False,conditions,wave_height
			



def send_message():
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	server.starttls()
	server.login( <your email>, <password> )
	go_surfing,conditions,wave_height=scrape()
	conditions=conditions.replace("Conditions","")
	message= "You should go surfing today. The conditions at Pleasure Point are "+ conditions+ "with a wave height of "+wave_height
	print message
	if go_surfing:
		server.sendmail( 'Sam', <your number>@mms.att.net, message)
		server.sendmail( 'Sam', <a friends number>@mms.att.net, message)

	print "Message sent"

def main():
	job=sched.add_interval_job(send_message,minutes=0.2,start_date='2014-11-11 10:00:00', args="")


if __name__=="__main__":
	main()
