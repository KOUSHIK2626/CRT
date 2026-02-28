'''
# Reverse a String Using Loop

## Problem Statement
Reverse a string without using slicing.

### Example
Input: "Python"
Output: "nohtyP"

## Instructions
1. Write your solution in `task.py`
2. Do NOT modify `test_task.py`
3. Run tests locally before pushing

## Submission Rules
- Only `task.py` will be evaluated

'''
def Reverse_String(s: str) -> str:
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string


if __name__ == '__main__':
    s = input()
    print(Reverse_String(s))
