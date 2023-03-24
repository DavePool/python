def is_armstrong_number(number):
    sum = 0
    for unit in str(number):
        to_pow = len(str(number))

        print ("The number: "+ unit +" Would be powded by: "+ str(to_pow))
        sum = sum + (pow(int(unit), to_pow))
    
    print("The sum is: "+ str(sum))
    if sum == number:
        return True
    else:
        return False