#/usr/bin/python
#
# If the numbers 1 to 5 are written out in words:
# one, two, three, four, five, then there are
#   3 + 3 + 5 + 4 + 4 = 19 
# letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive
#were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. 
# For example, 342 (three hundred and forty-two) contains 23 letters
# and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with 
# British usage.
#
# This was an attempt to rewrite the solution from an other version
# that I wrote in the past in C. Thus it couldn't take care of all
# the advantages of Python.

from util import chronometer

def length_of(n):
    """
        Returns the lenght of the number in n when it is written 
        as word.

        for example:
            length_of(1) => 3 
        because 1 is "one" that has length 3.
    """

    # lengths of the numbers before 19
    numTo19 = [4, 3, 3, 5, 4, 4, 3, 5, 5,
               4, 3, 6, 6, 8, 8, 7, 7, 9,
               8, 8]

    # lengths of the number: 20, 30, 40, 50, 60, 70, 80, 90
    numTo99 = [6, 6, 5, 5, 5, 7, 6, 6]
    
    if n == 1000:
        return numTo19[1] + 8 # 8 => "thousand"
    elif n % 100 == 0:
        return numTo19[(n/100)+1] + 7 # 7 => "hundred"
    elif n > 100:
        tmp_len = numTo19[(n/100)+1] + 10 # 10 => "hundred and"

        n %= 100;
        if n <= 19:
            return tmp_len + numTo19[n];
        elif n % 10 == 0:
            return tmp_len + numTo99[(n/10)-2];
        else:
            return tmp_len + numTo99[(n/10)-2] + numTo19[n%10];
    elif n <= 19:
        return numTo19[n];
    elif n < 100:
        if n % 10 == 0:
            return numTo99[(n/10)-2];
        else:
            return numTo99[(n/10)-2] + numTo19[n%10];
    else:
        return 0;

@chronometer
def problem_17():
    return sum(map(length_of, range(1, 1001))) 

print problem_17()
