
#from selenium import webdriver as webdriver
#from selenium.webdriver.common.keys import Keys

import subprocess
from subprocess import Popen, PIPE, STDOUT

from datetime import datetime as dt
from datetime import date

import sys
from sys import platform
import time
import random as rm

import pyautogui as pygui

from appscript import app, k

#this doesn't work on mac, maybe it will work on windows
import pyperclip

import parser

#American Airlines url
def aa_url():
	return 'https://www.aa.com/homePage.do'
#Delta url
def delta():
	return 'https://www.delta.com/'
#United url
def united():
	return 'https://www.united.com/ual/en/us/'
#Southwest url
def southwest():
	return 'https://www.southwest.com/'


def delaytime():
	return 1.5


def sleepRandom():
	time.sleep(rm.uniform(0.5, 1.5))
def type(str):
	for c in str:
		app('System Events').keystroke(c)
		time.sleep(rm.uniform(.15, .2))
def moveMouse(x, y):
	pygui.moveTo(x, y, duration=rm.uniform(0.3, 0.7))
def backspace(x):
	for i in range(x):
		pygui.hotkey('backspace')
		time.sleep(rm.uniform(.05, .15))

assert (platform == 'linux' or platform == 'linux2' or platform == 'darwin' or platform == 'win32'), 'platform not found'

if platform == 'linux' or platform == 'linux2': #linux (obviously)
	def copy():
		pygui.hotkey('ctrl', 'shift', 'c')
		time.sleep(rm.uniform(.05, .15))
	def selectAll():
		pygui.hotkey('ctrl', 'shift', 'a')
		time.sleep(rm.uniform(.05, .15))
	def enter():
		pygui.hotkey('enter')
		time.sleep(rm.uniform(.05, .15))
elif platform == 'darwin': #mac os
	def copy():
		#app('System Events').keystroke('c', using=k.command_down)
		pygui.hotkey('command', 'c')
		time.sleep(rm.uniform(.05, .15))
	def selectAll():
		#app('System Events').keystroke('a', using=k.command_down)
		pygui.hotkey('command', 'a')
		time.sleep(rm.uniform(.05, .15))
	def enter():
		pygui.hotkey('return')
		time.sleep(rm.uniform(.05, .15))
elif platform == 'win32': #windows
	def copy():
		pygui.hotkey('ctrl', 'c')
		time.sleep(rm.uniform(.05, .15))
	def selectAll():
		pygui.hotkey('ctrl', 'a')
		time.sleep(rm.uniform(.05, .15))
	def enter():
		pygui.hotkey('enter')
		time.sleep(rm.uniform(.05, .15))



#departing airport
round_trip = True
departing_airport = 'ORD' #london heathrow
arriving_airport = 'LAX' #chicago
number_passangers = 1
departing_date = '7/20/2018'
returning_date = '7/30/2018'


assert (number_passangers > 0 and number_passangers < 7), 'invalid number of passengers'

today = dt.today().strftime('%m/%d/%Y')
assert (dt.strptime(departing_date, '%m/%d/%Y') >= dt.strptime(today, '%m/%d/%Y')), 'invalid depart date'

assert ( (dt.strptime(returning_date, '%m/%d/%Y') >= dt.strptime(departing_date, '%m/%d/%Y')) or one_way ), 'invalid return date'


#american airlines
p = Popen(['open', aa_url()], stdin=PIPE, stdout=PIPE)

#let the website load
time.sleep(5)

#round trip
if round_trip:
	moveMouse(494, 633)
	sleepRandom()
	pygui.click(494, 633)
#one way
else:
	moveMouse(584, 635)
	sleepRandom()
	pygui.click(584, 635)

sleepRandom()

#departing location
moveMouse(554, 749)
sleepRandom()
pygui.click(554, 749)

sleepRandom()

backspace(3)
type(departing_airport)

#arriving location
moveMouse(772, 749)
sleepRandom()
pygui.click(772, 749)

sleepRandom()

backspace(3)
type(arriving_airport)

#number of passengers
moveMouse(995, 749)
sleepRandom()
pygui.click(995, 749)

sleepRandom()

type(str(number_passangers))

sleepRandom()

#this may not be universal
enter()

'''pygui.moveTo(995, 749, duration=rm.uniform(min(), max()))
sleepRandom()
pygui.click(995, 749)'''

sleepRandom()

#scroll down
pygui.scroll(-10)

#select the departure date range
moveMouse(554, 427)
sleepRandom()
pygui.click(554, 427)

backspace(10)
type(departing_date)

sleepRandom()

if round_trip:
	moveMouse(772, 427)
	sleepRandom()
	pygui.click(772, 427)

	sleepRandom()

	backspace(10)
	type(returning_date)

	sleepRandom()

#search for flights
moveMouse(995, 427)
sleepRandom()
pygui.click(995, 427)

#let the new website load
time.sleep(10)

