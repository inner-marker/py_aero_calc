# Modules Specification

All modules must contain certain elements. The basic structure of the module is here:

```python
class Module:
    name = "Module Name"
    description = "This is a description of the module, perhapse talking about what it does with the arguements."
    #list of arguements over which main.py will loop to get value inputs from the user.
    arguements = ["Num1", "Num2"]

    def calculate(self, arguements_in, *args):
        """Do something with the arguements."""

        # some logic to compute a result
        result = 1

        #return the result
        return result
```