# CTI 110
# M3Lab
# Camron Hill
# 9/13/2017

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    score =int(input('Give me a score: '))

    if score >= 90:
        print('Your grade is: A')
    else:
        if score > 80 and score <=89:
            print('Your grade is: B')
        else:
            if score <= 79 and score > 70:
               print('Your grade is: C')
            else:
               if score <= 69 and score >= 60:
                   print('Your grade is: D')
               else:
                      print('Your grade is: F')







# program start
main()
