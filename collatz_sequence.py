#/usr/bin/python3


def collatz(number):

    print(number) 
    if number % 2 == 0:
        return collatz( number / 2)
    elif number == 1:
        return 1
    else:
        return collatz(number * 3 +1) 

def brute(number):

    while True:

        if number % 2 == 0:
            number = number / 2
            print(number)
        elif number == 1:
            break
        else:
            number = (number * 3) + 1
            print(number)

print ("Enter a number: ")

collatz( int(input()))

