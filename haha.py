
n = 0
for i in range(1,5) :
    for j in range(1,5):
        for k in range(1,5):
            if(i != j) & (i != k) &(j != k):
                print(i,j,k)
                n +=1
print('一共有' ,n,'种')

