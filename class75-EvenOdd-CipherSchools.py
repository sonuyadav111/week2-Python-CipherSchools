def odd_even(num):
    if num%2==0:
        return "even"
    else:
        return "odd"
a=int(input("Enter a number: "))
print(odd_even(a))
