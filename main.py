import numpy, math
import pandas as pd
import scipy.signal as signal
import scipy.integrate as integrate
import matplotlib.pyplot as plt

var_names = ['acc_x', 'acc_y', 'acc_z', 'gyr_x', 'gyr_y', 'gyr_z'] #Initiate variable names
df = pd.read_csv(r'data\data_q1.csv', names=var_names) # Load the data
'''
fs = 60 # Sampling frequency of the sensor
fc = 5 # Cut-off frequency of the filter
w = (2*fc / fs) # Normalize the frequency
b, a = signal.butter(2, w, 'low') # Create filter para
acc_x_filtered = signal.lfilter(b, a, df['acc_x'])
'''


total_steps = len(df.index)
total_time = total_steps/60

time_array = []
for i in range(total_steps):
    time_array.append(i / total_steps * total_time)

df.index = time_array

orientation_x = numpy.cumsum(df['gyr_x'])/60


'''plt.plot(df.gyr_x, label="gyr x")'''

plt.plot(time_array, orientation_x, label="gyr rotation")

'''
plt.plot(df.acc_x, label="acc x")
plt.plot(time_array, acc_x_filtered, label="acc x filtered")

plt.plot(df.acc_y, label="acc y")
plt.plot(df.acc_z, label="acc z")

plt.xlabel('Seconds')
plt.ylabel('acceleration [m/s]')
plt.title('Accelerometer Data')

plt.plot(df.gyr_x, label="gyr x")
plt.plot(df.gyr_y, label="gyr y")
plt.plot(df.gyr_z, label="gyr z")
'''
plt.xlabel('Seconds')
plt.ylabel('Angle [degrees]')
plt.title('Rotation Data')
'''
plt.legend()
'''
plt.legend()
plt.show()
