from bs4 import BeautifulSoup
import urllib2
import smtplib


def scrape():
	search_url="http://www.surfline.com/surf-report/pleasure-point-central-california_4190/"
	search_page=urllib2.urlopen(search_url)
	soup=BeautifulSoup(search_page)

	wave_range=soup.find('h2',{'id': 'observed-wave-range'})
	wave_height=wave_range.text
	spot_conditions=soup.find('div',{'id': 'observed-spot-conditions'})
	conditions=spot_conditions.text

	
	print wave_height[:1]
	if "good" in conditions:
		return True
	if "fair" in conditions and wave_height[:1]>=3:
		return True
	return False
			



def main():
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	server.starttls()
	server.login( <your email>, <password> )
	go_surfing=scrape()

	if go_surfing:
		server.sendmail( 'Sam', <your number>@mms.att.net', 'Go surfing today!' )

	print "Message sent"

if __name__=="__main__":
	main()
