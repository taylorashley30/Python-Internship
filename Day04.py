'''
def myfunction(name):
    print("Hello World")
    print("Name is:",name)

myfunction("Ashley")
'''

'''
def myfunction():
 name="Megumi"
 n1=20
 return  name,n1

name,n1=myfunction()
print("Name is ",name)
print("n1 is ",n1)
'''

'''
def calSum(n1=100, n2=200):
    print(n1+n2)

calSum(10,20)
calSum()
'''

'''
def sum(a,b):
    print("Sum is:",a+b)
sum(b=240,a=20)
'''
'''
def calSum(n1, n2):
    print(n1+n2)

calSum(n2=10, n1=20)
'''

'''
def sum(*n1):
    sum=0
    for i in n1:
        sum=sum+i
    print("Ans is ",sum)
sum(10,20)
sum(10,20,30)
'''

'''
def myfunction(**arg):
    for i,j in arg.items():
        print(j)

myfunction(name="Maki", nm="Yuta")
'''

'''
def add(*num):
    sum=0
    for n in num:
        sum=sum+n
    print("Sum:",sum)
add(120,30)
add(23,12,45)
'''

'''
def my_func():
    x=10
    print("Value inside function:",x)
x=20
my_func()
print("Value outside function:",x)
'''

import Day04_demo 
name=Day04_demo.myfunction("Kakashi")
print("Name is ",name)
