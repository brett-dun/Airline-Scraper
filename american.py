
from functions import *
from options import *

import subprocess
from subprocess import Popen, PIPE, STDOUT

from appscript import app, k

import time
import math

import parser

#American Airlines url
def url():
	return 'https://www.aa.com/homePage.do'

def run():
	#american airlines
	p = Popen(['open', url()], stdin=PIPE, stdout=PIPE)

	#let the website load
	time.sleep(5)


	y0 = 633

	#round trip
	if round_trip:
		x = 494
	#one way
	else:
		x = 584

	moveMouse(x, y0)
	sleepRandom()
	pygui.click(x, y0)

	sleepRandom()

	y1 = 749

	#departing location
	x = 554
	moveMouse(x, y1)
	sleepRandom()
	pygui.click(x, y1)

	sleepRandom()

	backspace(3)
	type(departing_airport)

	#arriving location
	x = 772
	moveMouse(x, y1)
	sleepRandom()
	pygui.click(x, y1)

	sleepRandom()

	backspace(3)
	type(arriving_airport)

	#number of passengers
	x = 995
	moveMouse(x, y1)
	sleepRandom()
	pygui.click(x, y1)

	sleepRandom()

	type(str(number_passangers))

	sleepRandom()

	#this may not be universal
	enter()

	sleepRandom()

	#scroll down
	pygui.scroll(-10)

	y2 = 427

	#select the departure date range
	x = 554
	moveMouse(x, y2)
	sleepRandom()
	pygui.click(x, y2)

	backspace(10)
	type(departing_date)

	sleepRandom()

	if round_trip:
		x = 772
		moveMouse(x, y2)
		sleepRandom()
		pygui.click(x, y2)

		sleepRandom()

		backspace(10)
		type(returning_date)

		sleepRandom()

	#search for flights
	x = 995
	moveMouse(x, y2)
	sleepRandom()
	pygui.click(x, y2)

	#let the new website load
	time.sleep(10)

	if round_trip:
		moveMouse(830, 715)
		sleepRandom()
		pygui.click(830, 715)

		#let the new website load
		time.sleep(10)

		pygui.hotkey('command', 'option', 'u')

		time.sleep(10)

		#click in the center of the screen
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

		with open('american_return.html', 'w') as f:
			f.write(text)
			f.close()

		#click into the view-source tab
		moveMouse(700, 400)
		sleepRandom()
		pygui.click(700, 400)

		#close the view-source tab
		pygui.hotkey('command', 'w')
		sleepRandom()

		#click into the original tab
		moveMouse(700, 400)
		sleepRandom()
		pygui.click(700, 400)

		time.sleep(2)

		pygui.hotkey('command', '[')

		time.sleep(10)

	
	pygui.hotkey('command', 'option', 'u')

	time.sleep(10)

	#click in the center of the screen
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

	with open('american_depart.html', 'w') as f:
		f.write(text)
		f.close()

	#click into the view-source tab
	moveMouse(700, 400)
	sleepRandom()
	pygui.click(700, 400)

	#close the view-source tab
	pygui.hotkey('command', 'w')
	sleepRandom()

	#click into the original tab
	moveMouse(700, 400)
	sleepRandom()
	pygui.click(700, 400)

	#close the original tab
	pygui.hotkey('command', 'w')

	print('departing flights')
	departing_flights = parser.parse('american_depart.html', 0)

	for flight in departing_flights:
		print(flight)

	if round_trip:
		print('returning flights')
		returning_flights = parser.parse('american_return.html', 1)
		lowest = math.inf
		for i in range(7, 12):
			
			for flight in returning_flights:
				if flight[i] is not None:
					if int(flight[i].split(' ')[1].replace(',','')) < lowest:
						lowest = int(flight[i].split(' ')[1].replace(',',''))

			for flight in returning_flights:
				if flight[i] is not None:
					flight[i] = '$ ' + str(int(flight[i].split(' ')[1].replace(',',''))-lowest)

		for flight in returning_flights:
			print(flight)


		

