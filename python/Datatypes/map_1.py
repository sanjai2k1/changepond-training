from functools import reduce

def filtering(x,chars):
    print(x,chars)
    for i in chars:
        if i in x:
            return False
    return True
def main():
    # size = int(input('enter the size : '))
    # lst=[]
    # print('enter values : ')
    # for i in range(size):
    #     value = int(input())
    #     lst.append(value)
    # print('user list : ',lst)
    # map_list = list(map(lambda num : num**3,lst))
    # print('map list : ',map_list)
    # reduce_list = reduce((lambda num1,num2: num1+num2),map_list)
    # print('reduce list ',reduce_list)
    chars=[",",';']
    course=['','python','java',',,','angul;ar','php']
    print(list(filter(lambda x : filtering(x,chars) and x!='',course)))

if __name__ == "__main__":
    main()