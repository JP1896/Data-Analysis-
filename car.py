class Car:
    def __init__(self,brand,velocity,color):
        self.brand = brand
        self.velocity = velocity
        self.color = color
    '''
    def getAceleration(self,v,t):
        aceleration = v/t
        print('The aceleration of the car is : ', aceleration)
'''
    def carInfo(self):
        print('Brand:',self.brand)
        print('Velocity:', self.velocity)
        print('Color:', self.color)


