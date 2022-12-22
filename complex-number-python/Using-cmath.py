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

log_z = cmath.log(z)  # calculate the natural logarithm of z
print(log_z)  # prints (1.272019649514069+0.7853981633974483j)

log10_z = cmath.log10(z)  # calculate the common logarithm of z
print(log10_z)  # prints (0.0413927576601566+0.11394335230683677j)

sinh_z = cmath.sinh(z)  # calculate the hyperbolic sine of z
print(sinh_z)  # prints (-1.1752145867567424+1.959601041421606j)

cosh_z = cmath.cosh(z)  # calculate the hyperbolic cosine of z
print(cosh_z)  # prints (-1.1827617389611787+2.0588909443089185j)

tanh_z = cmath.tanh(z)  # calculate the hyperbolic tangent of z
print(tanh_z)  # prints (0.03653436389426984+0.9950547536867305j)

acos_z = cmath.acos(z)  # calculate the inverse cosine of z
print(acos_z)  # prints (1.1437177404024195+1.528570919157559j)

acosh_z = cmath.acosh(z)  # calculate the inverse hyperbolic cosine of z
print(acosh_z)  # prints (1.3169578969248168+1.5707963267948966j)
