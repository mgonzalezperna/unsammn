import numpy as np
import matplotlib.pyplot as plt

def function1(x):
    return x*x-2
def function2(x):
    return np.log(x)-1
def function3(x):
    return np.cos(x)+1

def get_root(function, method, ext_left, ext_right, *, iterations=None, epsilon=None):
    x = np.linspace(ext_left, ext_right, 200)
    plt.grid(True)
    plt.plot(x, function(x), label='Funcion ingresada')
    if iterations is not None:
        count = 1
        while iterations > 0:
            print("iteracion: " + str(count))
            (ext_left, ext_right, error) = method(function, ext_left, ext_right)
            if error == 0:
                #raise("Already got the root!")
                break
            plt.plot(x, get_straight(ext_left, ext_right, function, x))
            iterations-=1
            count+=1
    elif epsilon is not None:
        count = 1
        method_error = epsilon
        while abs(method_error) >= epsilon:
            print("iteracion: " + str(count))
            (ext_left, ext_right, method_error) = method(function, ext_left, ext_right)
            plt.plot(x, get_straight(ext_left, ext_right, function, x))
            count+=1
    else:
        raise("Theres no cut condition!")
    plt.show()

def get_straight(x1, x2, function, x):
    a = slope(x1, function(x1), x2, function(x2))
    b = constant(a, x1, function(x1))
    return a*x+b

def slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

def constant(slope, x, y):
    return y - (slope*x)

def bisection(function, ext_left, ext_right):
    new_point = (ext_left + ext_right)/2
    error = ext_left - new_point
    print("valor: " + str(new_point))
    print("dif: " + str(error))
    #if both have the same sign, multiply them will result in a value over zero
    if (function(new_point) * function(ext_right)) > 0:
        return_value = (ext_left, new_point, error)
    else:
        return_value = (new_point, ext_right, error)
    return return_value

def secant(function, ext_left, ext_right):
    new_point = ext_left - (function(ext_left)*(ext_right-ext_left))/(function(ext_right)-function(ext_left))
    error = ext_right - new_point
    print("valor: " + str(new_point))
    print("dif: " + str(error))
    return (ext_right, new_point, error)

print(get_root(function1, secant, 0, 2, epsilon = 0.0000001))
print(get_root(function1, secant, 0, 2, iterations = 20))
print(get_root(function2, secant, 1, 3, epsilon = 0.0000001))
print(get_root(function3, secant, 1, 4, epsilon = 0.0000001))
