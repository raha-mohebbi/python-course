# allows us to perform mathematical operations on numbers,
# such as addition, subtraction, multiplication, and division

def raise_to_power(base_num, power_num):
    result = 1
    for index in range(power_num):
        result = result * base_num
    return result

print(raise_to_power(3, 2))