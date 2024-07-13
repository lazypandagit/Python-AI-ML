import numpy as np

## Creating numpy array

### using arange():
ar = np.arange(1, 17)

### using special arrays

#### using zeros():
arz = np.zeros((3, 3))

#### using ones():
aro = np.ones((4, 4))

#### using zeroeslike():
# - gives a matrix with all elements zero in the dimention of the passed in matrix
arzl = np.zeros_like(aro)

## changing shape of matrix:
### using reshape()
breshaped = ar.reshape(4, 4)
print(f"\n\n{ar=},\n\n{arz=},\n\n{aro=},\n\n{arzl=},\n\n{breshaped=}")

## stacking 2 matrix
### using vstack():
a1 = np.arange(1, 7).reshape(2, 3)
a2 = np.arange(7, 13).reshape(2, 3)

vstk = np.vstack((a1, a2))
print(f"\n\narray 1 is: \n{a1}\n array 2 is \n{a2}\n vertically stacked is \n{vstk}\n")

### using hstack():
b1 = np.arange(13, 7, -1).reshape(3, 2)
b2 = np.arange(6, 0, -1).reshape(3, 2)

hstk = np.hstack((a1, a2))
print(f"array 1 is: \n{b1}\n array 2 is \n{b2}\n horizontally stacked is \n{hstk}\n")
