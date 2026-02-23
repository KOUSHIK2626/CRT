'''4
Docstring for IV-SEM.Python.Practice.M02_Logic_Building
_and_Patterns.S04.PS05_Basic_patterns]
print 4 *4 pattern of stars
'''
n = int(input())
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

# to print right angle triangle
n = int(input())   
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print()
# to print inverted right angle triangle
n = int(input())
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()