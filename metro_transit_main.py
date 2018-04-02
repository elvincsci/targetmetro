import sys
import metro_transit_common_func as commonFunc
import metro_transit_config_file as configfile




def main():
    #arg 1 = “BUS ROUTE”
    #arg 2 = “BUS STOP NAME”
    #arg 3 = “DIRECTION”
    if len(sys.argv) != 4:
        print("Three argument required to run, ", len(sys.argv), " were passed" )
        exit(0)

    route_Number = commonFunc.get_Route(sys.argv[1])

    if route_Number == 0:
        print("Unable to find the provided route:", sys.argv[1])
        print("Please check the name, this may mean the last bus for the day has already left)")
        exit(0)

    direction = sys.argv[3]

    if direction.lower() == "east":
        direction = configfile.East
    elif direction.lower() == "west":
        direction = configfile.West
    elif direction.lower() == "south":
        direction = configfile.South
    elif direction.lower() == "north":
        direction = configfile.North
    else:
        print("Check the direction please", direction)
        exit(0)

    get_stop = commonFunc.get_stop(sys.argv[2],route_Number,direction)

    if get_stop == 0:
        print("Unable to find the BUS STOP NAME", sys.argv[2])
        exit(0)

    dept_time = commonFunc.Get_Departures_Time(route_Number,direction,get_stop)


    if dept_time == 0:
        print("Transport is not currently running, please check back later")
    elif dept_time.lower() == "due":
        print("Metro transit transport is due")
    else:
        if "Min" in dept_time:
            split = dept_time.split(" ")
            print(split[0], "Minutes")
        else:
            print(commonFunc.Get_Departures_Min(dept_time), "Minutes")

main()