class MyClass:

    __privateVar = 27;

    def __privMeth(self):
        print("Im inside class myClass")

    def hello(self):
        print("Private Variable value:  ",MyClass.__privateVar)

foo = MyClass()
foo.hello()
foo.__privMeth