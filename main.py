
import pandas as pd
var_names = ['acc_x', 'acc_y', 'acc_z', 'gyr_x', 'gyr_y', 'gyr_z'] #Initiate variable names
df = pd.read_csv(r'data\data_q1.csv', names=var_names) # Load the data

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'fakka, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('niffau')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
