#######################################################
# The main user IO file for accessing E6B functions.
#######################################################

# imports
import importlib, os, re, sys

# Constants
MODULES_DIRECTORY = './plugins'
#add system path to the plugins directory to make this more universal
sys.path.append(MODULES_DIRECTORY)

# GLOBAL VARIABLES
modules = {}

def load_modules():
    print ("Loading Modules...")
    
    counter = 1
    for plugin_file in sorted(os.listdir(MODULES_DIRECTORY)):
        if re.search('\.py$', plugin_file):
            module_name = re.sub('\.py$', '', plugin_file)
            module = importlib.import_module(module_name)
            modules[counter] = module.Plugin()
            # print ("   %s" % ( module_name ))
            counter += 1
    
    print ("Modules Loaded: ", len(modules))
    


def list_modules():
    """Prints a numbered list of modules
    """
    print('Available Modules:')
    for plugink, pluginv in modules.items():
        print(f'{plugink}: {pluginv.name}')
    print(f"")
    
    
def run_module(module_number: int):
    """Run one module until the user says they do not want to run it again.

    Args:
        module_number (int): Number of the module from the list.
    """    
    run_again = True
    
    #loop while the user wants to keep using this module
    while run_again:
        #print the name and description of the module
        print(f"\nModule Name:        {modules[module_number].name}")
        print(f"Module Description: {modules[module_number].description}\n")
        
        #get user inputs for all of the arguements
        arguments_input = []
        for arg in modules[module_number].arguements:
            arguments_input.append(input(f"{arg}: "))
            
        #calculate then print the result
        result = modules[module_number].calculate(arguments_input)
        print (f'Result: {result}\n')
        
        #does the user want to run the module aain?
        run_again_input = input(f"Run Again (Y/N)? ").upper()
        if run_again_input == "Y":
            run_again = True
        else:
            run_again = False
    
    
def main():
    
    load_modules()
    list_modules()
    
    module_number_in = int(input('Enter Module Number to Run: '))
    run_module(module_number_in)
    
    # num1 = float(input('Num1: '))
    # num2 = float(input('Num2: '))


    # input_module = input_module.strip()

    # print (f'{plugins[input_module].calculate(num1,num2)}')


if __name__ == "__main__":
    main()