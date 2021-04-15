import numpy as np
import copy
import random
from client import *

secret_key = "xfynomZku5eRSx4RmkKm8MUdiunDaxJiAUyNS0VUnSN5s9eWCv"

overfit_file = open('./overfit_now.txt' , 'r')
initial_weight = overfit_file.read()
overfit_file.close()

initial_weight = initial_weight[1:len(initial_weight) - 1]
initial_weight = initial_weight.replace(" ","")
initial_weight = initial_weight.split(',')
initial_weight = list(map(float, initial_weight))
initial_w = np.array(initial_weight)

errors  = get_errors(secret_key , list([-5.44897788e-13 ,-2.39320228e-07 , 1.54009038e-12 , 1.09381114e-06
  ,-2.49609150e-14 , 0.00000000e+00 ,-4.79219068e-18 ,-1.85823970e-13
   ,7.45912001e-12 , 8.74441901e-17 ,-9.50795943e-11]))

# [ 7.45912001e-12 -2.39320228e-07  1.74195676e-12  5.38497567e-07
  # -2.49609150e-14  0.00000000e+00 -4.79219068e-18 -1.85823970e-13
#   # -5.44897788e-13  8.74441901e-17 -9.50795943e-11] 
# [ 7.45912001e-12, -3.80419473e-07 , 1.28140365e-12 , 1.09381114e-06
#   ,-2.49609150e-14 , 0.00000000e+00, -4.79219068e-18 ,-1.85823970e-13
#   ,-5.44897788e-13 , 8.74441901e-17, -9.50795943e-11] 

# [-9.922808990278071e-14, 0.0, 1.6550543534994243e-16, -1.739566433305385e-11, 1.1731227359041937e-11, -5.187780215086327e-13, -7.688096996531447e-09, 1.2315239803294492e-05, -3.3088748077244316e-07, -5.389187016082068e-17, 6.529135878417431e-11]
print(errors)