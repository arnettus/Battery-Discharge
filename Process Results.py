import csv
import matplotlib
import os 
import numpy as np

from matplotlib import pyplot as plt

directory = r'C:\Users\Adaria\Desktop\Battery Testing\Test Results'
directory_graphs = r'C:\Users\Adaria\Desktop\Battery Testing\Test Results\Graphed Results'
file_number = 0

time_list = []
voltage_list = []
current_list = []

while os.path.isfile('{0}/battery_string_{1}.csv'.format(directory, file_number)):
  
  with open('{0}/battery_string_{1}.csv'.format(directory, file_number, 'r')) as a:
    reader = csv.reader(a)
  
    for row in reader:
      try:
        time_list.append(float(row[0]))
        voltage_list.append(float(row[1]))
        current_list.append(float(row[2]))
      except IndexError:
        continue
      
    fig = plt.figure()
    ax = plt.axes()

    line = ax.plot(time_list, voltage_list)
    #cap = integrate.simps(voltage_list, time_list, even='last')
    
    avg_current = np.mean(current_list)
    
    cap = (avg_current)*(1000)*(time_list[-1]/(3600))

    ax.set_title('Capacity is {0} mAh'.format(cap))
    ax.set_xlabel('TIME (s)')
    ax.set_ylabel('VOLTAGE (V)')

    plt.savefig('{0}/battery_string_{1}_graph.pdf'.format(directory_graphs, file_number))

    file_number += 1
    
    del time_list[:]
    del voltage_list[:]
    del current_list[:]
    

  

