######## Constants

class Conversions:
    def __init__(self) -> None:
        self.KILOMETERS_PER_NAUTICAL_MILE = 1.852
        self.METERS_PER_NAUTICAL_MILE = 1852
        self.MILES_PER_NAUTICAL_MILE = 1.15078
        self.YARDS_PER_NAUTICAL_MILE = 2025.37
        self.FEET_PER_NAUTICAL_MILE = 6076.12
        self.INCHES_PER_NAUTICAL_MILE = 72913.4
        
        self.NAUTICAL_MILES_PER_KILOMETER = 0.539957
        self.MILES_PER_KILOMETER = 0.621371
        self.YARDS_PER_KILOMETER = 1093.61
        self.MILES_PER_KILOMETER = 3280.84
        
        self.KILOMETERS_PER_MILE = 1.60934
        self.METERS_PER_MILE = 1609.34
        self.NAUTICAL_MILES_PER_MILE = 0.868976
        self.YARDS_PER_MILE = 1760
        self.FEET_PER_MILE = 5280
        self.INCHES_PER_MILE = 63360
        
        @staticmethod
        def conv_distance(value, *args, **kwargs):
            """Convert distance units

            Args:
                value (float): input value

            kwargs:
                value_unit (str): abbreviations per README
                output_unit (str): abbreviations per README
            
            Returns:
                float: output value in new unit
            """            
            output = 0.0
            return output
        
        
        
        
        