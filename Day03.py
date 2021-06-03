'''
a=int(input("Enter first no:"))
b=int(input("Enter second no:"))
ans=a+b
print("Ans is:",ans)
'''

'''
n1=200
n2=30
if n1>n2:
    print("n1 is greater")

if n1<n2:
    print("n2 is greater")
'''

'''
n1=20
n2=30
if n1>n2:
    print("n1 is greater")

else:
    print("n2 is greater")
'''

'''
n1=20
n2=30
if n1==n2:
    print("Both n1 and n2 are equal")

elif n1>n2:
    print("n1 is greater")    

else:
    print("n2 is greater")
'''

'''
n1=10

if n1>=0:
    if n1==0:
        print("n1 is Zero")
    else: 
        print("n1 is Positive")
else:
    print("n1 is Negative")
'''

'''
i=1
while i<=10:
     print("value is ", i)
     i +=1
'''

'''
for i in "Hello":
    print(i)
'''

'''
l1=[30,40,'hey!']
print(l1)
for i in l1:
    print("value is ",i)
'''

'''
for i in range(10):
    print("value is", i)
print("These are values of i\n")

for j in range(1,5):
    print("value is", j)
print("These are values of j\n")

for k in range(1,10, 2):
    print("value is", k)
print("These are values of k\n")
'''

'''
list1 = [10, 20, "Yuji"]

for i in range(len(list1)):
    print('Value is :', list1[i])
'''

'''
a=[12,14,"Nobara"]
print(a)

for i in a:
    print("Value is ",i)

for j in range(len(a)):
    print("Value is ",a[j])
'''
'''
list1 = [10, 20, "Netflix"]
for i in range(len(list1)):
    print('Value is :', list1[i])
else:
        print("No elements left.")
'''

'''
i=0
while i<10:
    print("Value is:",i)
    i +=1
    if i>=5:
        break
'''

for x in range(10):
    if x%2==0:
        continue
    print("Value is:",x)