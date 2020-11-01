# This is all my code
# I wrote this code when they asked the question in the lesson

def sort_012(input_list):
    
    start_index = 0
    last_index = len(input_list)-1
    
    current_index = 0
    
    while current_index < last_index:
        value = input_list[current_index]
        if value == 0:
            input_list[start_index],input_list[current_index] = 0,input_list[start_index]
            start_index += 1
            current_index += 1
        if value == 2:
            if input_list[last_index] == 1:
                input_list[last_index], input_list[current_index] = 2, input_list[last_index]
                last_index -= 1
                current_index += 1
            elif input_list[last_index] == 0:
                input_list[last_index], input_list[current_index] = 2, input_list[last_index]
            else:
                last_index -= 1
        if value == 1:
            current_index += 1
                
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]) # Pass [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]) # Pass [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]) # Pass [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]

test_function([0, 0]) # Pass [0, 0]

test_function([0, 1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1]) # Pass [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

test_function([0]) # Pass [0]

test_function([2,2,2,2,2]) # Pass [2, 2, 2, 2, 2]



