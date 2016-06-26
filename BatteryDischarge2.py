import visa
import time
import csv
import matplotlib
import os
import sys
from matplotlib import pyplot as plt
from matplotlib import animation as ani

rm = visa.ResourceManager()
resources = rm.list_resources()
inst = rm.open_resource(resources[0])

inst.write('*RST')
inst.write('FUNC CURR')
inst.write('CURRent 20')
inst.write('INP ON')

def animate(i):
  values = float(str(inst.query(':FETCh:VOLTage?')))
  current = float(str(inst.query(':FETCh:CURRent?')))
  print(values)

  if len(x) > 10:
    x.pop(0)

  if len(y) > 10:
    y.pop(0)
 
  y.append(values)
  value_list.append(values)
  time_list.append((x[-1]+1)*(period_ms/1000))
  current_list.append(current)
  x.append(x[-1] + 1)

  line[0].set_data(x, y)

  ax.set_xlim(x[0],x[-1])
  
  if (values < 3.2):
    with open('{0}/battery_string_{1}.csv'.format(directory, file_number), 'w') as file:
      writer = csv.writer(file)
      for i in range(0, len(time_list)):
        writer.writerow([time_list[i], value_list[i], current_list[i]])

    print("Safe exit")
    hasCapacity = False
    inst.write('CURRent 0')	
    inst.write('INP 0')	
    time.sleep(1)
    sys.exit()

  return line


try:
  value_list = []
  time_list = []
  current_list = []
  period_ms = 100

  directory = 'C:\\Users/Adaria/Desktop/Battery Testing/Test Results'

  file_number = 0
  while os.path.isfile('{0}/battery_string_{1}.csv'.format(directory, file_number)):
    file_number += 1
    
  values = 0
  hasCapacity = True

  fig = plt.figure()
  ax = plt.axes(ylim=(0, 6))

  y = [0]
  x = [0]
   
  line = ax.plot([],[])

  ani = ani.FuncAnimation(fig, animate, interval = period_ms, blit = False)

  plt.show()

except:
    print('Failed to initialize')
    inst.write('INP OFF')
    inst.write('CURRent 0')		
