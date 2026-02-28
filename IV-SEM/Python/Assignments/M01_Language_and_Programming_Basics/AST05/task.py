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
from typing import List


def Collatz_Sequence(n: int)-> List:
      sequence = []
      while n != 1:
         sequence.append(n)
         if n % 2 == 0:
               n = n // 2
         else:
               n = 3 * n + 1
      sequence.append(1)
      return sequence
      
if __name__ == '__main__':
    n = int(input())
    print(Collatz_Sequence(n))