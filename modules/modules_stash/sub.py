class Plugin:
    
    name = "Subtract"
    description = "Subtracts Num1 from Num2"
    arguements = ["Num 1", "Num 1"]

    def calculate(self, *args):
        """add some numbers"""
        return float(args[0]) - float(args[1])