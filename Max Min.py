# This is all my code
# Only one solution I could think of as this is the most simple solution for this problem in O(n) time.

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
    	return None
    final_max = ints[0]
    final_min = ints[0]

    for value in ints:
    	if value> final_max:
    		final_max = value
    	if value < final_min:
    		final_min = value

    return final_min,final_max


## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail") # pass

l = [i for i in range(0, 50)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 49) == get_min_max(l)) else "Fail") # pass


l = [i for i in range(12, 18)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((12, 17) == get_min_max(l)) else "Fail") # pass


l = [i for i in range(0, 0)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if (None == get_min_max(l)) else "Fail") # pass