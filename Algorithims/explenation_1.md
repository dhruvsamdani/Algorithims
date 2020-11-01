Floor Sqrt:

For problem 1 I used a binary search because I needed to find the closest square root to a number. The search started with the max being the number itself and it would run until there was one number in the range from 0 to the number to be square rooted, getting me the answer. The time complexity is O(log n), where n is the number of elements the program has to search through (difference from max and min) and the space complexity is O(1), because there is only one array

Rotated Sorted Array Search:

For problem 2 I used another binary search and a modified binary search. I used a modified binary search to find the pivot point and then a binary search was optimal because I needed to find a certain element in the time constraint of O(log n), where a binary sort was perfect. The time constraint was O(log n), where n is the number of elements in the given array and the space time complexity is O(1) for the one array.

Max Sum:

For problem 3 I had to use mergesort to get a sorted array, since it has a runtime of O(nlogn). Once I got the sorted array I could figure out the max sum by breaking the array into two and alternating digits to add in the array. This program has a runtime of O(nlogn), where log n is the size of the array after each split and n is the number of splits needed to happen based on the size of the array. The space time complexity is O(n) beacuase a new array is made every time in mergesort

Sort 012:

For problem 4 I kept the array because I could move the elements around without creating an extra array. This was in a while loop and had to be done with one traversal, making the runtime O(n), where n is the number of elements in the array. Since only 1 array is being used it has a space time complexity of O(1).

Auto Complete Trie:

For problem 5 I used a trie because it allows for fast look up of words for autocomplete. The runtime for a trie is 
O(w x L), where w is the number of words and L is the number of letters in each word. Since the trie stores each letter in its own node this is the runtime and the space time compxity is O(n), where n is the number of nodes a trie has.

Max Min:

In problem 6 I used a for loop to iterate through an array and find a max and min. Since it only went through one iteration with a for loop the runtime is O(n), where n is the number of elements in the array. The space time complexity is O(1), because 1 array was being used.

Router Trie:

For problem 7 I used a trie because it allows for fast look up of paths in a website. The runtime for a trie is 
O(P x I), where P is the number of complete paths and I is the number of sub paths in each complete path. Since the trie stores each letter in its own node this is the runtime and the space time compxity is O(n), where n is the number of nodes a trie has.