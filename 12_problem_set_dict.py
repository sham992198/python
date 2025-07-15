# to create dictionary hindi word with value as their english translation. provide user option
words = {
    "billi":"cat",
    "dog":"kutta",
    "man":"manav"
}
print(words)

# to input eight number from the users and display all the unique number
n = set()
m = input("enter no:")
n.add(int(m))
m = input("enter no:")
n.add(int(m))
m = input("enter no:")
n.add(int(m))
m = input("enter no:")
n.add(int(m))
m = input("enter no:")
n.add(int(m))
m = input("enter no:")
n.add(int(m))
m = input("enter no:")
n.add(int(m))
m = input("enter no:")
n.add(int(m))
print(n)

# can we have set as int 18 and str "18" in value in it
s = set()
s.add(int(18))
s.add("18")
print(s)  

# what wii be the lenght of program
# s = set()
#s.add(20)
#s.add(20.0)
#s.add("20")

s = set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))

# S={}
#What is type of 's'
s = {}
print(type(s))

# create an empty dictionary.allow 4 friend to their fev language as value and use key their name.
#assume that the name are unique
d = {}
names = input("Enter name:")
lang = input("enter lang:")
d.update({names:lang})
names = input("Enter name:")
lang = input("enter lang:")
d.update({names:lang})
names = input("Enter name:")
lang = input("enter lang:")
d.update({names:lang})
names = input("Enter name:")
lang = input("enter lang:")
d.update({names:lang})
print(d)