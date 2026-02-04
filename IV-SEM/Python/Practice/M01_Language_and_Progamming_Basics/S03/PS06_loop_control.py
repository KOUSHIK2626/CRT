'''
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)    
'''
p1 = "abc123"
for i in range(3):
    p2 = input()
    if p1 == p2:
        print("Login Successful")
        break
else:
    print("Login Failed")