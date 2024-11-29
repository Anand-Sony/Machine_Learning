import numpy as np

decimalArray = np.array([1,2.54,1.88112,0.16112,8.002222])

roundDecimalArray = np.round(decimalArray , decimals=1)
print(roundDecimalArray)  # Output: [1.  2.5 1.9 0.2 8. ]