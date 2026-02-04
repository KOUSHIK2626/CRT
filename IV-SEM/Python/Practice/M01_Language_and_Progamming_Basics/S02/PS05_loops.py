 #while loop
'''
counter = 0
while counter < 5:
    print("Hello World!")
    counter += 1    
#print("Hello World!")

read two intgeres start and step variables
display all even numbers between start and stop

start = int(input("Enter start value: "))
stop = int(input("Enter stop value: "))
while start <= stop:
    if start % 2 == 0:
        print(start, end=" ")
    start += 1
'''
start = int(input("Enter start value: "))
stop = int(input("Enter stop value: "))
while start <= stop:
    if start % 3 == 0 and start % 5 == 0:
        print("fizzbuzz")
    elif start % 5 == 0:
        print("buzz")
    elif start % 3 == 0:
        print("fizz")
    else: 
        print(start)
    start += 1
    