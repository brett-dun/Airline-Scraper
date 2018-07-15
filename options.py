
#options for searching for flights initially
round_trip = True
departing_airport = 'ORD'
arriving_airport = 'SAN'
number_passangers = 2
#note: same day round trips are not reliable (yet)
departing_date = '8/1/2018' #8/27/2018'
returning_date = '8/7/2018'

#options for sorting flights
allow_connections = False
allow_basic = False
allowed_cabins = ['economy, economy_plus, business, first']
preferred_departure_time = ['12:00 pm', '4:00 pm']
acceptable_departure_time = ['9:00 am', '7:00pm']
preferred_return_time = ['12:00 pm', '4:00 pm']
acceptable_return_time = ['9:00 am', '7:00pm']
maximum_price = 500
mimimize = 'price' #'time'