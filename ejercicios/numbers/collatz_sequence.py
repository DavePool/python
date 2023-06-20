#/usr/bin/python3

import unittest

def collatz(number):

    print(number) 
    if number % 2 == 0:
        return int(collatz( number / 2))
    elif number == 1:
        return int(1)
    else:
        return int(collatz(number * 3 +1)) 

def brute(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    else:
        stp = 0
        while True:

            if number % 2 == 0:
                stp +=  1
                number = number / 2
                print("Step number: "+str(stp)+" value: "+str(int(number)))
            elif number == 1:
                return (stp)
            else:
                stp += 1
                number = (number * 3) + 1
                print("Step number: "+str(stp)+" value: "+str(int(number)))


# print ("Enter a number: ")
# collatz( int(input()))

# unit test for collatz steps
class CollatzConjectureTest(unittest.TestCase):

    def test_zero_steps_for_one(self):
        self.assertEqual(brute(1), 0)
    def test_divide_if_even(self):

        self.assertEqual(brute(12), 9)
    def test_even_and_odd_steps(self):
        self.assertEqual(brute(4), 2)

unittest.main()