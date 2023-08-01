#membership operator
list1=[1,2]
print(1 in list1)
list2=['a','b','c']
print('d' not in list2)
print('a' in list1)
print(1 in list2)

#Bitwise Operator
a=int(input("enter value of first operand:"))
b=int(input("enter value of second operand:"))
print("a&b:{0}".format(a&b))
print("a|b:{0}".format(a|b))
print("a^b:{0}".format(a^b))
print("~b:{0}".format(~b))
print("a<<2:{0}".format(a<<2))
print("a>>2:{0}".format(a>>2))

#Logical Operator
c=True
d=False
print(c and d)
print(c or d)
print(not(c and d))
print(not(c or d))
print(type(c) is type(d))