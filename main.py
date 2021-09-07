#Libraries used in this project
import numpy as np
import car
import bike
import random
import pandas as pd
from IPython.display import display
import statistics


#Generating dummy data between an interval
vel1 = random.randint(70,80)
vel2 = random.randint(70,80)
vel3 = random.randint(70,80)
vel4 = random.randint(70,80)
vel5 = random.randint(70,80)
vel6 = random.randint(70,80)
vel7 = random.randint(70,80)
vel8 = random.randint(70,80)
vel9 = random.randint(70,80)
vel10 = random.randint(70,80)

vel11 = random.randint(70,80)
vel12 = random.randint(70,80)
vel13 = random.randint(70,80)
vel14 = random.randint(70,80)
vel15 = random.randint(70,80)
vel16 = random.randint(70,80)
vel17 = random.randint(70,80)
vel18 = random.randint(70,80)
vel19 = random.randint(70,80)
vel20 = random.randint(70,80)

#Creating an object of the class car with some parameters
c1 = car.Car('Honda',vel1,'black')
#c1.carInfo()
c2 = car.Car('Toyota',vel2,'red')
#c2.carInfo()
c3 = car.Car('Ferrari',vel3,'blue')
#c3.carInfo()
c4 = car.Car('BMW',vel4,'grey')
#c4.carInfo()
c5 = car.Car('Aston Martin',vel5,'red')
#c5.carInfo()
c6 = car.Car('Tesla',vel6,'magenta')
#c6.carInfo()
c7 = car.Car('Ford',vel7,'yellow')
#c7.carInfo()
c8 = car.Car('GM',vel8,'black')
#c8.carInfo()
c9 = car.Car('Lambo',vel9,'black')
#c9.carInfo()
c10 = car.Car('Honda',vel10,'red')
#c10.carInfo()

#Creating an object of the class bike with some parameters
b1 = bike.Bike('Yamaha','black',vel11)
b2 = bike.Bike('Honda','red',vel12)
b3 = bike.Bike('Ducati','silver',vel13)
b4 = bike.Bike('Kawasaki','green',vel14)
b5 = bike.Bike('Triumph','black',vel15)
b6 = bike.Bike('Bmw','black',vel16)
b7 = bike.Bike('Harley-Davidson','blue',vel17)
b8 = bike.Bike('Suzuki','baby blue',vel18)
b9 = bike.Bike('Yamaha','orange',vel19)
b10 = bike.Bike('YDucati','yellow',vel20)

#List with cars information
dataCar =[   [c1.brand,c1.color,c1.velocity],
             [c2.brand,c2.color,c2.velocity],
             [c3.brand,c3.color,c3.velocity],
             [c4.brand,c4.color,c4.velocity],
             [c5.brand,c5.color,c5.velocity],
             [c6.brand,c6.color,c6.velocity],
             [c7.brand,c7.color,c7.velocity],
             [c8.brand,c8.color,c8.velocity],
             [c9.brand,c9.color,c9.velocity],
             [c10.brand,c10.color,c10.velocity],
]

#List with bike information
dataBike = [    [b1.brand,b1.color,b1.velocity],
                [b2.brand,b2.color,b2.velocity],
                [b3.brand,b3.color,b3.velocity],
                [b4.brand,b4.color,b4.velocity],
                [b5.brand,b5.color,b5.velocity],
                [b6.brand,b6.color,b6.velocity],
                [b7.brand,b7.color,b7.velocity],
                [b8.brand,b8.color,b8.velocity],
                [b9.brand,b9.color,b9.velocity],
                [b10.brand,b10.color,b10.velocity]
]

lstVel = []  #CARS velocity
lstVel2 = [] #BIKES velocity

lstVel.append(c1.velocity)
lstVel.append(c2.velocity)
lstVel.append(c3.velocity)
lstVel.append(c4.velocity)
lstVel.append(c5.velocity)
lstVel.append(c6.velocity)
lstVel.append(c7.velocity)
lstVel.append(c8.velocity)
lstVel.append(c9.velocity)
lstVel.append(c10.velocity)

lstVel2.append(b1.velocity)
lstVel2.append(b2.velocity)
lstVel2.append(b3.velocity)
lstVel2.append(b4.velocity)
lstVel2.append(b5.velocity)
lstVel2.append(b6.velocity)
lstVel2.append(b7.velocity)
lstVel2.append(b8.velocity)
lstVel2.append(b9.velocity)
lstVel2.append(b10.velocity)

#Displaying data in a table and getting standard deviation of the information
print('Data obtained from taking samples of highway 75 of 10 different cars ')
dfc = pd.DataFrame(dataCar,columns=['Brand','Color','Velocity [mph]'])
display(dfc)
#df.to_csv('VelocityData.csv',data.values)
print('Standard Deviation of data sample is: ', statistics.stdev(lstVel))
print('Mean of data sample is: ', statistics.mean(lstVel))

print('Data obtained from taking samples of highway 80 of 10 different bikes ')
dfb = pd.DataFrame(dataBike,columns=['Brand','Color','Velocity [mph]'])
display(dfb)
print('Standard Deviation of data sample is: ', statistics.stdev(lstVel2))
print('Mean of data sample is: ', statistics.mean(lstVel2))