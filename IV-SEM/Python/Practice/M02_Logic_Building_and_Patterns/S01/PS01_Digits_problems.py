'''
Docstring for Python.Practice.M02_Logic_Building_and_Patterns.S01.PS01_Digits_problems
n = int(input())
count = 0
while n > 0:
    count +=1
    n= n//10
print(count)
n = int(input())
s = 0
while n > 0:
    s += n%10
    n = n//10
print(s)
n = int(input())
while n > 0:
    digit = n%10
    if digit%2 == 0:
        print(digit,end = " ")1
    n = n//10

def reverse(num):
    rev = 0
    while num > 0:
        rev = rev*10 + num%10
        num = num//10
    return rev
n = int(input())
while n > 0:
    digit = n%10
    if digit%2 == 0:
        print(digit,end = " ")  
    n = n//10
'''
n = int(input())