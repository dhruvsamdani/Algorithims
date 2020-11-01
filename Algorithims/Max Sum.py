# This is all my code
# I used the merge sort from the lesson for the merge sort


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """



    arr = merge_sort(input_list)

    int1 = []
    int2 = []
    # print(arr)
    for item in range(len(arr)): 
        if item%2 == 0:
            int1.append(str(arr[item]))

        else:
            int2.append(str(arr[item]))


    int1 = ''.join(int1)
    int2 = ''.join(int2)

    if len(int2) == 0:
        return int(int1)
    return int(int1), int(int2)


    pass

def merge_sort(arr):

    def merge(left, right):
        merged_arr = []
        left_index = 0
        right_index = 0

        while left_index<len(left) and right_index<len(right):
            if left[left_index] < right[right_index]:
                merged_arr.append(right[right_index])
                right_index += 1
            else:
                merged_arr.append(left[left_index])
                left_index += 1

        merged_arr += left[left_index:]
        merged_arr += right[right_index:]

        return merged_arr 



    if len(arr) <= 1:
        return arr

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]]) # pass
test_function([[4, 6, 2, 5, 9, 8], [964, 852]]) # pass
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]] # pass
test_function(test_case)
arr = [1,1,1,1,1,1,1,1,1]
print(rearrange_digits(arr)) # (11111, 1111)

arr = [1]
print(rearrange_digits(arr)) # 1



