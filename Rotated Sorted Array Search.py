# Inspiration taken from geeks for geeks for the pivot 
# All code is mine, however

# Geeks for Geeks link

# https://www.geeksforgeeks.org/search-an-element-in-a-sorted-and-pivoted-array/


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    return binary_search(input_list,number,find_pivot(input_list))






def find_pivot(arr):

    begining = 0
    last = len(arr)-1
    
    while begining <= last:
        mid = (begining + last)//2

        if arr[mid+1] < arr [mid]:
            return mid
        if mid < last and arr[mid] > arr [mid +1]:
            begining = begining
            last = mid - 1
        if mid > begining and arr[mid] > arr[mid - 1]:
            begining = mid + 1
            last = last
        return mid-1

    return mid




def binary_search(arr,number,pivot):
    n = len(arr)
    begining = 0
    last = n - 1

    if arr[0] == number:
        return 0

    if arr[n-1] == number:
        return n-1


    while begining < last:
        sorted_mid = (begining + last)//2
        mid = ((begining + last)//2 + pivot+1)%n
        if arr[mid] == number:
            return mid
        if number < arr[mid]:
            last = (mid - 1-pivot-1)%n
        if number > arr[mid]:
            begining = (mid + 1-pivot-1)%n

    mid = ((begining + last)//2 + pivot+1)%n
    if arr[mid] == number:
            return mid
    return -1






def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6]) # Pass
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1]) # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 8]) # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 1]) # Pass
test_function([[6, 7, 8, 1, 2, 3, 4], 10]) # Pass

print(rotated_array_search([1,2,3,4], 2)) # 1

print(rotated_array_search([1,1,1,1,], 1)) # 0
