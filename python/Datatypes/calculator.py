import arithmetic


def main():

    print('Choose operators')
    print('1.Add 2 Sub 3.Mul 4.Div')
    select = int(input('select 1/2/3 : '))
    num01 = int(input('enter 1st number : '))
    num_02 = int(input("enter 2nd number : "))
    if (select == 1):
        Ans = arithmetic.Addition(num01, num_02)
        print(f' {num01} + {num_02} = {Ans}')
    elif (select == 2):
        Ans = arithmetic.Subraction(num01, num_02)
        print(f' {num01} - {num_02} = {Ans}')
    elif (select == 3):
        Ans = arithmetic.Multiplication(num01, num_02)
        print(f' {num01} * {num_02} = {Ans}')
    elif (select == 4):
        Ans = arithmetic.Division(num01, num_02)
        print(f' {num01} / {num_02} = {Ans}')
    else:
        print('choose 1/2/3')


if __name__ == "__main__":
    main()
