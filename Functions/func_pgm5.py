def sum(a,b=2,*c,**d):
    print("a: ",a,"b: ",b)
    print("c: ",end=' ')
    for i in c: print(i,end=' ')
    print("\nd: ",end=' ')
    for k, v in d.items(): print("({}={})".format(k,v),end=' ')
    print()

sum(1,2,3,4,5,6,7,x=2,y=4,z=9)  #a:  1 b:  2
                                #c:  3 4 5 6 7 
                                #d:  (x=2) (y=4) (z=9)

sum(1,2)

sum(1,2,3,4)
sum(1,2,x=9)
