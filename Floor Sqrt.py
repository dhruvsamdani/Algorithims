# I did not look the solution up anywhere I used my own binary search as that was the 
# only way I knew how to solve the problem on O(log n)
# This is all my code



def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """


    start = 0
    end = number

    if number < 0:
    	return 'Please enter a number greater than 0'

    while start <= end:
        mid = (start + end)//2
        if mid**2 == number:
            return mid
        if mid**2 > number:
            end = mid - 1 
            continue
        else:
            start = mid + 1
            continue
    

    return mid

print ("Pass" if  (3 == sqrt(9)) else "Fail") # Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail") # Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail") # Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail") # Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail") # Pass



print(sqrt(-1)) 
# Please enter a number greater than 0

print(sqrt(999999999999999999999999999))
# 31622776601683


