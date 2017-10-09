#M5T2
#Camron Hill
#10/9/17
def main():
#Initialize the accumulator.
    total = 0
#Get the bugs collected for each day.
    for day in range(1,8):
        print('Enter the bugs collected on day', day)
        bugs= int(input())
        total += bugs
#Display the total bugs.
    print('You collected a total of', total, 'bugs.')

main()
