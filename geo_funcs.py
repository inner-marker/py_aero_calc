#geo utilities

import math

RADIUS = 6371000 #mean radius of earth in meters

def distance_greatcircle (lat1, lon1, lat2, lon2):
    """find the distance between two points using earth great circle, assuming a spherical earth.

    Args:
        lat1 (float): lat/lon in decimal degrees
        lon1 (float): lat/lon in decimal degrees
        lat2 (float): lat/lon in decimal degrees
        lon2 (float): lat/lon in decimal degrees

    Returns:
        float: great circle distance in nautical miles
    """    
    #convert decimal degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)
    
    #find the change in lat and lon from the start point (1)
    lat_delta_rad = lat2_rad - lat1_rad
    lon_delta_rad = lon2_rad - lon1_rad
    
    a = math.sin(lat_delta_rad/2) * math.sin(lat_delta_rad/2) + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(lon_delta_rad/2) * math.sin(lon_delta_rad/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))

    d_meters = RADIUS * c #in metres
    
    #convert to nautical miles
    d_nm = d_meters * 0.000539957
    
    return d_nm
    
    
#find the initial bearing along a great circle arc between two lat/lon points
#INPUT: pair of lat/lon points in decimal degrees
#:OUTPUT: bearing in decimal degrees from true north
def bearing_initial_greatcircle ( lat1, lon1, lat2, lon2 ):
    #convert decimal degrees to radians
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    y = math.sin(lon2_rad-lon1_rad) * math.cos(lat2_rad)
    x = math.cos(lat1_rad)*math.sin(lat2_rad) - math.sin(lat1_rad)*math.cos(lat2_rad)*math.cos(lon2_rad-lon1_rad)
    theta = math.atan2(y, x)
    brng = ( theta * 180 / math.pi + 360) % 360 # in degrees
    return brng

#find the initial bearing along a great circle arc between two lat/lon points
#INPUT: pair of lat/lon points in decimal degrees
#:OUTPUT: bearing in decimal degrees from true north
def bearing_final_greatcircle ( lat1, lon1, lat2, lon2 ):
    brng = bearing_initial_greatcircle (lat2, lon2, lat1, lon1)
    
    #brng is currently the bearing from point 2 to point 1, we need the reciprocal to represent the final bearing
    brng_out = (brng + 180) % 360
    return brng_out

#find the initial bearing along a great circle arc between two lat/lon points
#INPUT: lat/lon points in decimal degrees, 
#       bearing in decimal degrees true north, 
#       distance in nautical miles
#:OUTPUT: lat/lon in decimal degrees as a list
def point_bearing_distance (lat1_deg, lon1_deg, bearing_deg, distance_nm):
    #convert input distance (nautical miles) to meters
    distance = distance_nm * 1852
    
    #convert decimal degrees to radians
    lat1_rad = math.radians(lat1_deg)
    lon1_rad = math.radians(lon1_deg)
    bearing_rad = math.radians(bearing_deg)
    #meann radius of the earth
    
    lat2_rad = math.asin( math.sin(lat1_rad)*math.cos(distance/RADIUS) + math.cos(lat1_rad)*math.sin(distance/RADIUS)*math.cos(bearing_rad) )
    lon2_rad = lon1_rad + math.atan2(math.sin(bearing_rad)*math.sin(distance/RADIUS)*math.cos(lat1_rad), math.cos(distance/RADIUS)-math.sin(lat1_rad)*math.sin(lat2_rad))
    
    lat2_deg = math.degrees(lat2_rad)
    lon2_deg = math.degrees(lon2_rad)
    
    return lat2_deg, lon2_deg

#find the midpoint of a circular arc on the surface of the earth
#INPUT: three lat/lon pairs in decimal degrees for start/end/center points
#       direction of rotation (True=CW, False=CCW)
#OUTPUT: lat/lon center point in decimal degrees
def circular_arc_midpoint (lat1_deg, lon1_deg, lat2_deg, lon2_deg, latctr_deg, lonctr_deg, direction):
    
    #find bearing FROM center TO 1
    bearing1 = bearing_initial_greatcircle (latctr_deg, lonctr_deg, lat1_deg, lon1_deg)
    #find bearing FROM center TO 2
    bearing2 = bearing_initial_greatcircle (latctr_deg, lonctr_deg, lat2_deg, lon2_deg)
    
    bearing_delta = 0
    #find the mid-bearing accounting for direction
    if direction:
        bearing_delta = (bearing2 - bearing1) % 360
    else:
        bearing_delta = -((bearing1 + 360 - bearing2) % 360)
    mid_bearing = (bearing1 + (bearing_delta / 2)) % 360
    
    distance = distance_greatcircle (latctr_deg, lonctr_deg, lat1_deg, lon1_deg)
    
    mid_point = point_bearing_distance (latctr_deg, lonctr_deg, mid_bearing, distance)
    
    return mid_point

#find the midpoint of a circular arc on the surface of the earth
#INPUT: center and bezier handle lat/lon pairs in decimal degrees
#OUTPUT: lat/lon of opposite bezier handle in decimal degrees
def bezier_opposite_handle (ctr_lat, ctr_lon, bez_lat, bez_lon):
    brg_ctr_to_bez = bearing_initial_greatcircle (ctr_lat, ctr_lon, bez_lat, bez_lon)
    dist_ctr_to_bez = distance_greatcircle (ctr_lat, ctr_lon, bez_lat, bez_lon)
    brg_ctr_to_bez2 = (brg_ctr_to_bez + 180) % 360
    bez2 = point_bearing_distance (ctr_lat, ctr_lon, brg_ctr_to_bez2, dist_ctr_to_bez)
    return bez2


# #test variables
# lat_in_1 = 76.586419	
# lon_in_1 = -068.467528
# lat_in_2 = 76.523094
# lon_in_2 = -068.290206
# lat_in_ctr = 76.566667
# lon_in_ctr = -068.300000
# cw = True

# bearing = 45
# distance = 156

# #test methods
# #print(str( bearing_initial_greatcircle( lat_in_1,lon_in_1,lat_in_2,lon_in_2) ))
# #print(str( bearing_final_greatcircle( lat_in_1,lon_in_1,lat_in_2,lon_in_2) ))
# print(str(circular_arc_midpoint( lat_in_1,lon_in_1,lat_in_2,lon_in_2,lat_in_ctr,lon_in_ctr,cw)))


