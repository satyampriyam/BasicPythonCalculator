def main():
    print("Enter a basic expression to be evaluated")
    s = input()
    oper = s.split(' ')
    a = int(oper[0])
    b = int(oper[2])
    op = oper[1]

    if op == '+':
        print(a+b)
    elif op == '-':
        print(a-b)
    elif op == '*':
        print(a*b)
    elif op == '/':
        print(a/b)
    elif op == '//':
        print(a//b)
    elif op =='%':
        print(a%b)

if __name__ == '__main__':
    main()
