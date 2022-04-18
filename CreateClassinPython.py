class Rectangle(object):
    #Declare methpds
    def __init__(self, length, width):
        #set variables/attributes
        self.length = length
        self.width = width

    def calculateArea(self):
        #define
        print("The area of the rectangle is: ")
        print(self.length * self.width)
    def calculatePerimeter(self):
        #define
        print("The area of the perimeter is: ")
        print((self.length*2) + (self.width*2))
#Function1
def setwidth():
    width = int(input("What is the rectangle width?\n"))
    return width
#Function2
def setLength():
    length = int(input("What is the rectangle length?\n"))
    return length
#Main Function
def main():
    again = input("Would you like to continue? Select Y \n")
    while again == 'Y' or again == 'y':
        p1 = Rectangle(setwidth(), setLength())
        print()
        p1.calculateArea()
        print()
        p1.calculatePerimeter()
        again = input("Would you like to continue? Select Y \n")
#Main Function call
main()