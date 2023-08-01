def modify(st):
    st1 = st[0]
    for i in range(1,len(st)):
        if  st[i]==st[i-1] :
            st1+='*'
        else :
            st1+=st[i]
    print(st1)    
str = input("Enter a string : ")
modify(str)
