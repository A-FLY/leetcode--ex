x=[1,2,3,4,5,6,7,8,9]
for i in range(1,len(x)+1):
    for j in range(i,len(x)+1):
        y=i*j
        print("{}*{}={:2}\t".format(i,j,y))
    print()
    
