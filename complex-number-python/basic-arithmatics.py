z1 = complex(1, 2)  # create a complex number with real part 1 and imaginary part 2
z2 = complex(3, 4)  # create a complex number with real part 3 and imaginary part 4
z3 = z1 + z2  # add z1 and z2
print(z3)  # prints (4+6j)

z1 = complex(1, 2)  # create a complex number with real part 1 and imaginary part 2
z2 = complex(3, 4)  # create a complex number with real part 3 and imaginary part 4
z3 = z1 - z2  # subtract z2 from z1
print(z3)  # prints (-2-2j)

z1 = complex(1, 2)  # create a complex number with real part 1 and imaginary part 2
z2 = complex(3, 4)  # create a complex number with real part 3 and imaginary part 4
z3 = z1 * z2  # multiply z1 and z2
print(z3)  # prints (-5+10j)

z1 = complex(1, 2)  # create a complex number with real part 1 and imaginary part 2
z2 = complex(3, 4)  # create a complex number with real part 3 and imaginary part 4
z3 = z1 / z2  # divide z1 by z2
print(z3)  # prints (0.44+0.08j)

z = complex(3, 4)  # create a complex number with real part 3 and imaginary part 4
magnitude = abs(z)  # calculate the magnitude of z
print(magnitude)  # prints 5.0

import cmath
z = complex(3, 4)  # create a complex number with real part 3 and imaginary part 4
phase = cmath.phase(z)  # calculate the phase of z
print(phase)  # prints 0.93

z = complex(3, 4)  # create a complex number with real part 3 and imaginary part 4
real_part = z.real  # access the real part of z
imag_part = z.imag  # access the imaginary part of z
print(real_part)  # prints 3.0
print(imag_part)  # prints 4.0

z = complex(3, 4)  # create a complex number with real part 3 and imaginary part 4
conjugate = z.conjugate()  # calculate the conjugate of z
print(conjugate)  # prints (3-4j)

import cmath
real_part = 3.0
imag_part = 4.0
z = cmath.complex(real_part, imag_part)  # create a complex number with real part 3 and imaginary part 4
print(z)  # prints (3+4j)
