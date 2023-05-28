def sum(a,b):
    if b>0:
        a=a+1
        b=b-1
        return sum(a,b)
    else:
        return a


print(sum(2, 6))