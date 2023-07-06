from sense_hat import SenseHat
import time

sense = SenseHat()
sense.clear()

def binomial_graph(data, max_a, min_a, levels=7):
    """
    This function draws a binomial graph representing the acceleration data
    on the LED matrix of the Sense HAT.
    
    Subjects:
    data -- list of acceleration values ​​for each axis (x, y, z)
    levels -- number of levels used to determine the color of the bar (default 7)
    
    Return value:
    x -- cursor position on the LED matrix after drawing the graph (0-7)
    """
    sense.clear()
    x=[0,3,6]
    
    steps=[]
    for i in range(3):
      steps.append((max_a[i]-min_a[i])/levels)
      
    for i in range(3):
        color = []
        intensity=data[i]
        maxy=max_a[i]
        miny=min_a[i]
        step = steps[i]
        if intensity >= maxy-step:
            color = [255, 0, 0]  # rosso
        elif intensity >= maxy-2*step:
            color = [255, 128, 0]  # arancione
        elif intensity >=maxy-3*step:
            color = [255, 255, 0]  # giallo
        elif intensity <= miny+step:
            color = [255, 0, 0]  # rosso
        elif intensity <= miny+2*step:
            color = [255, 128, 0]  # arancione
        elif intensity <= miny+3*step:
            color = [255, 255, 0]  # giallo
        else:
            color = [0, 255, 0]  # verde
        y_pos = int(7 * (1 - (intensity-miny)/((maxy-miny) or 0.0000001)))
        
        for j in range(8):
          if j <= y_pos:
              sense.set_pixel(x[i],j, color)
              sense.set_pixel(x[i]+1, j, color)
          else:
              sense.set_pixel(x[i], j, [0, 0, 0])
              sense.set_pixel(x[i]+1,j , [0, 0, 0])
    return x

# Open the file
f = open("dati.csv", "a")
#Ax Ay Az Acceleration from accelerometer (X,Y,Z)
#Gx Gy Gz Acceleration from gyroscope (X,Y,Z)
f.write("Time,Ax,Ay,Az,Gx,Gy,Gz,pitch,roll,yaw\n")
f.close()

# Start program
sense.show_message("HELLO ASTRONAUT, THE PROGRAM WILL START IN 3 2 1")
time.sleep(1)

sense.show_message("GETTING GYROSCOPE AND ACCELEROMETER DATA...")
time.sleep(1)

#init vars
start_time = time.time()
acceleration = sense.get_accelerometer_raw()
max_a=[acceleration['x'], acceleration['y'], acceleration['z']]
min_a=[acceleration['x'], acceleration['y'], acceleration['z']]
    
while True:
  gyro = sense.get_gyroscope_raw()
  acceleration = sense.get_accelerometer_raw()
  orientation =sense.get_orientation()
  data_a = [acceleration['x'], acceleration['y'], acceleration['z']]
  
  #update max and min
  for i in range(3):
    if data_a[i]>max_a[i]:
      max_a[i]=data_a[i]
    if data_a[i]<min_a[i]:
      min_a[i]=data_a[i]    

  x = binomial_graph(data_a,max_a,min_a)
  f = open("dati.csv", "a")
  f.write(str(time.time()) + "," + str(acceleration['x'])+","+ str(acceleration['y'])+","+ str(acceleration['z'])+"," +str(gyro['x'])+","+ str(gyro['y'])+","+ str(gyro['z'])+","+str(orientation['pitch']) +","+str(orientation['roll']) +","+str(orientation['yaw'])+"\n")
  f.close()
  
  elapsed_time = time.time() - start_time
  if elapsed_time >= 10800:
    break
