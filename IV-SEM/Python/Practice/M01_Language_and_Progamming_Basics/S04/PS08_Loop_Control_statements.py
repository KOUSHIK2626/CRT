'''
Docstring for IV-SEM.Python.Practice.M01_Language_and_Progamming_Basics.S04.PS08_Loop_Control_statements
try : 
    a = int(input("Enter a number: "))
    print(10/a)
except ZeroDivisionError :
    print("Division by zero is not allowed.")
except ValueError :
    print("Invalid input.")
'''
import pdb
def add(a,b):
    pdb.set_trace()
    return a + b
a = int(input("Enter a number: "))
b = int(input("Enter another number: "))
print(add(a,b))
