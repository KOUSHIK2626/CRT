'''
# Student Grade System 

## Problem Statement

Calculate and store student grades for various subjects.

This project stores student grades for various subjects, calculates their average, and determines their final grade. The user can input subject marks, and the system calculates the overall result (pass/fail).

Input: Student name and grades for multiple subjects(3).
Output: Student’s average grade and status (pass/fail).

### Example
Input:
Name: Pavan, Grades: 85, 90, 78

Output:
"Average grade: 84.33, Status: Pass"

## Instructions
1. Write your solution in `task.py`
2. Do NOT modify `test_task.py`
3. Run tests locally before pushing

## Submission Rules
- Only `task.py` will be evaluated

'''
def Student_Grade_System(name:str,n1: int,n2: int,n3: int) -> str:
    average = (n1 + n2 + n3) / 3
    status = "Pass" if average >= 40 else "Fail"
    return f"Average grade: {average:.2f}, Status: {status}"

if __name__ == '__main__':
    name = input()
    n1,n2,n3 = list(map(int,input().split()))
    print(Student_Grade_System(name,n1,n2,n3))