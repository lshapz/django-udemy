# VARIABLES
age = 12
print(age)
name = "Laura"
# I don't think strings are truthy 

""" multi line comment
"""
print(name)
fullname = "Laura Rachel Cohen Shapiro"
print(fullname[13:18])
print("hello my name is {} and I am {}".format(name, age))

# CONDITIONALS 
today = True
cold = False

if name == "Laura":
  print("name")
else:
  print("no good")

if today:
  print("truth")
else: 
  print("false")

if age > 18:
  print("welcome to the ride")
else:
  print('baby')

# FUNCTIONS
def hello():
  print("Hello World")

hello()

def hey(name):
  print("Hello " + name)

hey("Laura")

def sup(name="World", age=0):
  print("Hello {} you are {} years old".format(name, age))

sup()
sup("Laura")
sup("Laura", 29)

def hi(name):
  return name

returned = hi("Laura")
print(returned)

def tripleprint(string):
    print(string+string+string)
tripleprint("Laura")

# LISTS (ARRAYS)
dognames = ["Snoopy", "Maralynn", "Spot", "Coda"]
print(dognames)
dognames.insert(0, "Scooby")
print(dognames)
dognames.insert(4, "Peanut")
print(dognames)
print(dognames[2])
del(dognames[3])
print(dognames)
# dognames.insert(-1, "Phillip")
# -1 is getting me penultimate, -0 is getting me first
# print(dognames)
print(len(dognames))
dognames.insert(len(dognames), "James")
# there's for last
print(dognames)
dognames[5] = "Jimmy"
print(dognames)

# LOOPS 

dognames = ["Snoopy", "Maralynn", "Spot", "Scooby"]

for dog in dognames: 
  print(dog)

for x in range(1, 1000):
  print(x)
# non inclusive last # - length 

age = 0 
while age < 18:
  print(age)
  age += 1

# DICTIONARIES hashes objects 

dogs = {"Maralynn": 12, "Scooby": 45, "Fido": 69}

print(dogs)
print(dogs["Scooby"])
del(dogs["Fido"])
print(dogs)
dogs["Mine"] = False
print(dogs)
dogs["Mine"] = True
print(dogs)

# CLASSES

class Dog:
  doginfo = "Dogs are Cool"

  def bark(self):  # passes object in as variable
    print("BARK!")
  
  def woof(self, string):
    print("WOOF " + string)
  
fido = Dog()
fido.bark()
# dynamically add instance variables
fido.name = "Fido"
fido.age = "6"
print(fido.name)
print(fido.age)
print(Dog.doginfo)
Dog.doginfo = "Dogs are AWESOME"
print(Dog.doginfo)
fido.woof('WOOF')

class Dog2:
  doginfo = "Dogs are Cool"

  def __init__(dag, name = "", age = 0, fur = ""):
    dag.name = name
    dag.age = age
    dag.fur = fur

  def bark(dag):  # passes object in as variable
    print("BARK!")
  
  def woof(dag, string):
    print("WOOF " + string)

bud = Dog2()
bud.name = "Pal"
print(bud.name)
pal = Dog2('Buddy', 10, "gray")
print(pal.name)
print(pal.age)
print(pal.fur)
pal.bark()
pal.woof("woof")
# you _can_ rename self as above, but why bother

