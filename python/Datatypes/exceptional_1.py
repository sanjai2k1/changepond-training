student_id = [123,124,125,126]
try:
    for i in range(4):
        print(i,'-',student_id[i])
except:
    print('Index out of range')