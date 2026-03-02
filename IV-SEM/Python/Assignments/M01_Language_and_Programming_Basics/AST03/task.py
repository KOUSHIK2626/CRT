def Student_Grade_System(name:str,n1: int,n2: int,n3: int) -> str:
    grades = [n1, n2, n3]
    avg = int(sum(grades) * 100 / 3) / 100
    status = "Pass" if all(grade >= 35 for grade in grades) else "fail"
    return f"Average grade: {avg}, Status: {status}"
    

if __name__ == '__main__':
    name = input()
    n1,n2,n3 = list(map(int,input().split()))
    print(Student_Grade_System(name,n1,n2,n3))