import e6b_funcs as e6b


############################################################
# User interaction functions
############################################################

def userio_groundspeed_knots ():
    """User IO to calculate ground speed in knots
    """    
    
    # Create the variables
    user_distance = 0
    user_distance_unit = "nm"
    user_time = 0
    user_time_unit = "hours"
    groundspeed = 0
    user_groundspeed_unit = 'knots'
        
    # Get the values
    user_distance =         float(input('Distance: '))
    user_distance_unit =          input("Distance Unit (nm, sm, km): ")
    user_time =             float(input('Time: '))
    user_time_unit =              input("Time Unit (hours, minutes, seconds): ")
    user_groundspeed_unit =              input("Groundspeed Unit (knots, mph, kph): ")
    
    # Calculat the result
    groundspeed = e6b.calc_groundspeed(user_distance,user_time, time_unit=user_time_unit, distance_unit = user_distance_unit, groundspeed_unit=user_groundspeed_unit)
    
    # Print the result
    print(f"Ground Speed ({user_groundspeed_unit}): ", "{:.1f}".format(groundspeed))
    
    
############################################################
# Main functions
############################################################

def main ():
    """Main method.
    
    Call all of the user io functions from here.
    """    

    # groundspeed
    userio_groundspeed_knots()
    
    
if __name__ == '__main__':
    """dunder main
    """    
    main()