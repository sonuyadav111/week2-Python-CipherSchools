def rev_list(l):
    reversed=[]
    for i in range(len(l)):
        a=l.pop()
        reversed.append(a)
    return reversed
b=[1,2,3,4]
print(rev_list(b))



