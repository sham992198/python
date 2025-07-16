# # if elif else cond

a =int(input("enter no:"))
if(a>10):
    print("a is boss")
elif(a<5):
    print("a is small boss")
elif(a==0):
    print("a is not boss")
else:
    print("noooo")

a = int(input("enter no:"))
if(a%2==0):
    print("even")
if (a>=18):
    print("yes")
else:
    print("no")


# problem solve
# to find 4 greatest no.entered by the user

a1 =int(input("enter:"))
a2 =int(input("Enter no 2:"))
a3 =int(input("Enter no 3:"))
a4 =int(input("Enter no 4:"))
if(a1>a2 and a1>a3 and a1>a4):
    print("greatest no:",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("graeter no:",a2)
elif(a3>a1 and a3>a2 and a3>a4):
    print("graeter no:",a3) 
else:
    print("greater are:",a4)

# to find student are passed and failed and it require atleast 40% to pass and 33% ot pass each subject
# assume 3 subject and take mark as a input from the user  
a =int(input("enter marks:"))
b =int(input("enter marks:"))
c =int(input("enter marks:"))
total_percentage = (a+b+c)/300*100
if(total_percentage>=40 and a>=33 and b>=33 and c>=33):
    print("pass",total_percentage)   
else:
    print("fail",total_percentage)

# a spam comment in define as a text containing following keyword.
# "make lot of money","buy now","click this".
x = input("enter massege:")
if(x=="make a lot of money" or x=="buy now" or x=="subscribe now" or x=="click this"):
    print("spam")
else:
    print("not spam")

# to find given username contian less than 10 character or not
a =input("enter:")
names=len(a)<10
if(names):
    print("good")
else:
    print("to long")

# find out whether given name are present in list or not

A=("sham","ram","jonhy","rahul")
b = input("give name:")
if(b in A):
    print("present")
else:
    print("not")

# calc grade student of his marks from the list
# 90-100=ex
# 80-90=A
# 70-80=B
# 60-70=C
# 50-60=D
# <50=fail
a = int(input("enter no:"))
if(a>=90):
    print("ex")
elif(a>=80):
    print("A")
elif(a>=70):
    print("B")
elif(a>= 60):
    print("c")
elif(a>50):
    print("D")
else:
    print("fail")

#check whether given post is about harry or not
B = ("harry is good boy")
c = input("check name :")
if(c in B):
    print("this post is about harry")
else:
    print("this is not about:",c)
