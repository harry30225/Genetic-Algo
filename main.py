import numpy as np
import copy
import random
from client import *

# global variables and functions
genaration_size  = 10
validate_factor = 1
train_factor = 0.7
population_size = 20
secret_key = "secret_key"

def calc_fitness(weights):
    cal_fitness = []
    errors = []
    for i in range(population_size):
        error = get_errors(secret_key , list(weights[i]))
        cal_fitness.append(abs(train_factor*error[0] + validate_factor*error[1]))
        errors.append(error)

    cal_fitness = np.array(cal_fitness)
    idx = np.where(cal_fitness == np.amin(cal_fitness))
    error_file = open('./errors_now.txt' , "a")
    error_file.write(str(errors[idx[0][0]]))
    error_file.write('\n')
    error_file.close()
    print('Fitness')
    print(cal_fitness)   
    return cal_fitness    
        

# Initial Vector to Create Initial Population
overfit_file = open('./overfit_now.txt' , 'r')
initial_weight = overfit_file.read()
overfit_file.close()

initial_weight = initial_weight[1:len(initial_weight) - 1]
initial_weight = initial_weight.replace(" ","")
initial_weight = initial_weight.split(',')
initial_weight = list(map(float, initial_weight))
initial_w = np.array(initial_weight)

# print(initial_w)
# print(type(initial_w))

# Inital Population

population_child = np.vstack([initial_w]*population_size)
population_parent = np.vstack([initial_w]*population_size)
# print(initial_population)

fitness_prev = np.empty(population_size)
fitness_now = np.empty(population_size)

mutate_prob = np.empty(population_size)

f = open('./generations/generation_now.txt' , "a")

for i in range(genaration_size):
    s = 'Generation' + str(i+1)
    f.write(s)
    f.write('\n')
    print('Generation ' + str(i+1))
    # calculate fitness
    if i > 0:
        fitness_now = calc_fitness(population_child)
        population_child = np.column_stack((population_child , fitness_now))
        population_child = population_child[np.argsort(population_child[:,-1])]
        population_child = np.delete(population_child , -1 , 1)
        fitness_now = np.sort(fitness_now)

    else:
        error = get_errors(secret_key , list(population_child[0]))
        fitness_0 = abs(train_factor*error[0] + validate_factor*error[1])
        error_file = open('./errors_now.txt' , "a")
        error_file.write(str(error))
        error_file.write('\n')
        error_file.close()
        calcu_fitness = []
        for i in range(population_size):
            calcu_fitness.append(fitness_0)

        fitness_now = np.array(calcu_fitness)    
       

    f.write("Initial Population")
    f.write('\n')
    print('Initial Population')
    if i > 0:
       f.write(str(population_parent))
       f.write('\n')
       print(population_parent)

    else:
        f.write(str(population_child))
        f.write('\n')
        print(population_child)   
    # Make the mating pool and fitness of mating pool

    if len(fitness_prev) > 0:
        ind = 0
        j = 0
        current_population = []
        fitness = []
        for k in range(population_size):
            if fitness_now[ind] < fitness_prev[j]:
                current_population.append(population_child[ind])
                fitness.append(fitness_now[ind])
                ind = ind + 1

            else:
                current_population.append(population_parent[j])
                fitness.append(fitness_prev[j])
                j = j + 1

        current_population = np.array(current_population)
        fitness = np.array(fitness)
        population_parent = copy.deepcopy(current_population)
        fitness_prev = copy.deepcopy(fitness)             

    else:
        population_parent = copy.deepcopy(population_child)
        fitness_prev = copy.deepcopy(fitness_now)
    
    f.write("After Selection")
    f.write('\n')
    f.write(str(population_parent))
    f.write('\n')
    print('After Selection')
    print(population_parent)

    # Crossover 
    crossover_point = int(11/2)
    mutate = []
    for j in range(population_size):
        parent_x_indx = j % population_size
        parent_y_indx = (j + 1) % population_size
        population_child[j , 0 : crossover_point + 1] = population_parent[parent_x_indx , 0 : crossover_point + 1]
        population_child[j , crossover_point + 1 :] = population_parent[parent_y_indx , crossover_point + 1 :]
        mutate.append(random.randint(0,10))

    mutate_prob = np.array(mutate)

    f.write("After Crossover")
    f.write('\n')
    f.write(str(population_child))
    f.write('\n')
    print('After Crossover')
    print(population_child)

    # Mutation
    for j in range(population_size):
        if mutate_prob[j] >= 3 and mutate_prob[j] < 7:
            idx = random.randint(0,5)
            idx_1 = random.randint(6,10)
            population_child[j][idx] , population_child[j][idx_1] = population_child[j][idx_1] , population_child[j][idx]


        elif mutate_prob[j] >= 7:
            idx = random.randint(0,10)
            idx_1 = random.randint(0,10)
            if abs(random.uniform(0.3, 1.6) * population_child[j][idx]) < 10:
                population_child[j][idx] = random.uniform(0.3, 1.6) * population_child[j][idx]

            if abs(random.uniform(0.3, 1.6) * population_child[j][idx_1]) < 10:
                population_child[j][idx_1] = random.uniform(0.3, 1.6) * population_child[j][idx_1]    

    f.write("After Mutation")
    f.write('\n')
    f.write(str(population_child))
    f.write('\n')        
    print('After Mutation')
    print(population_child)

f.close()
fitness_now = calc_fitness(population_child)
population_child = np.column_stack((population_child , fitness_now))
population_child = population_child[np.argsort(population_child[:,-1])]
population_child = np.delete(population_child , -1 , 1)
fitness_now = np.sort(fitness_now)

overfit_file = open('./overfit_now.txt' , "w")
if fitness_now[0] < fitness_prev[0]:
    overfit_file.write(str(list(population_child[0])))

else:
    overfit_file.write(str(list(population_parent[0])))

overfit_file.close()    
