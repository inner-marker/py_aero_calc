############################################################
# Calculation functions
############################################################

def calc_groundspeed_knots (distance_nm, time, time_unit = "hours"):
    """calculate grounud speed in knots

    Args:
        distance_nm (float): distance in nautical miles
        hours (float): hours to travel the distance
        time_unit (Str): Time unit. "hours" (default), "minutes"

    Returns:
        float: ground speed in knots
    """ 
    
    groundspeed_knots = 0
    time_hours = 0
    
    # process the time variable
    if time_unit == "minutes":
        time_hours = time / 60
    else:
        time_hours = time
        
    try:
        groundspeed_knots = distance_nm / time_hours
    except:
        print('possible divide by zero error')
    return groundspeed_knots

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
    groundspeed_knots = calc_groundspeed_knots(user_distance_nautical_miles,user_time, time_unit=user_time_unit)
    
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