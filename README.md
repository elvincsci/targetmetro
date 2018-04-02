
This Python script is used to get the amount of time in minute until the next bus or train leaves a given bus stop, using the leverage Metro transit API at http://svc.metrotransit.org/.

Script files
This script is make up of three files: metro_transit_main.py, metro_transit_config_file.py and metro_transit_common_func.py. In order to run the script metro_transit_main.py and pass in
three arguments, BUS ROUTE, BUS STOP NAME and DIRECTION

“BUS ROUTE” will be a substring of the bus route name which is only in one bus
route
“BUS STOP NAME” will be a substring of the bus stop name which is only in one bus
stop on that route
“DIRECTION” will be “north” “east” “west” or “south”

example of command
$ metro_transit_main.py “METRO Blue Line” “Target Field Station Platform 1” “south”

Provided the correct input the script will return the minutes until the bus leaves the specified bus or train stop
example: 8 Minutes