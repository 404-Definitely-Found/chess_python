sum=0
print("enter student marks:")
for i in range(5):
    j=int(input("enter marks of subject {0}:".format(i)))
    sum+=j

perc=float(sum/5)

if (perc>=90):
    print("your percentage is {0} and grade is A+".format(perc))
elif (perc>=80 and perc<90):
    print("your percentage is {0} and grade is A".format(perc))
elif (perc>=70 and perc<80):
    print("your percentage is {0} and grade is B+".format(perc))
elif (perc>=60 and perc<70):
    print("your percentage is {0} and grade is B".format(perc))
elif (perc>=50 and perc<60):
    print("your percentage is {0} and grade is C+".format(perc))
elif (perc>=40 and perc<50):
    print("your percentage is {0} and grade is C".format(perc))
else :
    print("Fail")