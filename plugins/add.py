class Plugin:
    name = "Add"
    description = "Adds Num1 + Num2"
    arguements = ["Num1", "Num2"]

    def calculate(self, arguements_in, *args):
        """add some numbers"""
        return float(arguements_in[0]) + float(arguements_in[1])