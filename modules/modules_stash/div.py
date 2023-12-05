class Plugin:

    name = "Divide"
    description = "Divides Num1 by Num2"
    arguements = ["Num 1", "Num 1"]
    
    def calculate(self, arguements_in, *args):
        """add some numbers"""
        return float(args[0]) / float(args[1])