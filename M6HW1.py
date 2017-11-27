#This program calculates number grade's into letter grades
#M6HW1
#Camron Hill
#11/8/17
def askForScore():
        grade1 = float(input('Enter grade 1: '))
        grade2 = float(input('Enter grade 2: '))
        grade3 = float(input('Enter grade 3: '))
        grade4 = float(input('Enter grade 4: '))
        grade5 = float(input('Enter grade 5: '))
        return grade1,grade2,grade3,grade4,grade5

def calc_average(grade1,grade2,grade3,grade4,grade5):
        average=(grade1+grade2+grade3+grade4+grade5) / 5
        return average 


def determine_grade(grade):
    if(grade >= 90):
        return "A"
    else:
        if(grade >=80  ):
            return "B"
        else:
            if(grade >= 70):
                return "C"
            else:
                if(grade >= 60):
                    return "D"
                else:
                    return "F"
def printTableOfResults(grade1, grade2, grade3, grade4, grade5):
    print("\nScore\tLetter Grade")
    print(str(grade1) +"\t\t" + determine_grade(grade1),\
    str(grade2) +"\t\t" + determine_grade(grade2),\
    str(grade3) +"\t\t" + determine_grade(grade3),\
    str(grade4) +"\t\t" + determine_grade(grade4),\
    str(grade5) +"\t\t" + determine_grade(grade5), sep = "\n")
def main():
    grade1, grade2, grade3, grade4, grade5 =askForScore()
    printTableOfResults(grade1, grade2, grade3, grade4, grade5)
main()
