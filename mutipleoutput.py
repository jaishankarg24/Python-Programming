def calc(x,y):
    '''this function will perform add,mul,div,sub'''
    #print(calc.__doc__)
    help(calc)
    a=x+y
    b=x-y
    c=x*y
    d=x/y
    return(a,b,c,d)
p=20
q=10
res1,res2,res3,res4=calc(p,q)
print(res1,res2,res3,res4)
