""" print ("hello world")
age= 34 """
# learning input
""" name =input("what is your name?  ")
print( "welcome " + name)

//operator
num1= input("enter the next number")
num2= input("enter the  float number")
sumOf=str(int(num1) + float(num2))
print("the sum of numbers" + sumOf)

//strings editor
fullname = "lord of the rings "
fullname1= fullname.find("r")
print(fullname1) """

 #operators 
""" print(7/3)

print(7//3)

print(7%3)
print(7**3) """
""" n=1
while n!=0 :


    unit=input("is your weight in kg(k) or lbs(l)")
    if unit.upper() == "L" or unit.upper() == "K" :
        weight=int(input ("enter your weight"))
    

        if type(weight)== int or type(weight)== float:


            if unit.upper()=="K":
                weight*=2
                print("your weight in lbs is " + str(weight)+ "Lbs")
                n=0
                
            else: 
                weight/=2
                print("your weight in kg is " + str(weight) + "Kg")
                n=0
        else:
             print ("enter an integerr or floating number")   
    else:
            print("your weight must be in kg or lbs")
        
         """
from datetime import datetime ,date
import calculator
import os.path
names= [ "John", "paul","goal", "hoet", "troy"  ]
print (names[-1])

print (names[0:3])
print (names[0:])
names.sort() #arranges in alphabetical
names.reverse() #arranges in reversw order
names.insert(3, "lover")

print(names)

ranger=range(10)
print(ranger)

    #sets order is not promised
sets1= {"A","B","C", "D","B","C", "D" ,"B","C", "D","B","C", "D","K" }
sets2= {"B","C", "D" ,"A","B","C", "D","B","C", "D","B","C", "D" ,"J"}

intersection= sets1&sets2
difference=sets1 -sets2
union = sets1|sets2
difference2=sets2 -sets1



#sets vs s
arrays= ["A","B","C", "D","B","C", "D" ,"B","C", "D","B","C", "D" ]

print (arrays)
print(f"intersection ={intersection}")
print(f"union={union}")
print(f"difference ={difference}")
print(f"difference2={difference2}")

# sets intersection

#dictionaries
dictsa = {1:"A", 2:"B", 3:"C", 4:"D",5:"K" }
print(dictsa[3])
print(dictsa.get(1))
print(dictsa.keys())
print(dictsa.values())
#looping a dictionary 

for key in dictsa:
   
    print (f"key:{key} value:{  dictsa[key]} " )

for item in dictsa:
    print(f" the key is {item} the value:{dictsa[item]} ")

for key,value in dictsa.items():
    print(f"key: {key} value:{value}  ")

l=0
list1= [1,2,3,4,5,6,7,8,9,10,78,67,56,3,4,3,2,46,7,67,2]
lens= len(list1)
for i in list1:
    l+=i
print(f"sum is : {l}  ")
h=0
while h <10:
    print (h)
    h+=1
else:
    print("end")

k=0
while k <10:
    k+=1
    if k<3:
        continue
        print (f" k is {k}")
    else:
        print(f"final k is {k}")
        break
    
def greet(name="Guest", age=-1):
     if age>0:
        print(f"Hello {name} you are {age} years ")
     else:
         
        print(f"Hello {name} you didnt give us your age ")
   
def isAge(age):
    return age>=10   
     
def gender(gen):
    if gen.upper()== "M":
        return"male"
    elif gen.upper()=="L":
        return  "female"
    else:
        return f"the gender entered is wrong "

    
bool= isAge(43) 
print(bool)
gender("m")
greet("Jola",24)

greet("Oola",)
greet("Ola",56)

print(calculator.addition(2,6))

print(calculator.division (12,6))

print(calculator.multiplication(2,6))

print(calculator.subtraction(18,6))

#Classes
class phone:  

    def __init__(self, price, brand):
        self.price=price
        self.brand=brand
    def call(self,number):
        print(f"{self.brand} is calling using {number}")

iphone7= phone(300, "iphone7")
print(iphone7.brand)
print(iphone7.call(4567432345))
print(iphone7) 

class person:
    #property of classs below
    def __init__(self,name,age, location) -> None:
        self.name=name
        self.age=age
        self.location=location
        print( f"Hello {self.name}. you nare now {self.age}. you also live in {self.location} ")
    #behaviour

    def __str__(self) -> str:
        return f"Hello {self.name}. you nare now {self.age}. you also live in {self.location} "


    def call(self,number):
        print(f"{self.name} is calling {number} ")

valen=person("val",45,"Lagos")
valent=person("ale",25,"Lag")
valent.call(4567854)
valen.call(4567854)
print(valent)

#work(ing wwith date

currentDate=datetime.now()
currentDay=date.today()
print(f"unedited date is {currentDate} ")
print(f"edited date is {currentDate.strftime('%d/%m/%Y %H:%M:%S')} ")
print(f"edited date is {currentDate.strftime('%d-%B-%Y %H %M %S')} ")
print(f"edited date is {currentDate.strftime('%d/%b/%y %H:%M:%S')} ")

print(f"undedited day is {currentDay}  ")
print(f"edited day is {currentDay.strftime( '%d %m %y' )} ")
print(f"edited day is {currentDay.strftime( '%d %B %Y' )} ")
print(f"edited day is {currentDay.strftime( '%d %b %y' )} ")

print(date.today)
print(datetime.now().date())

#working with files

#reading from files only r
file1=open("./data.doc","r")
read1=file1.read()
file1.close()

#writing from files only w
file2=open("./data2.doc","w")
file2.writelines(["hello /n","jesus /n", "Flow/n"])
file2.close()

#reading and writing from files only r+
file3=open("./data3.doc","r+")
file3.write("flowserve" + " /n")
file3.write("flow thrjnhsdbvufuvjjslsl;;v''lffkmmfmfmb" + "/n")
file3.write("ghgtrf flow thrjnhsdbvufuvjjslsl;;v''lffkmmfmfmb" + " /n ")
file3.write("dderf flow thrjnhsdbvufuvjjslsl;;v''lffkmmfmfmb" + " /n ")
#read3=file3.readlines() #reads files into A LIST


for lin in file3:
    print(f"{lin} + /n")
#print(read3)


file3.close()

#appending  and reading from files  a+
file4=open("./data4.doc","a+")
file4.write("flowserve " + "/n")
file4.write("flow thrjnhsdbvufuvjjslsl;;v''lffkmmfmfmb" + " /n ")

file4.write("flow thrjnhsdbvufuvjjslsl;;v''lffkmmfmfmb " + "/n")

file4.write("hello flow thrjnhsdbvufuvjjslsl;;v''lffkmmfmfmb"+ "/n")
read4=file4.readlines()

file4.close()

#appending from files  a
file5=open("./data5.doc","a")
file5.write("flowserve")
file5.close()

# openin files using with syntax. you dont need to close files
file6="./data2.doc"

if os.path.isfile(file6):
    with open(file6,"r+")as file:
        print(f"this is {file.read()}")
else:
    print(f"the {file6} doesn't exist  ")
    

    
    
     


