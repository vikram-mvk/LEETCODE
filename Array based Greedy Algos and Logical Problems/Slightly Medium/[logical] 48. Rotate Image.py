a=[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
n = len(a)
#Transpose by swapping diagonals. i.,e simply swap i,j but inner loop form i+1 and not 0
for i in range(n):
    for j in range(i+1,n):
      a[i][j],a[j][i]=a[j][i],a[i][j]
      #this will swap the diagonals
    print(a)
#reversing an array
for i in range(n):
    for j in range(n//2):
        a[i][j],a[i][n-1-j]=a[i][n-1-j],a[i][j]
        #this will reverse a row
    print(a)

