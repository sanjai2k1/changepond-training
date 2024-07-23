# def Addition():
#     print('Inside Addition')
# Addition()

def Addition(value_01):
    print('Inside Addition')
    print('Argument : ',value_01)

def Addition(value_01,value_02):
    print('Inside Addition')
    print('Argument : ',value_01,value_02)
    print(f'{value_01} and {value_02} adiition is',value_01+value_02)
    add= value_01+value_02
    print('Inside Subtraction')
    print('Argument : ',value_01,value_02)
    print(f'{value_01} and {value_02} subtraction is',value_01-value_02)
    sub=value_01-value_02
    return add,sub

def Subraction(value_01,value_02):
    print('Inside Subtraction')
    print('Argument : ',value_01,value_02)
    print(f'{value_01} and {value_02} subtraction is',value_01-value_02)
    return value_01-value_02

def main():
    add,sub=Addition(12,13)
    print(add,sub)

if __name__ == "__main__":
    main()
# print(Subraction(12,13))
