dp=[[30,25,16,7,8,9],[29,24,15,6,1,2],[28,23,14,5,4,3],
[27,22,13,12,11,10],[26,21,20,19,18,17]]

rows = 5
cols = 6
rStart = 1
cStart = 4


EW=[]
EWCheck = cols-1
i,j = rStart+1,cStart+1
while EWCheck>0:
    EW.append([i,j])
    i+=1
    j+=1
    EWCheck-=1
print(EW)

WE=[]
WECheck =cols-1
i,j = rStart-1,cStart-1

while WECheck>0:
    WE.append([i,j])
    i-=1
    j-=1
    WECheck-=1
print(WE)
  
  
SN = []
SNCheck =cols-1
i,j = rStart+1,cStart-1

while SNCheck>0:
    SN.append([i,j])
    i+=1
    j-=1
    SNCheck-=1
    
print(SN)

NS=[]
NSCheck = cols-1
i,j = rStart-1,cStart+1

while NSCheck>0:
    NS.append([i,j])
    i-=1
    j+=1
    NSCheck-=1

print(NS)

        


