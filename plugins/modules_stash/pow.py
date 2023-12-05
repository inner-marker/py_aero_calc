class Plugin:
    
    name = "Power"
    description = "Returns the power of Num1 to the power of Num2"
    arguements = ["Num 1", "Num 1"]

    def calculate(self, *args):
        """add some numbers"""
        return float(args[0]) ** float(args[1])