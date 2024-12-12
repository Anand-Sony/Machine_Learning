import numpy as np
import scipy 

print("Version of SciPy", scipy.__version__)

from scipy import constants, special
result_add = np.add(5,3)
result_exp = np.exp(2)
result_bessel = special.jn(2,3)
# Bessel functions are a set of mathematical functions that are used to describe the behavior of waves and other
# oscillatory phenomena.

print("Addition :", result_add)
print("Exponential :", result_exp)
print("Bessel function :", result_bessel)