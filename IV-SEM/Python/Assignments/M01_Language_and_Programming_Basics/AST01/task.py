'''
# Ticket Pricing

## Problem Statement
Write a program for a cinema that asks for age and then calculates the price:
```
Age < 5: Free
Age 5–17: $10
Age 18–64: $20
Age 65+: $15
```
### Example
Input:16

Output:
10

## Instructions
1. Write your solution in `task.py`
2. Do NOT modify `test_task.py`
3. Run tests locally before pushing

## Submission Rules
- Only `task.py` will be evaluated
'''
def Ticket_Pricing(n: int) -> int:
    if n < 5:
        return 0
    elif 5 <= n <= 17:
        return 10
    elif 18 <= n <= 64:
        return 20
    else:
        return 15
if __name__ == "__main__":
      age = int(input())
      print(Ticket_Pricing(age))