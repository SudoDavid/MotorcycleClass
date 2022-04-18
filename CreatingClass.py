
from unicodedata import name
#Define Class
class TermPaper:
    def __init__(person, name, subject, grade):
        person.name = name
        person.subject = subject
        person.grade = grade
    #Class Function
    def printTermPaper(person):
        print(person.name)
        print(person.subject)
        print(person.grade)
#Function1
def setUser():
    name = input("What is your name?\n")
    return name
#Function2
def setSubject():
    subject = input("What is the subject?\n")
    return subject
#Function3
def setGrade():
    grade = input("What is your letter grade?\n")
    return grade
#Main Function
def main():
    p1 = TermPaper(setUser(), setSubject(), setGrade())
    print()
    p1.printTermPaper()
#Main Function call
main()