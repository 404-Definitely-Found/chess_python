f = open("hello.txt",'r')
while True:
    x = f.readline()
    if not x:
        print("nope")
        break
    print(x)