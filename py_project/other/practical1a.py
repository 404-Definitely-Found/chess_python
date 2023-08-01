#padding and alignment

a=int(input("enter number 1:"))
b=int(input("enter number 2:"))
print("a={0} and b={1}".format(a,b))
print("a={1} and b={0}".format(a,b))
print("a={} and b={}".format(a,b))
print("a={0:3d} and b={1:7d}".format(a,b))
print("a={0:>3d} and b={1:>7d}".format(a,b))
print("a={0:<3d} and b={1:<7d}".format(a,b))
print("a={0:03d} and b={1:07d}".format(a,b))
print("binary={0:b} and hexadecimal={0:x} and octal={0:o}".format(a))
print("binary={0:b} and hexadecimal={0:x} and octal={0:o}".format(2))
print("a={:{}d} and b={:{}d}".format(a,a,b,b))
print("a={:0{}d} and b={:0{}d}".format(a,a,b,b))
print("a={:^5d} and b={:^5d}".format(a,b))
print("a={:^{}d} and b={:^{}d}".format(a,a,b,b))
print("\n")
#mutable and immutable object

#numeric immutable
a=5
b=5
print(id(a))
print(id(b))
a=6
print(id(a))
c=5.1 
d=5.1
print(id(c))
print(id(d)) #different because of precision
e=5+6j
f=5+6j
print(id(e))
print(id(f))
f=5+6.6j
print(id(f))

#strings are immutable
greeting="good"
greeting1="good"
print(id(greeting))
print(id(greeting1))
greeting="morning"
print(id(greeting))

#list is mutable
list1=[1,2]
print(id(list1))
list2=[1,2]
print(id(list2))
list1.append(3)
print(id(list1))

#tuple is immutable
tuple1=(1,2)
print(id(tuple1))
#tuple1.append(3) doesnt exist cause it is immutable
print(id(tuple1))

#set is immutable
set1={1,2,3}
print(id(set1))
#set1[0]=2
set2={1,2,3}
print(id(set2))

#dictionary is mutable
dict1={'1':'one','2':'two','3':'three'}
print(id(dict1))
dict1['3']='four'
print(id(dict1))