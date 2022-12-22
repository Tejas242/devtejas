# Representing complex numbers in Python

# Create a complex number using the complex() function
z = complex(3, 4)  # 3+4i
print(z)

# You can also create a complex number using the 'j' notation
z = 3 + 4j
print(z)

# Extracting the real and imaginary parts of a complex number
real_part = z.real  # 3
imag_part = z.imag  # 4

# You can also use the conjugate() method to get the conjugate of a complex number
conj_z = z.conjugate()  # 3-4j

# Converting between polar and rectangular coordinates

# To convert from rectangular to polar coordinates, you can use the cmath module
import cmath

# Convert from rectangular to polar coordinates
r, theta = cmath.polar(z)
print(f'r = {r}, theta = {theta}')  # r = 5, theta = 0.93

# To convert from polar to rectangular coordinates, you can use the rect() function
x, y = cmath.rect(r, theta)
print(f'x = {x}, y = {y}')  # x = 3.0, y = 4.0
