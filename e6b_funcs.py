from constants import Constants

############################################################
# Calculation functions
############################################################

def calc_groundspeed (distance, time, **kwargs):
    """calculate grounud speed in knots

    Args:
        distance_nm (float): distance in nautical miles
        hours (float): hours to travel the distance
        **kwargs: keyword arguements
        
    kwargs: (first value is the default)
    distance_unit = 'nm', 'sm', 'km'
    time_unit = 'hours', 'minutes', 'seconds'
    groundspeed_unit = 'knots', 'mph', 'kph'

    Returns:
        float: ground speed in knots
    """ 
    
    C = Constants()
    
    distance_nm = 0
    time_hours = 0
    groundspeed_knots = 0
    groundspeed_output = 0
    
    # process the distance variable
    if kwargs['distance_unit'] == "nm":
        distance_nm = distance
    elif kwargs['distance_unit'] == "sm":
        distance_nm = distance * C.NAUTICAL_MILES_PER_MILE
    elif kwargs['distance_unit'] == "km":
        distance_nm = distance * C.NAUTICAL_MILES_PER_KILOMETER
    else:
        print("Invalid distance unit arguement: ", kwargs['distance_unit'])
        
    # process the time variable
    if kwargs['time_unit'] == "hours":
        time_hours = time
    elif kwargs['time_unit'] == "minutes":
        time_hours = time / 60
    elif kwargs['time_unit'] == "seconds":
        time_hours = time / 3600
    else:
        print("Invalid time unit arguement: ", kwargs['time_unit'])
        
    try:
        groundspeed_knots = distance_nm / time_hours
    except:
        print('possible divide by zero error')
        
    # process the groundspeed_output variable
    if kwargs['groundspeed_unit'] == "knots":
        groundspeed_output = groundspeed_knots
    elif kwargs['groundspeed_unit'] == "mph":
        groundspeed_output = groundspeed_knots * C.MILES_PER_NAUTICAL_MILE
    elif kwargs['groundspeed_unit'] == "kph":
        groundspeed_output = groundspeed_knots * C.KILOMETERS_PER_NAUTICAL_MILE
    else:
        print("Invalid groundspeed unit arguement: ", kwargs['groundspeed_unit'])
        
    return groundspeed_output

############################################################
# User interaction functions
############################################################

def userio_groundspeed_knots ():
    """User IO to calculate ground speed in knots
    """    
    
    # Create the variables
    user_distance_nautical_miles = 0
    user_time = 0
    groundspeed_knots = 0
    user_time_unit = "hours"
    
    # Get the values
    user_distance_nautical_miles = float(input('Distance (nm):    '))
    user_time =                    float(input('Time (decimal):  '))
    user_time_unit = input("Time Unit ('hours', 'minutes'): ")
    # Calculat the result
    groundspeed_knots = calc_groundspeed(user_distance_nautical_miles,user_time, time_unit=user_time_unit)
    
    # Print the result
    print("Ground Speed (knots): ", "{:.1f}".format(groundspeed_knots))

############################################################
# Main functions
############################################################

def main ():
    """Main method.
    
    Call all of the user io functions from here.
    """    
    # print('hello world!')
    userio_groundspeed_knots()

if __name__ == '__main__':
    """dunder main
    """    
    main()