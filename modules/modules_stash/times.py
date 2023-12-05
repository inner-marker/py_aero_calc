class Plugin:
    
    name = "Multiply"
    description = "Multiplies two numbers"
    arguements = ["Num 1", "Num 1"]

    def calculate(self, *args):
        """add some numbers"""
        return float(args[0]) * float(args[1])