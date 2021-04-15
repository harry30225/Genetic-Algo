import numpy as np
import copy
import random
from client import *

secret_key = "xfynomZku5eRSx4RmkKm8MUdiunDaxJiAUyNS0VUnSN5s9eWCv"

# Initial Vector to Create Initial Population
overfit_file = open('./overfit_now.txt' , 'r')
initial_weight = overfit_file.read()
overfit_file.close()

initial_weight = initial_weight[1:len(initial_weight) - 1]
initial_weight = initial_weight.replace(" ","")
initial_weight = initial_weight.split(',')
initial_weight = list(map(float, initial_weight))
initial_w = np.array(initial_weight)

initial = [-5.44897788e-13 ,-2.39320228e-07 , 1.54009038e-12 , 1.09381114e-06
  ,-2.49609150e-14 , 0.00000000e+00 ,-4.79219068e-18 ,-1.85823970e-13
   ,7.45912001e-12 , 8.74441901e-17 ,-9.50795943e-11]
# Best 
# [0.00000000e+00 ,0.00000000e+00 ,0.00000000e+00, 0.00000000e+00
#   ,0.00000000e+00 ,0.00000000e+00 ,0.00000000e+00, 0.00000000e+00
#   ,0.00000000e+00, 1.13293645e-12 ,0.00000000e+00] 
# [0.00000000e+00 ,2.65741970e-12 ,0.00000000e+00, 0.00000000e+00
#   ,0.00000000e+00 ,0.00000000e+00 ,0.00000000e+00, 0.00000000e+00
#   ,0.00000000e+00, 8.01287500e-13 ,0.00000000e+00]
#  Best 2
# [0.00000000e+00 ,0.00000000e+00 ,0.00000000e+00, 0.00000000e+00
#   ,0.00000000e+00 ,1.75142475e-12 ,0.00000000e+00, 0.00000000e+00
#   ,0.00000000e+00, 0.00000000e+00 ,0.00000000e+00]
# Best 3
#  [0.00000000e+00 ,2.65741970e-12 ,0.00000000e+00, 0.00000000e+00
#   ,0.00000000e+00 ,0.00000000e+00 ,0.00000000e+00, 0.00000000e+00
#   ,0.00000000e+00, 0.00000000e+00 ,0.00000000e+00] 
# Submit Request

submit_stat = submit(secret_key , list(initial))

print(submit_stat)