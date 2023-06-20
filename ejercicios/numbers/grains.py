def square(number):
    actual_grain = 0
    chess_square = 1

    if number >= 1 and number <= 64:
        while chess_square <= number:
            if chess_square == 1:
                actual_grain += 1
                chess_square += 1
            else:
                # print ("Chess square: "+ str(chess_square)+" --> Grains count:"+str(actual_grain)) 
                actual_grain = actual_grain * 2
                chess_square += 1
        return actual_grain
    else:
        raise ValueError("square must be between 1 and 64")
    

def total():
    grain_count = 0

    for chess_square in range(1,65):
        grain_count += square(chess_square)

    return  grain_count