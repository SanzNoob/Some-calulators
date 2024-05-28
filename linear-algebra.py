# Some linear algebra // algebra lineal. 

def basic_linear_calculation(n, x, y):              #  n[x,y] = [n(x), n(y)]
    calculate_x = int(n*x)
    calculate_y = int(n*y)
    result_ = f"[{calculate_x}\n{calculate_y}]"
    return result_
    
    
print(basic_linear_calculation(5, 20, 43))


def another_basic_linear_calculation(x1, y1, x2, y2):
    calculate_x = x1 + x2
    calculate_y = y1 + y2
    result_ = f"[{calculate_x}\n{calculate_y}]"
    return result_
    
    
print(another_basic_linear_calculation(21, 34, 90, 67))

# 2x2 matrix:

def two_x_two_matrix(x, a, c, y, b, d):
    calculate_a_b = x*a + y*b
    calculate_c_d = x*c + y*d
    result_ = f"[{calculate_a_b}\n{calculate_c_d}]"
    return result_

print(two_x_two_matrix(2, 12, 32, 3, 54, 11))    
    
    
