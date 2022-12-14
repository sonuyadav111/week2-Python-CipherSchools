def rev_strings(l):
    lst=[]
    for i in l:
        a=i[::-1]
        lst.append(a)
    return lst    
v=["Harshit","Shivank","Srivastava"]
print(rev_strings(v))
    