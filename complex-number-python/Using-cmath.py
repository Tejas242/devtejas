import cmath

z = complex(1, 2)  # create a complex number with real part 1 and imaginary part 2
sin_z = cmath.sin(z)  # calculate the sine of z
print(sin_z)  # prints (3.165778513216168+1.959601041421606j)

cos_z = cmath.cos(z)  # calculate the cosine of z
print(cos_z)  # prints (-1.1673039782614188-2.0588909443089185j)

tan_z = cmath.tan(z)  # calculate the tangent of z
print(tan_z)  # prints (-0.033812089020793736+1.0147936161466338j)

sqrt_z = cmath.sqrt(z)  # calculate the square root of z
print(sqrt_z)  # prints (1.272019649514069+0.7861513777574233j)

exp_z = cmath.exp(z)  # calculate the natural exponent of z
print(exp_z)  # prints (-1.1312043837568135+2.4717266720048188j)
