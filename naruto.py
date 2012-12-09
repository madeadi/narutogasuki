from bs4 import BeautifulSoup
from hoiio import Hoiio

import urllib2
import re
import time

Hoiio.init('YOUR_APP_ID', 'YOUR_ACCESS_TOKEN')

url="http://www.mangareader.net/93/naruto.html"
origin_url = "http://www.mangareader.net"
page=urllib2.urlopen(url)
soup = BeautifulSoup(page.read())

latest = '/naruto/611'

while True:
	for link in soup.find_all(href=re.compile('naruto'), limit = 1):
		published = link.get('href')
		if(published != latest):
			#call hoiio API
			print("New Naruto: " + origin_url + published)
			res = Hoiio.sms.bulk_send("New Naruto: " + origin_url + published, 
				'+651111111',	#user 1
				'+651111112',	#user 2
				'',
				'', 								
				notify_url = ''
				)
				print res.bulk_txn_ref
				latest = published
			else:
				print 'No new Naruto'
time.sleep(900)