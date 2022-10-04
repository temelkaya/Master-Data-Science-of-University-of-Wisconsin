# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 18:08:03 2022

@author: temel
"""
#Subtask 2.1
import numpy as np

def simulate_revenue(average, std_dev, months):
    revenue = []
    for i in range(months):
        sample = np.random.normal(average, std_dev)
        revenue.append(round(sample))
    return np.array(revenue)

#Subtask 2.2
def main():
    before = simulate_revenue(100000, 2000, 24)
    after = simulate_revenue(103000, 4000, 12)

    all_months=np.concatenate([before, after])

    print_monthly_revenue(before, "before")
    
    print()
    print_monthly_revenue(after, "after")
   
    print()
    print_monthly_revenue(all_months, "Total")

#Subtask 2.3
def print_monthly_revenue(revenue, name):
    print('Revenue for period \'' + name + '\'\n')
    print('Mo: Revenue')
    print('-----------')

    for month in range(len(revenue)):
        rev = round(revenue[month] / 100) * 100
       
        if month < 9:
            print('0' + str(month + 1), end=':')
        else:
            print(str(month + 1), end=':')
        print(str(rev).rjust(8))

if __name__ == '__main__':
    main()

#Subtask 3.1: Random data

import random
import numpy 
import datetime 

def simulate_busses(mean, num_busses): 
	vec_time = [] 
	for i in range(num_busses): 
		time = random.expovariate(float(1/mean)) 
		time = round(time, 2)
		vec_time.append(time) 
	
	return vec_time 


def cumulative_wait(bus_times):
	cumulative_vec_times = [] 
	length = len(bus_times) 
	
	cumulative_vec_times.append(bus_times[0])
	

	for i in range(1, length):
		
		cumulative_time  = bus_times[i] + cumulative_vec_times[-1] 
		cumulative_vec_times.append(cumulative_time)
	
	return cumulative_vec_times 


def final_arrival_time(cum_wait_times):
	last_time = cum_wait_times[-1] 


	time_sec = last_time*60
	
	string_time = datetime.datetime(2020, 1, 1) + datetime.timedelta(seconds = time_sec)
	
	return string_time.strftime("%I:%M %p") 

bus_times = simulate_busses(15, 50)


print("The arrival intervals of the bus")
print(bus_times)
print()

print("Questions")
print("1 - What is the mean waiting time in your vector?")
mean_wait = sum(bus_times)/len(bus_times) 
mean_wait = round(mean_wait,2)
print(str(mean_wait)+"\n")

print("2 - What is the shortest waiting time?")
shortest_wait = min(bus_times) 
print(str(shortest_wait)+"\n")

print("3 - What is the longest waiting time?")
longest_wait = max(bus_times) 
print(str(longest_wait)+"\n")


#Subtask 3.3:Cumulative Wait Times
bus_times = cumulative_wait(bus_times)


bus_times = numpy.array(bus_times)

numpy.save("cum_wait_time.npy", bus_times)


print("Cumulative wait times")
print(bus_times)
print()

print("4 - At what time does the last bus arrive?")
print(final_arrival_time(bus_times))

#Task 4: Chocolate and the Nobel
import numpy 


def gen_choc_nobel(): 
    choc_nobel = numpy.zeros(shape=(50,2)) 

    for i in range(50): 
        choc = random.uniform(0, 15) 
        nobel = 0.4*choc-0.8 

        if(nobel < 0): nobel = 0 

        choc_nobel[i,0]=choc
        choc_nobel[i,1]=nobel

    return choc_nobel 


def perturb(array):
    length = len(array) 

    for i in range(length):
        epsilon = random.normalvariate(0,1) 
        n_e = array[i,1] + epsilon

        if(n_e < 0): 
            n_e = 0
        
        array[i,1] = n_e

    return array 



def simulate_choc_nobel(num_sims):
    sim_choc_nobel = numpy.ndarray(shape=(num_sims,50,2)) 

    for i in range(num_sims): 
        choc_nobel = gen_choc_nobel() 
        perturbed_choc_nobel = perturb(choc_nobel) 

        sim_choc_nobel[i] = perturbed_choc_nobel 

    return sim_choc_nobel 



def save_simulatios(simulations_choc_nobel):
    num_sims = len(simulations_choc_nobel) 
    num_rows = len(simulations_choc_nobel[0]) 

    text = "" 
    file = open("nobel.csv", "w") 

    for row in range(num_rows):
        for col in range(num_sims):
            text+=str(simulations_choc_nobel[col,row,0])+","+str(simulations_choc_nobel[col,row,1])+","
        text=text[:-1]+"\n"

    file.write(text) 
    file.close()

choc_nobel = gen_choc_nobel()


perturbed_choc_nobel = perturb(choc_nobel)

choc_winner = []
nobel_winner = [] 

for i in range(len(perturbed_choc_nobel)): 
    n_e = perturbed_choc_nobel[i,1] 
    c = perturbed_choc_nobel[i,0] 

    if(n_e > 0.4*c-0.8 and n_e != 0): 
        choc_winner.append(c)
        nobel_winner.append(n_e)



nobel_winners = numpy.zeros(shape=(len(nobel_winner), 2))
for i in range(len(nobel_winner)):
    nobel_winners[i,0] = choc_winner[i]
    nobel_winners[i,1] = nobel_winner[i]


number_of_winners = len(nobel_winners)
print("The number of Nobel winners: "+str(number_of_winners))

simulations_choc_nobel = simulate_choc_nobel(5)

save_simulatios(simulations_choc_nobel)
