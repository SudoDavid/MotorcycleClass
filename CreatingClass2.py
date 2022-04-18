
from unicodedata import name
#Define Class
class Computer:
    def __init__(station, make, model, memory):
        station.make = make
        station.model = model
        station.memory = memory
    #Class Function
    def printSpecs(station):
        print(station.make)
        print(station.model)
        print(station.memory)
#Function1
def setMake():
    make = input("What is your make?\n")
    return make
#Function2
def setModel():
    model = input("What is the model?\n")
    return model
#Function3
def setMemory():
    memory = input("How much Memory do you have(Ram in GB)?\n")
    return memory
#Main Function
def main():
    p1 = Computer(setMake(), setModel(), setMemory())
    print()
    p1.printSpecs()
#Main Function call
main()