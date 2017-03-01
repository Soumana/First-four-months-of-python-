'''This program will ask the user to enter the number of locations for which WCT will be calculated,
and the decimal precision to be used when reporting numbers.
Thereafter, it will query the name, air temperature, and wind velocity for each location.
For each location, the program will compute WCT using the formula of the National Weather Service,
outputting this data in the desired precision.
Lastly, the program will report various summary metrics about the locations for which it was given data.'''


print("==> Windchill Temperature (WCT) Weather Report calculator <==")
user_locations = int(input("Enter the number of locations for which (WCT) will be calculated: "))
if user_locations <= 0:
    print("Error:", user_locations, "is not a valid input.")
    exit(-1)
user_decimal_precision = eval(input("Select decimal precision for the report [1--4]: "))
if user_decimal_precision < 1 or user_decimal_precision > 4:
    print("Error:", user_decimal_precision, "is not in the range 1--4.")
    exit(-1)

wct_sum = 0
air_temp_sum = 0
wind_velocity_sum = 0

lowest_wtc_number = 300
lowest_wtc_name = ""

lowest_air_temp_number = 300
lowest_air_temp_name = ""

highest_wind_number = 0
highest_wind_name = ""

for i in range(1, user_locations + 1):
    location_name = input("Enter name of ** Location " + str(i) + " **: ")
    air_temp = eval(input('\tEnter air temperature [in deg F]: '))
    if air_temp < lowest_air_temp_number:
        lowest_air_temp_number = float(air_temp)
        lowest_air_temp_name = location_name
    wind_velocity = eval(input('\tEnter wind velocity [in mph]: '))
    if wind_velocity > highest_wind_number:
        highest_wind_number = float(wind_velocity)
        highest_wind_name = location_name
    pre_round = 35.74 + 0.6215*air_temp - 35.75*(wind_velocity**0.16) + 0.4275*air_temp*(wind_velocity**0.16)
    rounded_wct_number = round(pre_round, user_decimal_precision)
    if rounded_wct_number < lowest_wtc_number:
        lowest_wtc_number = float(rounded_wct_number)
        lowest_wtc_name = location_name
    wct_sum = wct_sum + rounded_wct_number
    air_temp_sum = air_temp_sum + air_temp
    wind_velocity_sum = wind_velocity_sum + wind_velocity
    print('\tWCT is',rounded_wct_number, 'deg F.')








pre_round_wct_avg = wct_sum / user_locations
rounded_wct_avg = round(pre_round_wct_avg,user_decimal_precision)
air_temp_avg = air_temp_sum / user_locations
wind_velocity_avg = wind_velocity_sum / user_locations

print()
print("*** Summary ***")

print("WCT")
print('\tAvg recorded WCT:',rounded_wct_avg, 'deg', 'F')
print('\tLocation with lowest WCT:', lowest_wtc_name, '(' + str(lowest_wtc_number) + ')')

print("Air Temperature")
print('\tAvg recorded air temperature:', air_temp_avg, 'deg', 'F')
print('\tLocation with lowest air temperature:', lowest_air_temp_name, '(' + str(lowest_air_temp_number) + ')', 'F')

print("Wind Velocities")
print('\tAvg recorded wind velocity:', wind_velocity_avg, 'mph')
print('\tLocation with highest wind velocity:', highest_wind_name, '(' + str(highest_wind_number) + ')', 'mph')


