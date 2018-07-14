
'''with open('scraper2.html', 'r') as f:

	html = f.read()
	useful = html.split('<ul class="search-results-normal js-forsort">')[1].split('<li id="slice0Flight')#('<div class="row flight-matrix">')

	print(useful)
'''

#//*[@id="slice0Flight4BasicEconomy"]

from selenium import webdriver as webdriver
from selenium.webdriver.common.keys import Keys

import re

import sys

def parse():

	driver = webdriver.Chrome()
	driver.get('file://' + sys.path[0] + '/scraper4.html')

	price_finder = re.compile(r'\$\s[0-9]*(,)?[0-9][0-9]([0-9])?')

	count = 1
	flights = []
	while True:
		try:
			depart_time = driver.find_element_by_xpath('//*[@id="slice0Flight' + str(count) + '"]/div/div[1]/div/div[2]/div[1]/span').text
			arrive_time = driver.find_element_by_xpath('//*[@id="slice0Flight' + str(count) + '"]/div/div[1]/div/div[2]/div[3]/span').text
			flight_duration = driver.find_element_by_xpath('//*[@id="slice0Flight' + str(count) + '"]/div/div[1]/div/div[2]/div[4]/div').text
			nonstop = driver.find_element_by_xpath('//*[@id="slice0Flight' + str(count) + '"]/div/div[1]/div/div[2]/div[5]/div').text.lower() == 'nonstop'
			flight_number = driver.find_element_by_xpath('//*[@id="slice0Flight' + str(count) + '"]/div/div[1]/div/div[4]/div/span[1]').text
			plane_type = driver.find_element_by_xpath('//*[@id="slice0Flight' + str(count) + '"]/div/div[1]/div/div[4]/div/span[3]').text
			wifi_onboard = driver.find_element_by_xpath('//*[@id="slice0Flight' + str(count) + '"]/div/div[1]/div/div[4]/div/span[5]').text.lower() == 'wifi on-board'

			try:
				basic_price = re.search(price_finder, driver.find_element_by_xpath('//*[@id="slice0Flight' + str(count) + 'BasicEconomy"]').text).group()
			except Exception as e1:
				#print(e1)
				basic_price = None

			try:
				economy = re.search(price_finder, driver.find_element_by_xpath('//*[@id="slice0Flight' + str(count) + 'MainCabin"]').text).group()
			except Exception as e1:
				#print(e1)
				economy = None

			try:
				economy_plus = re.search(price_finder, driver.find_element_by_xpath('//*[@id="slice0Flight' + str(count) + 'PremiumEconomy"]')).group()
			except Exception as e1:
				#print(e1)
				economy_plus = None

			try:
				business = re.search(price_finder, driver.find_element_by_xpath('//*[@id="slice0Flight' + str(count) + 'Business"]').text).group()
			except Exception as e1:
				#print(e1)
				business = None
			
			try:
				first = re.search(price_finder, driver.find_element_by_xpath('//*[@id="slice0Flight' + str(count) + 'First"]').text).group()
			except Exception as e1:
				#print(e1)
				first = None

			#print('depart: ' + depart_time + '; arrive: ' + arrive_time + '; flight duration: ' + flight_duration + '; nonstop: ' + str(nonstop) + '; flight number: ' + flight_number + '; plane: ' + plane_type + '; onboard wifi: ' + str(wifi_onboard))
			flights.append((depart_time, arrive_time, flight_duration, nonstop, flight_number, plane_type, wifi_onboard, basic_price, economy, economy_plus, business, first))

		except Exception as e:
			print(e)
			break
		count += 1

	for flight in flights:
		print(flight)

	driver.close()

