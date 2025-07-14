#two sum(array+hash map)
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]
        seen[num] = i

print(two_sum([2, 7, 11, 15], 9))  # [0, 1]

#binary search,,,,, Given a singly linked list, reverse it in-place
#
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev



# Search for an element in a sorted array.

def binary_search(arr, target):
    low, high = 0, len(arr)-1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target: return mid
        elif arr[mid] < target: low = mid + 1
        else: high = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9], 5))  # 2

#valid parenthesis(stack)
def is_valid(s):
    stack = []
    match = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in match.values():
            stack.append(char)
        elif char in match:
            if not stack or stack.pop() != match[char]:
                return False
    return not stack

print(is_valid("{[()]}"))  # True


#mereged two sorted array/list
def is_valid(s):
    stack = []
    match = {')': '(', ']': '[', '}': '{'}
    for char in s:
        if char in match.values():
            stack.append(char)
        elif char in match:
            if not stack or stack.pop() != match[char]:
                return False
    return not stack

print(is_valid("{[()]}"))  # True



