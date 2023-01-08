a = int(input())
b = input()
c = int(input())
if b == '+':
    print(a+c)
if b == '-':
    print(a-c)
if b == '*':
    print(a*c)
if b == '/':
    if c == 0 :
        print("на 0 делить нельзя")
    else:
        print(a/c)