'''
pygui.moveTo(660, 53, duration=rm.uniform(min(), max()))
sleepRandom()
pygui.click(660, 53)

app('System Events').keystroke('a', using=k.command_down)
#pygui.hotkey('command', 'a')
sleepRandom()
app('System Events').keystroke('c', using=k.command_down)
#pygui.hotkey('command', 'a')

url = subprocess.check_output('pbpaste', env={'LANG': 'en_US.UTF-8'}).decode('utf-8')
#url = pyperclip.paste()
print(url)
'''

time.sleep(5)

#view-source in chrome
#this is not universal
#app('System Events').keystroke('u', using=[k.command_down, k.option_down])
pygui.hotkey('command', 'option', 'u')

time.sleep(10)

moveMouse(700, 400)
sleepRandom()
pygui.click(700, 400)


selectAll()

sleepRandom()

copy()

time.sleep(2)

#html from webpage
#this is a Mac OS Specific Command (I think)
html = subprocess.check_output('pbpaste', env={'Lang': 'en_US.UTF-8'})

text = ''
for c in html:
	try:
		text += str(chr(c))
	except:
		text += ' '

with open('scraper4.html', 'w') as f:
	f.write(text)
	f.close()

moveMouse(700, 400)
sleepRandom()
pygui.click(700, 400)

pygui.hotkey('command', 'w')
sleepRandom()

moveMouse(700, 400)
sleepRandom()
pygui.click(700, 400)

pygui.hotkey('command', 'w')
sleepRandom()

parser.parse()

#start by parsing this html


#they really don't like selenium
'''
driver = webdriver.Chrome()
driver.get(url)

#wait for website to load
time.sleep(2)

flight = 1
while True:
	try:
		elem = driver.find_element_by_xpath('//*[@id="slice0Flight' + str(flight) + '"]')
		print()
		print(elem.get_attribute('innerHTML'))
		flight += 1
	except:
		break
'''

#//*[@id="flight0SeatsLink"]
#//*[@id="flight1SeatsLink"]

#American Airline's Website detects and blocks selenium, RIP
'''#check the aa website
driver = webdriver.Chrome()
driver.get(aa())


#driver.find_element_by_xpath('//*[@id="advBookingSearch"]').click()
#driver.find_element_by_xpath('//*[@id="reservationFlightSearchForm"]/input[3]').click()

#rewrite all of this to use the 'advanced search' option

attempts = 0
while attempts < 5:

	try:

		#select one way or round trip
		if one_way:
			driver.find_element_by_xpath('//*[@id="flightSearchForm.tripType.oneWay"]').click()
		#else:
		#	driver.find_element_by_xpath('//*[@id="flightSearchForm.tripType.roundTrip"]').click()

		time.sleep(delaytime())

		#type in the airport that we will be departing from
		elem = driver.find_element_by_xpath('//*[@id="reservationFlightSearchForm.originAirport"]')
		elem.clear()
		elem.send_keys(departing_airport)

		time.sleep(delaytime())

		#type in the airport that we will be landing at
		elem = driver.find_element_by_xpath('//*[@id="reservationFlightSearchForm.destinationAirport"]')
		elem.clear()
		elem.send_keys(arriving_airport)

		time.sleep(delaytime())

		#select passanger count
		driver.find_element_by_xpath('//*[@id="flightSearchForm.adultOrSeniorPassengerCount"]').click()

		time.sleep(delaytime())

		#select the number of passangers (1-6)
		driver.find_element_by_xpath('//*[@id="flightSearchForm.adultOrSeniorPassengerCount"]/option[' + str(number_passangers) + ']').click()

		time.sleep(delaytime())

		#type in the date that we want to leave on
		elem = driver.find_element_by_xpath('//*[@id="aa-leavingOn"]')
		elem.clear()
		elem.send_keys(departing_date)

		time.sleep(delaytime())

		#if this is a round trip flight, type in the date we want to return on
		if not one_way:
			elem = driver.find_element_by_xpath('//*[@id="aa-returningFrom"]')
			elem.clear()
			elem.send_keys(returning_date)

		time.sleep(delaytime())

		driver.refresh()

		#click submit
		driver.find_element_by_xpath('//*[@id="flightSearchForm.button.reSubmit"]').click()

		time.sleep(delaytime())

		#https://www.delta.com/flight-search/search?action=findFlights&tripType=ONE_WAY&priceSchedule=PRICE&originCity=CHI&destinationCity=MSP&departureDate=07%2F14%2F2018&departureTime=AT&returnDate=&returnTime=&paxCount=1&searchByCabin=true&cabinFareClass=BE&deltaOnlySearch=false&deltaOnly=off&Go=Find%20Flights&meetingEventCode=&refundableFlightsOnly=false&compareAirport=false&awardTravel=false&datesFlexible=false&flexAirport=false&paxCounts%5B0%5D=1

		break

	except:

		print('FAILURE (trying again)')
		attempts += 1
'''


