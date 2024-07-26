# def sum_all(*args):
#     count=0
#     for i in args:
#         count+=i
#     return count

# output = sum_all(1,2,3,4,5)
# print(output)


#changepond = ['gokul','ajth','suresh','dhanush']
# def capitilize(*args):
#     for i in args:
#         print(i.capitalize())

# def main():
#     capitilize('gokul','ajth','suresh','dhanush')

# if __name__=="__main__":
#     main()
    
    
    
def staffDetails(*args,**kwargs):
    print(args)
    for key,value in kwargs.items():
        print(key,value)

def main():
    changepond={'name':'gokul',
                'age':21,
                'mobilenum':1234444}
    lst=[1,2,3,4]
    staffDetails(*lst,**changepond)
if __name__=="__main__":
    main()