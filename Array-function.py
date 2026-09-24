#using np array:
import numpy as np
arr_from_list = np.array([1, 2, 3, 4, 5])
print("np.array():\n", arr_from_list)

#using np.linspace()
# Generates 5 evenly spaced numbers from 0 to 10
arr_linspace = np.linspace(0, 10, num=5)
print("\n np.linspace():\n", arr_linspace)

#Using np.logspace()
# Generates 4 values evenly spaced from 10^0 (1) to 10^3 (1000)
arr_logspace = np.logspace(0, 3, num=4)
print("\n np.logspace():\n", arr_logspace)

#Using np.arange()
# Starts at 2, stops before 11, increments by 2
arr_arange = np.arange(2, 11, 2)
print("\n np.arange():\n", arr_arange)

#Using np.zeros() and np.ones()
# Generates a 1D array of three zeros
zeros_1d = np.zeros(3)

# Generates a 2D matrix (2 rows, 4 columns) of ones
ones_2d = np.ones((2, 4))

print("\n np.zeros():\n", zeros_1d)
print("\n np.ones():\n", ones_2d)
