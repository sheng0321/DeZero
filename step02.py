import numpy as np
class Variable:
    def __init__(self,data):
        self.data = data

#define a function class
# class Function:
#     def __call__(self, input):
#         x=input.data
#         y= x**2
#         output = Variable(y)
#         return output
# data = np.array(1.0)
# # instance the function
# f=Function()
# print('f type',type(f))
# #call the function and pass the data
# y=f(Variable(data))
# print('y type',type(y))
# print(y.data)
#define a function parent class
class Function:
    def __call__(self,input):
        x=input.data
        #forward method will be implemented in the child class
        y=self.forward(x)
        output=Variable(y)
        return output
    def forward(self,x):
        #raise an error if the forward method is not implemented
        raise NotImplementedError()
 #inherit from the Function class   
class Square(Function):
    #implement the forward method
    def forward(self,x):
        return x**2
data = np.array(1.0)
x = Variable(data)
f = Square()
print('f type',type(f))
y = f(x)
print(y.data)