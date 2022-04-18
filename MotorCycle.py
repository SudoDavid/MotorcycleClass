
class MotorCycle(object):
    def __init__(self, max_speed, speed, sidecar):
    #set variables/attributes
        self.max_speed = max_speed
        self.speed = speed
        self.sidecar = sidecar
    
    def accelerate(self):
        if self.max_speed < self.speed:
            print("The motorcycle is going to fast.")
        else:
            print("The motorcycle is going too slow.")

#Setting Functions
def setmax_speed():
    max_speed = int(input("What is the speed limit in mph?\n"))
    return max_speed
#Function2
def set_speed():
    speed = int(input("What is your current speed in mph?\n"))
    return speed
#Function3
def sidecar():
    sidecar = str(input("Do you have a sidecar? 1 is yes, 2 if no. \n"))
    return sidecar
#Main Function
def main():
    p1 = MotorCycle(setmax_speed(), set_speed(), sidecar())
    print()
    p1.accelerate()
main()