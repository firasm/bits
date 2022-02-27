import random as rd
import numpy as np
import math
import pandas as pd
import problem_bank_helpers as pbh

def generate(data):
    data2 = pbh.create_data2()
    
    # define or load names/items/objects from server files
    names = pbh.names.copy()
    
    # store phrases etc
    data2["params"]["vars"]["title"] = "Terminal Velocity of a Coffee Filter"
    data2["params"]["vars"]["name"] = rd.choice(names)
    data2["params"]["vars"]["unit1"] = "$m/s$"
    data2["params"]["vars"]["unit2"] = "$kg/s$"
    
    # define bounds of the variables
    m = rd.randint(1,5) 
    d_m = rd.randint(30,60) # uncertainty in mass
    
    # store the variables in the dictionary "params"
    data2["params"]["m"] = m
    data2["params"]["d_m"] = d_m
    
    # define g
    g = 9.81 
    
    # generate the table
    v_meas = [pbh.roundp(rd.uniform(0.70,0.99), sigfigs=2) for _ in range(6)]
    
    # calculate mean measured velocity and standard deviation
    mean = pbh.roundp(float(np.mean(v_meas)), sigfigs = 2)
    sd = pbh.roundp(float(np.std(v_meas)), sigfigs = 2)
    
    # save table values in dictionary
    data2["params"]["sd"] = sd
    values = ["v{0}".format(i+1) for i in range(6)]
    for x in v_meas:
      value = values.pop(0)
      data2["params"][value] = x
      
    ## Part 1
    # define correct answer, error in velocity
    d_vT = pbh.roundp(sd/math.sqrt(6), sigfigs = 1)
    data2["correct_answers"]["part1_ans"] = d_vT
    
    ## Part 2 
    # define correct answer, average velocity
    data2["correct_answers"]["part2_ans"] = mean
    
    # For part 3 and part 4, the rounded final answers from part 1 and part 2 are used (see solution)
    
    ## Part 3
    
    # define correct answer, error in b. 
    data2["correct_answers"]["part3_ans"] = (d_m/m)+(d_vT/mean)
    
    ## Part 4. 
    # define correct answer, b
    data2["correct_answers"]["part4_ans"] = (m*g)/mean
    
    # Update the data object with a new dict
    data.update(data2)
    
def prepare(data):
    pass
    
def parse(data):
    pass
    
def grade(data):
    pass
    
