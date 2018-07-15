
#from selenium import webdriver as webdriver
#from selenium.webdriver.common.keys import Keys

from datetime import datetime as dt
from datetime import date

from functions import *
from options import *
import american

#Delta url
def delta_url():
	return 'https://www.delta.com/'
#United url
def united_url():
	return 'https://www.united.com/ual/en/us/'
#Southwest url
def southwest_url():
	return 'https://www.southwest.com/'


assert (number_passangers > 0 and number_passangers < 7), 'invalid number of passengers'

today = dt.today().strftime('%m/%d/%Y')
assert (dt.strptime(departing_date, '%m/%d/%Y') >= dt.strptime(today, '%m/%d/%Y')), 'invalid depart date'

assert ( (dt.strptime(returning_date, '%m/%d/%Y') >= dt.strptime(departing_date, '%m/%d/%Y')) or one_way ), 'invalid return date'

#for round trips, I need to have it look at one way flights for each way in order to see if there is a cheaper flight combinination by using one airline for each direction
american.run()

#it looks like doing this for delta will be very difficult due to their calendar configuration
driver = webdriver.Chrome()
driver.get(delta_url())

driver.find_element_by_xpath('//*[@id="selectTripType-val"]').click()

if round_trip:
	driver.find_element_by_xpath('//*[@id="ui-list-selectTripType0"]').click()
else:
	driver.find_element_by_xpath('//*[@id="ui-list-selectTripType1"]').click()

elem = driver.find_element_by_xpath('//*[@id="calDepartLabelCont"]/span[2]')


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


