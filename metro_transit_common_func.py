import requests
import json
import metro_transit_config_file as configfile
from datetime import datetime


def get_Route(busroute):

 route = configfile.check_flag
 apiUrl = configfile.api_Url+'NexTrip/Routes?format=json'

 resp = requests.get(url=apiUrl)
 data = json.loads(resp.text)

 for routes in data:
  route_number = routes['Route']
  route_name = routes['Description']

  if busroute.lower() in route_name.lower() or route_number == busroute:
   route = routes['Route']
   return route
 return route


def get_stop(bus_stop, bus_route, direction):

	stop_Id = configfile.check_flag
	api_url = configfile.api_Url+'NexTrip/Stops/{}/{}?format=json'.format(bus_route, direction)

	resp = requests.get(url=api_url)
	data = json.loads(resp.text)

	#example of json result {'Text': 'Minnesota St and 4th St', 'Value': '4MIN'}
	for routeStop in data:
		routeText = routeStop['Text']
		routeValue = routeStop['Value']

		if bus_stop.lower() in routeText.lower():
			stop = routeValue
			return stop

	return stop_Id

def Get_Departures_Time(bus_route,direction,stop):

	depture_time = configfile.check_flag
	api_url = configfile.api_Url+'NexTrip//{}/{}/{}?format=json'.format(bus_route, direction,stop)

	resp = requests.get(url=api_url)
	data = json.loads(resp.text)

	#[] empty- means its not currently running, did not get anything from the api
	if len(data) == 0:
		return depture_time
	else:
		return data[0]['DepartureText']

def Get_Departures_Min(time):

	split = time.split(":")

	times_hour = int(split[0])
	times_minute = int(split[1])

	date = datetime.now()
	newdate = date.replace(hour=times_hour, minute=times_minute)

	time_difference = str(newdate - datetime.now())


	split2 = time_difference.split(":")
	depart_timee = int(split2[1])


	return depart_timee
