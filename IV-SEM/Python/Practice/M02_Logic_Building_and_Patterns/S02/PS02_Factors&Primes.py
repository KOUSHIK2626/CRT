'''
n = int(input())
for i in range(1,n//2+1):
    if n%i == 0:
        print(i,end = " ")
print(n)
n = int(input())
counter = 0
for i in range(1,n//2+1):
    if n%i == 0:
        counter += 1
print(counter) 
'''
'''
prime or not
n = int(input())
if n % 2 == 0:
    print("Not Prime")
else:
    for i in range(3,n//2+1,2):
        if n%i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")



#other logic
n = int(input())
counter = 0
for i in range(2,n//2+1):
    if n%i == 0:
        counter += 1
if counter == 0:
    print("Prime")
else:
    print("Not Prime")
ternary operator
n = int(input())
counter = 0
for i in range(2,n//2+1):
    if n%i == 0:
        counter += 1
print("prime" if counter == 0 else "not prime")


# in a given range print all the prime numbers
start = int(input())
end = int(input())
for n in range(start,end+1):
    counter = 0
    for i in range(2,n//2+1):
        if n%i == 0:
            counter += 1
    if counter == 0:
        print(n,end = " ")
'''
# factorial of a number
n = int(input())
fact = 1
for i in range(1,n+1):
    fact *= i
print(fact)

