#ChauHuynh
'''
1. Write a Python program to calculate the length of a string.
'''
def string_length(str):
    count = 0
    for char in str:
        count += 1
    return count

'''
2. Write a Python program to count the number of characters (character frequency) in a string. 
Sample String : 'google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''
def char_frequency(str):
    dict = {}
    for n in str:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

'''
3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.
Sample String :   'w3resource'  'w3',    ' w'
Expected Result : 'w3ce'        'w3w3'   Empty String
'''
def string_both_ends(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

'''
4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
Sample String : 'restart'
Expected Result : 'resta$t'
'''
def change_char(str):
  NewStr = ''
  checked = []
  for char in str:
    if char in checked:
      NewStr = NewStr + '$'
    else:
      NewStr = NewStr + char
    checked.append(char)
  return NewStr

'''
5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
Sample String : 'abc', 'xyz' 
Expected Result : 'xyc abz'
'''
def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b

'''
6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the given string is less than 3, leave it unchanged.
'''
def add_string(str):
  length = len(str)

  if length > 2:
    if str[-3:] == 'ing':
      str += 'ly'
    else:
      str += 'ing'

  return str

'''
7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. 
Sample String : 'The lyrics is not that poor!'
Expected Result : 'The lyrics is good!'
'''
def not_poor(str):
  snot = str.find('not')
  sbad = str.find('poor')

  if sbad > snot:
    str = str.replace(str[snot:(sbad+4)], 'good')

  return str

'''
8. Write a Python function that takes a list of words and returns the length of the longest one. 
'''

'''
9. Write a Python program to remove the nth index character from a nonempty string.
'''
def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part

'''
10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.
'''
def change_sring(str):
      return str[-1:] + str[1:-1] + str[:1]

'''
11. Write a Python program to remove the characters which have odd index values of a given string.
'''
def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result

'''
12. Write a Python program to count the occurrences of each word in a given sentence.
'''
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

'''
13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.
'''
user_input = input("What's your favourite language? ")
print("My favourite language is ", user_input.upper())
print("My favourite language is ", user_input.lower())     

'''
14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
'''
items = input("Input comma separated sequence of words")
words = [word for word in items.split(",")]
print(",".join(sorted(list(set(words)))))

'''
15. Write a Python function to create the HTML string with tags around the word(s)
'''
def add_tags(tag, word):
    return "<%s>%s</%s>" % (tag, word, tag) 

'''
16. Write a Python function to insert a string in the middle of a string.
insert_sting_middle('{{}}', 'PHP') -> {{PHP}}
'''
def insert_sting_middle(str, word):
    return str[:int(len(str)/2)] + word + str[int(len(str)/2):]

'''
21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters. 	
''' 
def to_uppercase(str):
    num_upper = 0
    for letter in str[:4]: 
        if letter.upper() == letter:
            num_upper += 1
    if num_upper >= 2:
        return str.upper()
    return str

'''
24. Write a Python program to check whether a string starts with specified characters
'''
string = "Huynh Ngoc Chau"
print(string.startswith("Huy"))
 
