'''
2. Write a Python program to multiplies all the items in a list.
'''
def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot

'''
4. Write a Python program to get the smallest number from a list.
'''
def smallest_num_in_list( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min

'''
5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''

'''
6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
'''
def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

'''
7. Write a Python program to remove duplicates from a list
'''
def dup_items(list):
    return list(set(list))

'''
8. Write a Python program to check a list is empty or not.
'''
l = []
if not l:
  print("List is empty")

'''
9. Write a Python program to clone or copy a list.
'''
new_list = list(original_list) #dont use new_list = original_list

'''
12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
'''
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
color = [x for (i,x) in enumerate(color) if i not in (0,4,5)]
print(color)

'''
21. Write a Python program to convert a list of characters into a string.
'''
s = ['a', 'b', 'c', 'd']
str = ''.join(s)

'''
30. Write a Python program to get the frequency of the elements in a list.
'''
import collections
my_list = [10,10,10,10,20,20,20,20,40,40,50,50,30]
print("Original List : ",my_list)
ctr = collections.Counter(my_list)
print("Frequency of the elements in the List : ",ctr)

'''
36. Write a Python program to get variable unique identification number or string. 
'''
my_list = ['p', 'q']
n = 4
new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
print(new_list)

'''
37. Write a Python program to find common items from two lists.
'''
color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"
print(set(color1) & set(color2))

'''
39. Write a Python program to convert a list of multiple integers into a single integer.
'''
L = [11, 33, 50]
print("Original List: ",L)
x = int("".join(map(str, L)))
print("Single Integer: ",x)

'''
47. Write a Python program to insert an element before each element of a list.
'''
color = ['Red', 'Green', 'Black']
print("Original List: ",color)
color = [v for elt in color for v in ('c', elt)]
print("Original List: ",color)

'''
50. Write a Python program to sort a list of nested dictionaries.
'''
my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print("Original List: ")
print(my_list)
my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
print("Sorted List: ")
print(my_list)

'''
58. Write a Python program to replace the last element in a list with another list.
'''
num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]
num1[-1:] = num2

'''
69. Write a Python program to remove duplicates from a list of lists.
Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
New List : [[10, 20], [30, 56, 25], [33], [40]]
'''
import itertools
num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print("Original List", num)
num.sort()
new_num = list(num for num,_ in itertools.groupby(num))
print("New List", new_num)
