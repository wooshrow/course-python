import random

def average(x,y,z):
    """ Calculate average

    This function calculates the average of three numbers.
    """

    # fist calculate the sum
    # then divide by n:
    sum = x + y + z
    av = sum/3
    return av

# just an example:
print(f"average of 0,2,4 is {average(0,2,4)}")
x1 = random.randint(0,10)
x2 = random.randint(0,10)
x3 = random.randint(0,10)
print(f"average of {x1},{x2},{x3} is {average(x1,x2,x3)}")
