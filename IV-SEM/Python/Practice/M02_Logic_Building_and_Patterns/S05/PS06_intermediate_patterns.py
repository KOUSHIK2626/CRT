# square of elements in a list
'''
li = [1,2,3,4,5]
res = []
for i in li:
    if i% 2 == 0:4
        res.append(i)
print(res)

# using list comprehension
print (" " *5)
li = ['a','b','c']
res = ' '
for ch in li:
    res = res+ch+ " "
print(res)
print( "@".join(li))


# print a pyramid pattern 
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i)
#reverse pyramid pattern
n = int(input())
for i in range(n,0,-1): 
    print(" "*(n-i)+"* "*i)

# print a diamond pattern
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i)+"* "*i) 
for i in range(n-1,0,-1):
    print(" "*(n-i)+"* "*i)
'''
# print a number pyramid pattern
n = int(input())
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    print()