class Plugin:

    name = "Modulo"
    description = "Gives the modulo (remainder) of two Num1 divided by Num2"
    arguements = ["Num 1", "Num 1"]
    
    def calculate(self, *args):
        """add some numbers"""
        return float(args[0]) % float(args[1])