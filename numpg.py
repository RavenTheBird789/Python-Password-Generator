# numerical password generator

import random

numbers = ['0','1','2','3','4','5','6','7','8','9']

d_list = [random.choice(numbers) for i in range(4)]
print(d_list)
