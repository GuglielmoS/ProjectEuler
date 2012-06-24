#!/usr/bin/python
#
# The fraction 49/98 is a curious fraction, as an inexperienced 
# mathematician in attempting to simplify it may incorrectly believe
# that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, 
# less than one in value, and containing two digits in the numerator and 
# denominator.
#
# If the product of these four fractions is given in its lowest common terms, 
# find the value of the denominator.

from util import chronometer
from util import simplify_fraction

@chronometer
def problem_33():
    final_product = (1, 1)
    for num in range(10, 99):
        for den in range(num+1, 99):
            # exclude every number that is divisible by 10
            if num % 10 != 0 and den % 10 != 0:
                expected_result = simplify_fraction((num, den))
                        
                # calculates the "simplified" version
                fd1, sd1 = num / 10, num % 10
                fd2, sd2 = den / 10, den % 10 
                
                # checks that the two digits are not zero
                if fd1 != 0 and fd2 != 0:
                    flag = True 
                    new_num = fd1
                    new_den = fd2

                    if fd1 == fd2:
                        new_num = sd1
                        new_den = sd2
                    elif fd1 == sd2:
                        new_num = sd1
                    elif sd1 == fd2:
                        new_den = sd2
                    elif sd1 == sd2:
                        pass
                    else:
                        flag = False

                    # if it can be "simplified"
                    if flag:
                        simplified_version = simplify_fraction((new_num, new_den))

                        # if the "simplification" produces a good result
                        if simplified_version == expected_result:
                            final_product = (final_product[0]*new_num, 
                                              final_product[1]*new_den)

    # returns the denominator of the simplified final product
    return simplify_fraction(final_product)[1]

print problem_33()  

