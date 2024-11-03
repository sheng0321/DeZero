import numpy as np
# create a variable class

class Variable:
    # constructor
    def __init__(self, data):
        self.data =data
# create a NumPy array with single value
data = np.array(1.0)
x = Variable(data)
#string format method
print(f'first {x.data}')
#new data
x.data = np.array(2.0)
#use multiple parameters in the print function to concatenate strings and other data types. The print function automatically adds a space between each parameter, making it easy to combine them into a single output.
print('new:',x.data)

#ndim is number of dimensions
x = np.array(1)
print('dimensions',x.ndim)

x = np.array([1,2,3])
print('dimensions',x.ndim)

x = np.array([[1,2,3],[4,5,6]])
print('dimensions',x.ndim)