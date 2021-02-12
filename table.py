def table(n):
    return lambda x:n*x
n=int(input('enter the num'))
ref=table(n)
for i in range(1,11):
    print(n,'*',i,'=',ref(i))
