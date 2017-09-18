# CTI 110
# Camromn Hill
# 9/18/2017
def main ():
    sell= int(input('How much it cost: '))
    pay= 99
    
    if sell <10:
        print('No discount.')
    else:
        if sell < 20:
            print('10% discount')
        else:
            if sell < 50:
                print('20% discount')
            else:
                if sell <100:
                    print('30% discount')
                else:
                    print('40% discount')


main()
                  
                  
                      
