import numpy as np
import copy
import random

overfit_file = open('./overfit_now.txt' , 'r')
initial_weight = overfit_file.read()
overfit_file.close()

initial_weight = initial_weight[1:len(initial_weight) - 1]
initial_weight = initial_weight.replace(" ","")
initial_weight = initial_weight.split(',')
initial_weight = list(map(float, initial_weight))
initial_w = np.array(initial_weight)

for i in range(20):
    mutate_prob = random.randint(0,10)
    if mutate_prob >= 3 and mutate_prob < 7:
            idx = random.randint(0,5)
            idx_1 = random.randint(6,10)
            initial_w[idx] , initial_w[idx_1] = initial_w[idx_1] , initial_w[idx]   


    elif mutate_prob >= 7:
        idx = random.randint(0,10)
        idx_1 = random.randint(0,10)
        if abs(random.uniform(0.3, 1.6) * initial_w[idx]) < 10:
            initial_w[idx] = random.uniform(0.3, 1.6) * initial_w[idx]
    
        if abs(random.uniform(0.3, 1.6) * initial_w[idx_1]) < 10:
            initial_w[idx_1] = random.uniform(0.3, 1.6) * initial_w[idx_1]


overfit_file = open('./overfit_now.txt' , "w")
overfit_file.write(str(list(initial_w)))
overfit_file.close()    