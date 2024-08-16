grid = [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
row = len(grid)
col = len(grid[0])
cnt=0
for i in range(0,row):
    for j in range(0,col):
        if i-1>-1 and j-1>-1 and i+1<row and j+1 <col:
            uniq = set([grid[i][j],grid[i][j+1],grid[i][j-1],grid[i-1][j],grid[i+1][j],grid[i-1][j-1],grid[i-1][j+1],grid[i+1][j-1],grid[i+1][j+1]])
            diagonal1 = grid[i][j]+grid[i-1][j-1]+grid[i+1][j+1]
            diagonal2 = grid[i][j]+grid[i-1][j+1]+grid[i+1][j-1]
            rowsum = grid[i][j]+grid[i][j-1]+grid[i][j+1]
            colsum = grid[i][j]+grid[i-1][j]+grid[i+1][j]
            rowdownsum = grid[i+1][j-1]+grid[i+1][j]+grid[i+1][j+1]
            rowupsum = grid[i-1][j-1]+grid[i-1][j]+grid[i-1][j+1]
            colleftsum = grid[i][j-1]+grid[i-1][j-1]+grid[i+1][j-1]
            colrightsum = grid[i][j+1]+grid[i-1][j+1]+grid[i+1][j+1]
            if len(uniq)==9 and diagonal1==15 and diagonal2==15 and rowsum==15 and colsum==15 and rowdownsum==15 and rowupsum==15 and colleftsum==15 and colrightsum ==15:
                print(i,j)
                cnt+=1
                
print(cnt)
                