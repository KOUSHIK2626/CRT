
# pascal triangle
n = int(input())
for i in range(1,n+1):
    num = 1
    for j in range(i):
        print(num, end=" ")
        num = num * (i-j-1) // (j+1)
    print()
# Butterfly pattern
n = int(input())
for i in range(1,n+1):
    print("* "*i + "  "*(2*(n-i)) + "* "*i)
for j in range(n,0,-1):
    print("* "*j + "  "*(2*(n-j)) + "* "*j)

