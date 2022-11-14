a=int(input("Enter a number : "))
l=[]
while a:
    l.append(a%10)
    a=int(a/10)
print(l)