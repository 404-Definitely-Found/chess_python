# reading a file
f = open('hello.txt','r')
while True:
    print(f.read(2))
    text = f.readline()
    if not text:
        print("over")
        break
f.close()

#writing a file
# f = open('hello.txt','a')
# f.write("hellooo")
# f.close()

#read line
# f = open("hello.txt",'r')
# while True:
#     x = f.readline()
#     if not x:
#         print("nope")
#         break
#     print(x)

# f = open('marks.txt','r')
# i=0
# while True:
#     t = f.readline()
#     i = i+1
#     if not t:
#         print("byby")
#         break
#     m1 = int(t.split(",")[0])
#     m2 = int(t.split(",")[1])
#     m3 = int(t.split(",")[2])
#     print(f"marks of student {i} is {m1}")
#     print(f"marks of student {i} is {m2}")
#     print(f"marks of student {i} is {m3}")
#     p = (m1+m2+m3)/3
#     print("percentage is = {:.2f}".format(p))
#     print(t)


# f = open("hello.txt",'w')
# # methode 1
# text = ["rudra\n" , "jiaval\n" , "rushil\n"]
# f.writelines(text)

# # methode 2
# he = ["rudra" , "jiaval" , "rushil"]
# for t in he:
#     f.write(t + '\n')
# f.close()