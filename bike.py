class Bike:
    def __init__(self,brand,color,velocity):
        self.brand = brand
        self.color = color
        self.velocity = velocity

        '''
        def getAceleration(self,v,t):
            aceleration = v/t
            print('The aceleration of the bike is : ', aceleration)
    '''
    def bikeInfo(self):
        print('Brand:',self.brand)
        print('Velocity:', self.velocity)
        print('Color:', self.color)