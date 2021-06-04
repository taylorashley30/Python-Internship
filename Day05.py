'''
# class
class Main:
    def myfunction(self):
        print("This is my function of class")

    def disp(self, name):
        print("Name is: ", name)



 obj = Main()
 obj.myfunction()
 obj.disp("Ashley Taylor")
'''


'''
# sum using class
class SumNum:
    def sum(self, a, b):
        ans = a + b
        print("Answer is: ", ans)


obj = SumNum()
obj.sum(10, 20)
'''

'''
# python constructors
# default constructors
class Main:
    def myfunction(self):
        print("This is my function of class")

    def disp(self, name):
        print("Name is: ", name)

    def _init_(self):
        print("This is default constructors")


obj = Main()
obj.myfunction()
obj.disp("Nobara Kugisaki")

# parameterized constructors
class Main:
    def myfunction(self):
        print("This is my function of class")

    def disp(self, name):
        print("Name is: ", name)

    def _init_(self, nm):
        print("This is default constructors")
        print("Name is ", nm)


obj = Main(input("Parameter: "))
obj.myfunction()
obj.disp("Yuji Itadori")
'''

'''
# assign string value tp class variable using method
class Demo:
    name = ""

    def func_1(self):
        print("Function 1.")

    def func_2(self, name):
        self.name = name

    def disp(self):
        print("Name is : ", self.name)


obj = Demo()
obj.func_1()
obj.func_2("Satoru")
obj.disp()
'''

'''
# Assign string value to class variable using constructor
# eg 1
class Demo:
    name = ""

    def _init_(self, name):
        self.name = name

    def func_1(self):
        print("Name is : ", self.name)


obj = Demo("Megumi")
obj.func_1()

# eg 2
class Demo:
    a = 0
    b = 0

    def _init_(self, a, b):
        self.a = a
        self.b = b

    def func_1(self):
        sum = self.a + self.b
        print("Answer is: ", sum)


obj = Demo(20, 20)
obj.func_1()
'''

# inheritence
'''
# single level inheritence
class Parent:
    def _init_(self):
        print("Parent Constructor")

    def func_1(self):
        print("Parent class..")

class Child(Parent):
    def  _init_(self):
        print("Child Constructor")

    def func_2(self):
        print("Child class..")


obj = Child()
obj.func_1()
obj.func_2()

# multi level inheritnce
class Parent:
    def _init_(self):
        print("Parent Constructor")

    def func_1(self):
        print("Parent class..")

class Child(Parent):
    def _init_(self):
        print("Child Constructor")

    def func_2(self):
        print("Child class..")

class SubChild(Child):
    def func_3(self):
        print("Sub Child class..")


obj = SubChild()
obj.func_1()
obj.func_2()
obj.func_3()

# multiple inheritence
class Demo1:
    def _init_(self):
        print("Parent Constructor")

    def func_1(self):
        print("Parent class..")

class Demo2:
    def  _init_(self):
        print("Child Constructor")

    def func_2(self):
        print("Child class..")

class Demo(Demo1, Demo2):
    def func_3(self):
        print("Multiple inheritence")


obj = Demo()
obj.func_1()
obj.func_2()
obj.func_3()

# heirarchical inheritence
class Parent:
    def _init_(self):
        print("Parent Constructor")

    def func_1(self):
        print("Parent class..")

class Child(Parent):
    def  _init_(self):
        print("Child Constructor")

    def func_2(self):
        print("Child class..")

class Child2(Parent):
    def func_3(self):
        print("Heirarchical inheritence")


obj = Child()
obj.func_1()
obj.func_2()

obj2 = Child2()
obj2.func_1()
obj2.func_3()
'''


# polymorphism
'''
# overriding method
class Parent:
    def func_1(self):
        print("Parent class..")

class Child(Parent):
    def func_1(self):
        print("Child class..")


obj = Child()
obj.func_1()
'''

# overloading
class Math:
    def sum(self, a, b):
        ans = a + b
        print("Answer is: ", ans)

    def sum(self, a, b, c):
        ans = a + b + c
        print("Answer is: ", ans)


obj = Math()
# obj.sum(10, 20)
obj.sum(10, 20, 30)