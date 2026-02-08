import sympy as sp
import numpy as np

def build_function(expr, variables):
    
    if len(variables) == 1:
        grad = sp.diff(expr, variables[0])
    else:
        grad = (
            sp.diff(expr, variables[0]),
            sp.diff(expr, variables[1])
        )

    f_num = sp.lambdify(variables, expr, "numpy")
    grad_num = sp.lambdify(variables, grad, "numpy")

    return f_num, grad_num