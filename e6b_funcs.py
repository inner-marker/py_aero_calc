############################################################
# Calculation functions
############################################################

def calc_groundspeed_knots (distance_nm, hours):
    """calculate grounud speed in knots

    Args:
        distance_nm (float): distance in nautical miles
        hours (float): hours to travel the distance

    Returns:
        float: ground speed in knots
    """ 
    
    groundspeed_knots = 0
    try:
        groundspeed_knots = distance_nm / hours
    except:
        print('possible divide by zero error')
    return groundspeed_knots

############################################################
# User interaction functions
############################################################

def userio_groundspeed_knots ():
    """User IO to calculate ground speed in knots
    """    
    user_distance_nautical_miles = 0
    user_hours = 0
    groundspeed_knots = 0
    user_distance_nautical_miles = float(input('Distance (nm):    '))
    user_hours =                   float(input('Hours (decimal):  '))
    groundspeed_knots = calc_groundspeed_knots(user_distance_nautical_miles,user_hours)
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