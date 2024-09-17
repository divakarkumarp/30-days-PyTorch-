## ---------------------Tensor Basic-----------------------------------------------
import torch

# Initialize an empty tensor with uninitialized values, of size 3
# x = torch.empty(3)
# tensor([1.1072e+20, 1.5064e-42, 0.0000e+00])

# Initialize a 2x3 empty tensor with uninitialized values
# x = torch.empty(2, 3)
# tensor([[-3.7151e+27,  1.6900e-42,  0.0000e+00],
#         [ 0.0000e+00,  0.0000e+00,  0.0000e+00]])

# Initialize a 2x2x2x3 empty tensor with uninitialized values
# x = torch.empty(2, 2, 2, 3)

# Initialize a 2x2 tensor filled with zeros
# x = torch.zeros(2,2)
# tensor([[0., 0.],
#         [0., 0.]])

# Initialize a 2x2 tensor filled with ones
# x = torch.ones(2,2)
# tensor([[1., 1.],
#         [1., 1.]])

# Initialize a 2x2 tensor filled with ones and set the data type to double
# x = torch.ones(2,2, dtype=torch.double)
# print(x.dtype)

# Initialize a 2x2 tensor filled with ones and set the data type to float16
# x = torch.ones(2,2, dtype=torch.float16)
# print(x.size())

# Initialize a tensor with specific values [2.5, 0.1]
# x = torch.tensor([2.5, 0.1])
# tensor([2.5000, 0.1000])
# print(x)

# Initialize two 2x2 tensors with random values
# x = torch.rand(2,2)
# y = torch.rand(2,2)

# Print the values of tensors x and y
# print(x)
# print(y)

# Add tensors x and y element-wise (two methods: direct addition and using torch.add)
# z = x + y
# z = torch.add(x,y)
# print(z)

# Add tensor x to y in-place
# y.add_(x)

# Subtract tensor y from x element-wise
# z = x - y
# z = torch.sub(x, y)

# Multiply tensors x and y element-wise
# z = x * y
# z = torch.mul(x, y)

# Divide tensor x by y element-wise
# z = x / y
# z = torch.div(x, y)

# Print the resulting tensor z after division
# print(z)

# Initialize a 5x3 tensor with random values
# x = torch.rand(5, 3)
# print(x)
# Access and print the value at the second row, second column
# print(x[1, 1])
# Convert the accessed value to a Python number and print it
# print(x[1, 1].item())

# Initialize a 4x4 tensor with random values
#x = torch.rand(4,4)
#print(x)

# Reshape the 4x4 tensor into a 1D tensor of size 16 (commented out)
# y = x.view(16)

# Reshape the 4x4 tensor into a 2D tensor with 8 columns, and automatically infer the number of rows
#y = x.view(-1, 8)

# Print the size of the reshaped tensor
#print(y.size())

import numpy as np
#a = torch.ones(5)
#print(a)
#b = a.numpy()
#print(b)

#a.add_(1)
#print(a)
#print(b)

'''
a = np.ones(5)
print(a)
b = torch.from_numpy(a)
print(b)

a +=1
print(a)
print(b)'''

'''
# Check if CUDA (GPU support) is available
if torch.cuda.is_available():
    # Set the device to GPU (CUDA)
    device = torch.device("cuda")
    
    # Create a tensor of ones directly on the GPU
    x = torch.ones(5, device=device)
    
    # Create a tensor of ones on the CPU by default
    y = torch.ones(5)
    
    # Move the tensor from CPU to GPU
    y = y.to(device)
    
    # Perform addition of the two tensors on the GPU
    z = x + y
    
    # Move the result tensor back to the CPU
    z = z.to("cpu")
    '''

x = torch.ones(5, requires_grad=True)
print(x)