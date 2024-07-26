#open() function -> filename , mode(r,w,q,....)

# file_read = open('python\Datatypes\calculator.py','r')
# print(file_read.read())

import os
def createfile(filename):
    if (os.path.exists(filename)):
        print('file is already exists')
    else:
        file_create = open(filename,'w')
        
        
        
def main():
    print('Enter the file you want to create :')
    file_name=input()
    createfile(file_name)

if __name__=="__main__":
    main()