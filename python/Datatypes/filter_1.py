# write a program which will check the number is greater and equal to and less than equal to 90
def check_number(x):
    return x >=70 and x<=90

def main():
    size = int(input('enter the size : '))
    lst=[]
    print('enter values : ')
    for i in range(size):
        value = int(input())
        lst.append(value)
    print('user list : ',lst)
    filter_list = list(filter(check_number,lst))
    print(filter_list)

if __name__ == "__main__":
    main()