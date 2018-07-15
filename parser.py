
from selenium import webdriver as webdriver
from selenium.webdriver.common.keys import Keys

import re

import sys

def parse(file, x):

	driver = webdriver.Chrome()
	#make this cross platform
	driver.get('file://' + sys.path[0] + '/' + file)

	price_finder = re.compile(r'\$\s[0-9]*(,)?[0-9][0-9]([0-9])?')

	count = 1
	flights = []
	while True:
		try:
			depart_time = driver.find_element_by_xpath('//*[@id="slice' + str(x) + 'Flight' + str(count) + '"]/div/div[1]/div/div[2]/div[1]/span').text
			#//*[@id="slice1Flight1"]/div/div[1]/div/div[2]/div[1]/span
			arrive_time = driver.find_element_by_xpath('//*[@id="slice' + str(x) + 'Flight' + str(count) + '"]/div/div[1]/div/div[2]/div[3]/span').text
			flight_duration = driver.find_element_by_xpath('//*[@id="slice' + str(x) + 'Flight' + str(count) + '"]/div/div[1]/div/div[2]/div[4]/div').text
			nonstop = driver.find_element_by_xpath('//*[@id="slice' + str(x) + 'Flight' + str(count) + '"]/div/div[1]/div/div[2]/div[5]/div').text.lower() == 'nonstop'
			flight_number = driver.find_element_by_xpath('//*[@id="slice' + str(x) + 'Flight' + str(count) + '"]/div/div[1]/div/div[4]/div/span[1]').text
			plane_type = driver.find_element_by_xpath('//*[@id="slice' + str(x) + 'Flight' + str(count) + '"]/div/div[1]/div/div[4]/div/span[3]').text
			wifi_onboard = driver.find_element_by_xpath('//*[@id="slice' + str(x) + 'Flight' + str(count) + '"]/div/div[1]/div/div[4]/div/span[5]').text.lower() == 'wifi on-board'

			try:
				basic = re.search(price_finder, driver.find_element_by_xpath('//*[@id="slice' + str(x) + 'Flight' + str(count) + 'BasicEconomy"]').text).group()
			except Exception as e1:
				#print(e1)
				basic = None

			try:
				economy = re.search(price_finder, driver.find_element_by_xpath('//*[@id="slice' + str(x) + 'Flight' + str(count) + 'MainCabin"]').text).group()
			except Exception as e1:
				#print(e1)
				economy = None

			try:
				economy_plus = re.search(price_finder, driver.find_element_by_xpath('//*[@id="slice' + str(x) + 'Flight' + str(count) + 'PremiumEconomy"]')).group()
			except Exception as e1:
				#print(e1)
				economy_plus = None

			try:
				business = re.search(price_finder, driver.find_element_by_xpath('//*[@id="slice' + str(x) + 'Flight' + str(count) + 'Business"]').text).group()
			except Exception as e1:
				#print(e1)
				business = None
			
			try:
				first = re.search(price_finder, driver.find_element_by_xpath('//*[@id="slice' + str(x) + 'Flight' + str(count) + 'First"]').text).group()
			except Exception as e1:
				#print(e1)
				first = None

			flights.append([depart_time, arrive_time, flight_duration, nonstop, flight_number, plane_type, wifi_onboard, basic, economy, economy_plus, business, first])

		except Exception as e:
			#print(e)
			break
		count += 1

	#for flight in flights:
	#	print(flight)

	driver.close()

	return flights

