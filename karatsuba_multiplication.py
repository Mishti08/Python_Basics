"""
Karatsuba Algorithm implementation
Running Time =O(n**log(3))

Base Case : if value of x and y is a single digit value directly multiply.
Step 1: x = 1234  y=5678
Step 2: x_H = 12,x_L = 34 ,y_H = 56, y_L = 78, m = ceil(max(len(x,y))/2)
Step 3: high_bit_multi= x_H*y_H
Step 4: low_bit_multi = x_L*y_L
Step 5: high_low_bit_multi = (x_H + x_L) *(y_H + y_L)
Step 6: final_cal = high_low_bit_multi - high_bit_multi -low_bit_multi
Step 7: calculated_value = high_bit_multi*(10**(m*2) + final_cal*(10**m) + low_bit_multi

math.ceil() ->Returns float value roundoff to upper bound value
Example:
    1. 3/2 = 1.5
    2. math.ceil(3/2) = 2

math.floor() ->Returns float value roundoff to lower bound value
Example:
    1. 3/2 = 1.5
    2. math.floor(3/2) = 1
"""



from math import ceil, floor

def karatsuba_multiplication(x,y):
    '''
    Function to perform multiplication using Karatsuba multiplication algorithm.

    Parameters
    ----------
    x: int
        Integer Value to multiply
    y : int
        Integer Value to multiply
    Returns
    -------
    calculated_value : int
        Value after Multiplication

    '''


    if x < 10 and y < 10: 
        return x*y

    n = max(len(str(x)), len(str(y)))
    m = ceil(n/2)

    x_H  = floor(x / 10**m)
    x_L = x % (10**m)

    y_H = floor(y / 10**m)
    y_L = y % (10**m)

    #Recursive steps
    high_bit_multi = karatsuba_multiplication(x_H,y_H)
    low_bit_multi = karatsuba_multiplication(x_L,y_L)
    high_low_bit_multi = karatsuba_multiplication(x_H + x_L, y_H + y_L)
    final_cal =  high_low_bit_multi - high_bit_multi - low_bit_multi
    calculated_value = int(high_bit_multi*(10**(m*2)) + final_cal*(10**m) + low_bit_multi)
    return calculated_value


print(karatsuba_multiplication(x=100,y=2))
