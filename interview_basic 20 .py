#reverse   string 

def reverse_string(s):
    return s[::-1]

#check prime number 
def is_prime(n):
    if n <= 1: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True
#fibonacci numbers
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b



#Palidrome check 

def is_palindrome(s):
    return s == s[::-1]


#list missing 
def factorial(n):
    if n == 0: return 1
    return n * factorial(n - 1)


#find factorial 
def find_missing_number(lst):
    n = len(lst) + 1
    return n * (n + 1) // 2 - sum(lst)

#frequency of characters 
def char_frequency(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq
#angram check 
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)
#sum of digits
def sum_of_digits(n):
    return sum(int(d) for d in str(n))


#stack implementation 

def stack_operations():
    stack = []
    stack.append(10)
    stack.append(20)
    stack.pop()
    return stack


#balanced parenthesis
def is_balanced(expr):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in expr:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack

#find duplicates 
def find_duplicates(lst):
    return [x for x in set(lst) if lst.count(x) > 1]

#binary search
def binary_search(arr, x):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1
  
#longest word
def longest_word(sentence):
    return max(sentence.split(), key=len)


#common elements 
def common_elements(a, b):
    return list(set(a) & set(b))


#flatten nested list

def flatten_list(lst):
    flat = []
    for i in lst:
        if isinstance(i, list):
            flat += flatten_list(i)
        else:
            flat.append(i)
    return flat


#sort dictionary
def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))

#check pangram
import string
def is_pangram(s):
    return set(string.ascii_lowercase) <= set(s.lower())



