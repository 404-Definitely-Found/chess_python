def fun(a):
    length = len(a)
    print(type(length))
    b=""
    d = {'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
    for i in range(length):
        b += d[a[i]]
    print(b)

n=int(input("Enter number = "))
s = str(n)
fun(s)    