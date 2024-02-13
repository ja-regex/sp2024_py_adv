var_1 = input('Please enter an integer:  ')                             # str, '3'
var_2 = input('Please enter another integer:  ')                        # str, '14'

int_var_1 = int(var_1)                                                  # int, 3
int_var_2 = int(var_2)                                                  # int, 14

power = int_var_1 ** int_var_2                                          # int, 4782969
str_power = str(power)                                                  # str, '4782969'
len_power = len(str_power)                                              # int, 7

print('=' * len_power)
print(str_power)
print('=' * len_power)