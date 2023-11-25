from conversions import Conversions

############################################################
# Calculation functions
############################################################

def calc_groundspeed (distance, time, **kwargs):
    """calculate grounud speed in knots.
    By default, this function divides distance by time. You can specify the units for distance, time and the groundspeed output using the kwargs.

    Args:
        distance_nm (float): distance in nautical miles
        hours (float): hours to travel the distance
        **kwargs: keyword arguements
        
    kwargs: (first value is the default)
        distance_unit (str): nm, sm, km
        time_unit (str): hours, minutes, seconds
        groundspeed_unit (str): knots, mph, kph

    Returns:
        float: ground speed in specified unit or knots
    """ 
    
    C = Conversions()
    
    distance_nm = 0
    time_hours = 0
    groundspeed_knots = 0
    groundspeed_output = 0
    
    # process the distance variable
    if 'distance_unit' in kwargs and kwargs['distance_unit'] == "nm":
        distance_nm = distance
    elif 'distance_unit' in kwargs and kwargs['distance_unit'] == "sm":
        distance_nm = distance * C.NAUTICAL_MILES_PER_MILE
    elif 'distance_unit' in kwargs and kwargs['distance_unit'] == "km":
        distance_nm = distance * C.NAUTICAL_MILES_PER_KILOMETER
    elif 'distance_unit' in kwargs:
        print("Invalid distance unit arguement: ", kwargs['distance_unit'])
    else:
        distance_nm = distance
        
    # process the time variable
    if 'time_unit' in kwargs and kwargs['time_unit'] == "hours":
        time_hours = time
    elif 'time_unit' in kwargs and kwargs['time_unit'] == "minutes":
        time_hours = time / 60
    elif 'time_unit' in kwargs and kwargs['time_unit'] == "seconds":
        time_hours = time / 3600
    elif 'time_unit' in kwargs:
        print("Invalid time unit arguement: ", kwargs['time_unit'])
    else:
        time_hours = time
        
    try:
        groundspeed_knots = distance_nm / time_hours
    except:
        print('possible divide by zero error')
        
    # process the groundspeed_output variable
    if 'groundspeed_unit' in kwargs and kwargs['groundspeed_unit'] == "knots":
        groundspeed_output = groundspeed_knots
    elif 'groundspeed_unit' in kwargs and kwargs['groundspeed_unit'] == "mph":
        groundspeed_output = groundspeed_knots * C.MILES_PER_NAUTICAL_MILE
    elif 'groundspeed_unit' in kwargs and kwargs['groundspeed_unit'] == "kph":
        groundspeed_output = groundspeed_knots * C.KILOMETERS_PER_NAUTICAL_MILE
    elif 'groundspeed_unit' in kwargs:
        print("Invalid groundspeed unit arguement: ", kwargs['groundspeed_unit'])
    else:
        groundspeed_output = groundspeed_knots
        
    return groundspeed_output



############################################################
# Main functions for testing
############################################################

def main ():
    """Main method.
    
    Call all of the user io functions from here.
    """    
    # print('hello world!')
    print("Groundspeed: ", calc_groundspeed(450,30))

if __name__ == '__main__':
    """dunder main
    """    
    main()