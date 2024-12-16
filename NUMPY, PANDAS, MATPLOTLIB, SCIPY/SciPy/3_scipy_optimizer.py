from scipy.optimize import minimize_scalar

def quadratic_function(x):
    return (x-3)**2 + 5

result = minimize_scalar(quadratic_function)
print(result.x)  # Output: 3.0

# The minimize_scalar function is used to minimize a scalar function. It returns the minimum value 
# of the function and the x-value at which this minimum occurs.

print(result.fun) # Output: 5.0
# result.fun is the minimum value of the function, which is 5.0 in this case



# now differential Evolution : 
from scipy.optimize import differential_evolution
def global_objective(x):
    return x[0]**2 + x[1]**2
# The global_objective function is a simple function that takes a 2D vector as input and
# returns the sum of the squares of its components.
result = differential_evolution(global_objective, [(-2,2) , (-2,2)])
#2D space where -2 <= x <= 2 and -2 <= y <=2

print(result.x)  # Output: [0. 0.]
# The result.x is the vector that minimizes the global_objective function, which is [0. 0.] in this case
print(result.fun) # Output: 0.0
