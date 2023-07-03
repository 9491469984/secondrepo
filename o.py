def consecutiveSum(a):
    
    na=[]
    for i in range(len(a)):
        if len(a) ==1:
            break
        elif len(na)==len(a)-1:
            print(na)
            a = na
            consecutiveSum(a)
        else:
            cs=a[i]+a[i+1]
            na.append(cs)

a=[3, 5, 7, 9]
print(a)
consecutiveSum(a)
