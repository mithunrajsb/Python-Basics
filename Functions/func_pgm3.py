def si(p,t,r):
    print("Interest: ",(p*t*r)/100)


si(1000,3,9.5)  # 285
si(p=1000,r=9.5,t=3)  # 285
si(1000,r=9.5,t=3)   # 285